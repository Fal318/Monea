EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_02x20_Odd_Even J?
U 1 1 61528489
P 5000 3900
F 0 "J?" H 5050 5017 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 5050 4926 50  0000 C CNN
F 2 "" H 5000 3900 50  0001 C CNN
F 3 "~" H 5000 3900 50  0001 C CNN
	1    5000 3900
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 615297EB
P 5600 2950
F 0 "#PWR?" H 5600 2800 50  0001 C CNN
F 1 "+5V" H 5615 3123 50  0000 C CNN
F 2 "" H 5600 2950 50  0001 C CNN
F 3 "" H 5600 2950 50  0001 C CNN
	1    5600 2950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 6152AB88
P 5600 3250
F 0 "#PWR?" H 5600 3000 50  0001 C CNN
F 1 "GND" H 5605 3077 50  0000 C CNN
F 2 "" H 5600 3250 50  0001 C CNN
F 3 "" H 5600 3250 50  0001 C CNN
	1    5600 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 3000 5600 3000
Wire Wire Line
	5600 3000 5600 2950
Wire Wire Line
	5300 3200 5600 3200
Wire Wire Line
	5600 3200 5600 3250
$Comp
L Connector:Conn_01x06_Female J?
U 1 1 6152C049
P 7300 3050
F 0 "J?" H 7328 3026 50  0000 L CNN
F 1 "Conn_01x06_Female" H 7328 2935 50  0000 L CNN
F 2 "" H 7300 3050 50  0001 C CNN
F 3 "~" H 7300 3050 50  0001 C CNN
	1    7300 3050
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Female J?
U 1 1 6152DF10
P 7300 3850
F 0 "J?" H 7328 3826 50  0000 L CNN
F 1 "Conn_01x04_Female" H 7328 3735 50  0000 L CNN
F 2 "" H 7300 3850 50  0001 C CNN
F 3 "~" H 7300 3850 50  0001 C CNN
	1    7300 3850
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x05_Female J?
U 1 1 6152E570
P 7300 4450
F 0 "J?" H 7328 4476 50  0000 L CNN
F 1 "Conn_01x05_Female" H 7328 4385 50  0000 L CNN
F 2 "" H 7300 4450 50  0001 C CNN
F 3 "~" H 7300 4450 50  0001 C CNN
	1    7300 4450
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 61535927
P 6800 2650
F 0 "#PWR?" H 6800 2500 50  0001 C CNN
F 1 "+3.3V" H 6815 2823 50  0000 C CNN
F 2 "" H 6800 2650 50  0001 C CNN
F 3 "" H 6800 2650 50  0001 C CNN
	1    6800 2650
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 61535F16
P 4500 2800
F 0 "#PWR?" H 4500 2650 50  0001 C CNN
F 1 "+3.3V" H 4515 2973 50  0000 C CNN
F 2 "" H 4500 2800 50  0001 C CNN
F 3 "" H 4500 2800 50  0001 C CNN
	1    4500 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 2800 4500 3000
Wire Wire Line
	4500 3000 4800 3000
Wire Wire Line
	6800 2650 6800 2850
Wire Wire Line
	6800 2850 7100 2850
$Comp
L power:GND #PWR?
U 1 1 61538D9A
P 6800 4800
F 0 "#PWR?" H 6800 4550 50  0001 C CNN
F 1 "GND" H 6805 4627 50  0000 C CNN
F 2 "" H 6800 4800 50  0001 C CNN
F 3 "" H 6800 4800 50  0001 C CNN
	1    6800 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	7100 2950 6800 2950
Wire Wire Line
	6800 2950 6800 3250
Wire Wire Line
	7100 3250 6800 3250
Connection ~ 6800 3250
NoConn ~ 7100 3050
Wire Wire Line
	7100 3350 5950 3350
Wire Wire Line
	5950 3350 5950 2600
Wire Wire Line
	4600 2600 4600 3200
Wire Wire Line
	4600 2600 5950 2600
Wire Wire Line
	4600 3200 4800 3200
Wire Wire Line
	4800 3100 4700 3100
Wire Wire Line
	4700 3100 4700 2700
Wire Wire Line
	6700 2700 6700 3150
Wire Wire Line
	6700 3150 7100 3150
Wire Wire Line
	4700 2700 6700 2700
Text Notes 7150 2750 0    50   ~ 0
BME280
$Comp
L power:+5V #PWR?
U 1 1 615BEF20
P 7000 3700
F 0 "#PWR?" H 7000 3550 50  0001 C CNN
F 1 "+5V" H 7015 3873 50  0000 C CNN
F 2 "" H 7000 3700 50  0001 C CNN
F 3 "" H 7000 3700 50  0001 C CNN
	1    7000 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 3700 7000 3750
Wire Wire Line
	7000 3750 7100 3750
Wire Wire Line
	7100 3850 6800 3850
Wire Wire Line
	6800 3250 6800 3750
Connection ~ 6800 3850
Wire Wire Line
	6800 3850 6800 4800
NoConn ~ 7100 3950
NoConn ~ 7100 4050
NoConn ~ 7100 4250
NoConn ~ 7100 4550
NoConn ~ 7100 4650
Text Notes 7350 4350 0    50   ~ 0
RX
Wire Wire Line
	7100 4350 5450 4350
Wire Wire Line
	5450 4350 5450 3300
Wire Wire Line
	5450 3300 5300 3300
Wire Wire Line
	5300 3400 5400 3400
Wire Wire Line
	5400 3400 5400 4450
Wire Wire Line
	5400 4450 7100 4450
$Comp
L LED:AE-WS2812B U?
U 1 1 615CA3ED
P 6050 3850
F 0 "U?" H 6050 4182 50  0000 C CNN
F 1 "AE-WS2812B" H 6050 4091 50  0000 C CNN
F 2 "" H 6050 4050 50  0001 C CNN
F 3 "" H 6050 4050 50  0001 C CNN
	1    6050 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 3200 5750 3200
Wire Wire Line
	5750 3200 5750 3750
Wire Wire Line
	5750 3750 5850 3750
Connection ~ 5600 3200
Wire Wire Line
	6250 3750 6800 3750
Connection ~ 6800 3750
Wire Wire Line
	6800 3750 6800 3850
Wire Wire Line
	6250 3950 7000 3950
Wire Wire Line
	7000 3950 7000 3750
Connection ~ 7000 3750
Wire Wire Line
	7000 3950 7000 4100
Wire Wire Line
	7000 4100 5750 4100
Wire Wire Line
	5750 4100 5750 3950
Wire Wire Line
	5750 3950 5850 3950
Connection ~ 7000 3950
$EndSCHEMATC
