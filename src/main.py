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
t_fine = 0


def writeReg(reg_address, data):
    bus.write_byte_data(i2c_address, reg_address, data)


def get_calib_param():
    calib = []

    for i in range(0x88, 0x88+24):
        calib.append(bus.read_byte_data(i2c_address, i))
    calib.append(bus.read_byte_data(i2c_address, 0xA1))
    for i in range(0xE1, 0xE1+7):
        calib.append(bus.read_byte_data(i2c_address, i))
    for i in range(0, 5, 2):
        digT.append((calib[i+1] << 8) | calib[i])
    for i in range(6, 23, 2):
        digP.append((calib[i+1] << 8) | calib[i])

    digH.append(calib[24])
    digH.append((calib[26] << 8) | calib[25])
    digH.append(calib[27])
    digH.append((calib[28] << 4) | (0x0F & calib[29]))
    digH.append((calib[30] << 4) | ((calib[29] >> 4) & 0x0F))
    digH.append(calib[31])

    digT[1] = (-digT[1] ^ 0xFFFF) + 1 if digT[1] & 0x8000 else digT[1]

    for i in range(1, 8):
        if digP[i] & 0x8000:
            digP[i] = (-digP[i] ^ 0xFFFF) + 1

    for i in range(6):
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
    prs = 0

    v1 = (t_fine - 128000) / 2
    v2 = (v1 / 4)**2 * digP[5] / 2048
    v2 += v1 * digP[4] * 2
    v2 = v2 / 4 + digP[3] * 65536
    v1 = digP[2] * (v1 / 4)**2 / 65536 + digP[1] * v1 / 131072
    v1 = digP[1] * (1 + v1 / 32768)

    if v1 == 0:
        return 0
    prs = ((1048576 - adc_P) - (v2 / 4096)) * 3125
    prs = (prs * 2) / v1 if prs < 0x80000000 else (prs / v1) * 2
    v1 = digP[8] * (prs / 8) ** 2 / 33554432
    v2 = prs * digP[7] / 32768
    prs += (v1 + v2 + digP[6]) / 16

    print(f"pressure : {(prs/100):.1f} hPa")
    return prs


def get_temp(adc_T) -> float:
    global t_fine
    v1 = (adc_T / 16384 - digT[0] / 1024) * digT[1]

    v2 = digT[2]*(adc_T / 131072 - digT[0] / 8192) ** 2

    t_fine = v1 + v2
    temperature = t_fine / 5120
    print(f"temp : {temperature:.1f} ℃")
    return temperature


def get_hum(adc_H) -> float:
    global t_fine
    hum = t_fine - 76800

    if hum == 0:
        return 0
    else:
        hum = (adc_H - (digH[3] * 64 + digH[4]/16384 * hum)) * (digH[1] / 65536 * (
            1 + digH[5] / 67108864 * hum * (1 + digH[2] / 67108864 * hum)))
    hum = hum * (1 - digH[0] * hum / 524288)
    hum = 100 if hum > 100 else 0 if hum < 0 else hum
    print(f"hum : {hum:.1f} ％")
    return hum


def setup():
    writeReg(0xF2, 1)
    writeReg(0xF4, 39)
    writeReg(0xF5, 160)


def send_data(co2: float, temp: float, hum: float, pres: float):
    url = 'https://monea-api.herokuapp.com/api/v1/record'
    sensor_id = os.environ.get("MONEA_ID")
    if sensor_id is None:
        exit("MONEA_ID is not defined")
    params = {
        "created": time.time(),
        "co2": co2,
        "humid": hum,
        "temp": temp,
        "pressure": pres,
        "sensorId": sensor_id
    }
    requests.post(url, json=params)


if __name__ == '__main__':
    setup()
    get_calib_param()
    try:
        temp, hum, pres = readData()
        #temp, hum, pres = -297, -1, -1
        send_data(temp=temp, hum=hum, pres=pres, co2=co2)
    except KeyboardInterrupt:
        pass
    finally:
        print(f"co2: {co2.co2} ppm")
