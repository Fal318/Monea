#coding: utf-8
import os
import time
import requests
from smbus2 import SMBus
import mh_z19

co2 = mh_z19.read()
bus_number, i2c_address = 1, 0x76
bus = SMBus(bus_number)
digT, digP, digH = [], [], []
t_fine = 0.0


def writeReg(reg_address, data):
    bus.write_byte_data(i2c_address, reg_address, data)


def get_calib_param():
    calib = []

    for i in range(0x88, 0x88+24):
        calib.append(bus.read_byte_data(i2c_address, i))
    calib.append(bus.read_byte_data(i2c_address, 0xA1))
    for i in range(0xE1, 0xE1+7):
        calib.append(bus.read_byte_data(i2c_address, i))

    digT.append((calib[1] << 8) | calib[0])
    digT.append((calib[3] << 8) | calib[2])
    digT.append((calib[5] << 8) | calib[4])
    digP.append((calib[7] << 8) | calib[6])
    digP.append((calib[9] << 8) | calib[8])
    digP.append((calib[11] << 8) | calib[10])
    digP.append((calib[13] << 8) | calib[12])
    digP.append((calib[15] << 8) | calib[14])
    digP.append((calib[17] << 8) | calib[16])
    digP.append((calib[19] << 8) | calib[18])
    digP.append((calib[21] << 8) | calib[20])
    digP.append((calib[23] << 8) | calib[22])
    digH.append(calib[24])
    digH.append((calib[26] << 8) | calib[25])
    digH.append(calib[27])
    digH.append((calib[28] << 4) | (0x0F & calib[29]))
    digH.append((calib[30] << 4) | ((calib[29] >> 4) & 0x0F))
    digH.append(calib[31])
    for i in range(1, 2):
        if digT[i] & 0x8000:
            digT[i] = (-digT[i] ^ 0xFFFF) + 1

    for i in range(1, 8):
        if digP[i] & 0x8000:
            digP[i] = (-digP[i] ^ 0xFFFF) + 1

    for i in range(0, 6):
        if digH[i] & 0x8000:
            digH[i] = (-digH[i] ^ 0xFFFF) + 1


def readData():
    data = []
    for i in range(0xF7, 0xF7+8):
        data.append(bus.read_byte_data(i2c_address, i))
    pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
    temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
    hum_raw = (data[6] << 8) | data[7]

    return [get_temp(temp_raw), get_hum(hum_raw), get_pressure(pres_raw)]


def get_pressure(adc_P):
    global t_fine
    pressure = 0.0

    v1 = (t_fine / 2.0) - 64000.0
    v2 = (((v1 / 4.0) * (v1 / 4.0)) / 2048) * digP[5]
    v2 = v2 + ((v1 * digP[4]) * 2.0)
    v2 = (v2 / 4.0) + (digP[3] * 65536.0)
    v1 = (((digP[2] * (((v1 / 4.0) * (v1 / 4.0)) / 8192)) / 8) +
          ((digP[1] * v1) / 2.0)) / 262144
    v1 = ((32768 + v1) * digP[0]) / 32768

    if v1 == 0:
        return 0
    pressure = ((1048576 - adc_P) - (v2 / 4096)) * 3125
    pressure = (pressure * 2.0) / \
        v1 if pressure < 0x80000000 else (pressure / v1) * 2
    v1 = (digP[8] * (((pressure / 8.0) * (pressure / 8.0)) / 8192.0)) / 4096
    v2 = ((pressure / 4.0) * digP[7]) / 8192.0
    pressure = pressure + ((v1 + v2 + digP[6]) / 16.0)

    print(f"pressure : {(pressure/100):.1f} hPa")
    return pressure


def get_temp(adc_T) -> float:
    global t_fine
    v1 = (adc_T / 16384.0 - digT[0] / 1024.0) * digT[1]
    v2 = (adc_T / 131072.0 - digT[0] / 8192.0) * \
        (adc_T / 131072.0 - digT[0] / 8192.0) * digT[2]
    t_fine = v1 + v2
    temperature = t_fine / 5120.0
    print(f"temp : {temperature:.1f} ℃")
    return temperature


def get_hum(adc_H):
    global t_fine
    hum = t_fine - 76800.0

    if hum == 0:
        return 0
    else:
        hum = (adc_H - (digH[3] * 64.0 + digH[4]/16384.0 * hum)) * (digH[1] / 65536.0 * (
            1.0 + digH[5] / 67108864.0 * hum * (1.0 + digH[2] / 67108864.0 * hum)))
    hum = hum * (1.0 - digH[0] * hum / 524288.0)
    hum = 100.0 if hum > 100.0 else 0.0 if hum < 0.0 else hum
    print(f"hum : {hum:.1f} ％")
    return hum


def setup():
    osrs_t, osrs_p, osrs_h = 1, 1, 1
    mode, t_sb, filter, spi3w_en = 3, 5, 0, 0

    ctrl_meas_reg = (osrs_t << 5) | (osrs_p << 2) | mode
    config_reg = (t_sb << 5) | (filter << 2) | spi3w_en
    ctrl_hum_reg = osrs_h

    writeReg(0xF2, ctrl_hum_reg)
    writeReg(0xF4, ctrl_meas_reg)
    writeReg(0xF5, config_reg)


def send_data(sensor_id: str, temp: float, hum: float, co2: float):
    url = 'https://monea-api.herokuapp.com/api/v0/record'
    params = {
        "created": time.time(),
        "co2": co2,
        "humid": hum,
        "temp": temp,
        "sensorId": sensor_id
    }
    requests.post(url, json=params)


setup()
get_calib_param()


if __name__ == '__main__':
    try:
        sensor_id = os.environ.get("MONEA_ID")
        if sensor_id is None:
            exit("MONEA_ID is not defined")
        temp, hum, pres = readData()
        send_data(temp=temp, hum=hum, co2=co2)
    except KeyboardInterrupt:
        pass
    finally:
        print(f"co2: {co2.co2} ppm")
