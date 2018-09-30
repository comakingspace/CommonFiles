EESchema Schematic File Version 4
LIBS:CNC_Control_Panel-cache
EELAYER 26 0
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
L Switch:SW_Push SW_OnOffButton1
U 1 1 5BA3FFC9
P 6450 800
F 0 "SW_OnOffButton1" H 6450 1085 50  0000 C CNN
F 1 "SW_Push_Dual" H 6450 994 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6450 1000 50  0001 C CNN
F 3 "" H 6450 1000 50  0001 C CNN
	1    6450 800 
	1    0    0    -1  
$EndComp
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 5BA3FE7F
P 4250 2350
F 0 "J1" H 4250 3828 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 4250 3737 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 4250 2350 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 4250 2350 50  0001 C CNN
	1    4250 2350
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_$X_Unlock1
U 1 1 5BA41125
P 6400 1500
F 0 "SW_$X_Unlock1" H 6400 1785 50  0000 C CNN
F 1 "SW_Push_Dual" H 6400 1694 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6400 1700 50  0001 C CNN
F 3 "" H 6400 1700 50  0001 C CNN
	1    6400 1500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_$H_Home1
U 1 1 5BA41145
P 6450 2250
F 0 "SW_$H_Home1" H 6450 2535 50  0000 C CNN
F 1 "SW_Push_Dual" H 6450 2444 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6450 2450 50  0001 C CNN
F 3 "" H 6450 2450 50  0001 C CNN
	1    6450 2250
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_Left1
U 1 1 5BA41170
P 6500 3350
F 0 "SW_Left1" H 6500 3635 50  0000 C CNN
F 1 "SW_Push_Dual" H 6500 3544 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 6500 3550 50  0001 C CNN
F 3 "" H 6500 3550 50  0001 C CNN
	1    6500 3350
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_Right1
U 1 1 5BA411A3
P 7850 3350
F 0 "SW_Right1" H 7850 3635 50  0000 C CNN
F 1 "SW_Push_Dual" H 7850 3544 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 7850 3550 50  0001 C CNN
F 3 "" H 7850 3550 50  0001 C CNN
	1    7850 3350
	1    0    0    -1  
$EndComp
$Comp
L LED:SFH4346 D_OnOff1
U 1 1 5BA41476
P 5850 800
F 0 "D_OnOff1" H 5800 1090 50  0000 C CNN
F 1 "SFH4346" H 5800 999 50  0000 C CNN
F 2 "LED_THT:LED_D3.0mm_IRBlack" H 5850 975 50  0001 C CNN
F 3 "http://cdn-reichelt.de/documents/datenblatt/A500/SFH4346.pdf" H 5800 800 50  0001 C CNN
	1    5850 800 
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_Y_Up1
U 1 1 5BA416AC
P 7200 2700
F 0 "SW_Y_Up1" H 7200 2985 50  0000 C CNN
F 1 "SW_Push_Dual" H 7200 2894 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 7200 2900 50  0001 C CNN
F 3 "" H 7200 2900 50  0001 C CNN
	1    7200 2700
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_Y_Down1
U 1 1 5BA416B4
P 7250 4000
F 0 "SW_Y_Down1" H 7250 4285 50  0000 C CNN
F 1 "SW_Push_Dual" H 7250 4194 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 7250 4200 50  0001 C CNN
F 3 "" H 7250 4200 50  0001 C CNN
	1    7250 4000
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_Z_Up1
U 1 1 5BA41747
P 8750 2950
F 0 "SW_Z_Up1" H 8750 3235 50  0000 C CNN
F 1 "SW_Push_Dual" H 8750 3144 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 8750 3150 50  0001 C CNN
F 3 "" H 8750 3150 50  0001 C CNN
	1    8750 2950
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_Push SW_Z_Down1
U 1 1 5BA4174F
P 8750 3550
F 0 "SW_Z_Down1" H 8750 3835 50  0000 C CNN
F 1 "SW_Push_Dual" H 8750 3744 50  0000 C CNN
F 2 "Button_Switch_THT:SW_PUSH_6mm" H 8750 3750 50  0001 C CNN
F 3 "" H 8750 3750 50  0001 C CNN
	1    8750 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 800  5550 800 
Wire Wire Line
	6650 2050 5050 2050
Wire Wire Line
	6600 1500 6600 1450
Wire Wire Line
	6600 1450 5050 1450
Wire Wire Line
	7400 2700 7400 2350
Wire Wire Line
	7400 2350 5050 2350
Wire Wire Line
	5050 2350 5050 2450
Wire Wire Line
	6700 2550 5050 2550
Wire Wire Line
	8050 2650 5050 2650
Wire Wire Line
	7450 4000 7450 2750
Wire Wire Line
	7450 2750 5050 2750
Wire Wire Line
	8950 2950 8950 2850
Wire Wire Line
	8950 2850 5050 2850
Wire Wire Line
	3450 1450 3450 650 
Wire Wire Line
	3450 650  5950 650 
Wire Wire Line
	5950 650  5950 800 
Wire Wire Line
	4550 3650 4550 4300
Wire Wire Line
	6200 1500 6200 550 
Wire Wire Line
	5550 800  5550 550 
Wire Wire Line
	5550 550  6200 550 
Connection ~ 5550 800 
Wire Wire Line
	5550 800  5500 800 
Connection ~ 6200 550 
Connection ~ 6300 4300
Connection ~ 7650 4300
Wire Wire Line
	7650 4300 8450 4300
Connection ~ 8550 4300
Wire Wire Line
	8550 4300 9450 4300
$Comp
L Device:R R1
U 1 1 5BB0F5EE
P 6800 1000
F 0 "R1" V 6593 1000 50  0000 C CNN
F 1 "100k" V 6684 1000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 6730 1000 50  0001 C CNN
F 3 "~" H 6800 1000 50  0001 C CNN
	1    6800 1000
	0    1    1    0   
$EndComp
Wire Wire Line
	9450 550  9450 4300
Wire Wire Line
	9250 700  6950 700 
Connection ~ 6650 2250
Wire Wire Line
	6550 2250 6650 2250
Wire Wire Line
	6650 2150 6650 2250
Wire Wire Line
	5050 2150 6650 2150
Wire Wire Line
	6700 2550 6700 3350
Wire Wire Line
	8050 2650 8050 3350
Wire Wire Line
	9250 700  9250 1500
Wire Wire Line
	9250 4250 8350 4250
Wire Wire Line
	6950 1000 6950 700 
Connection ~ 6950 700 
Connection ~ 6650 1000
Wire Wire Line
	6650 1000 6650 2050
Wire Wire Line
	6650 800  6650 1000
Wire Wire Line
	6250 800  6250 550 
$Comp
L Device:R R2
U 1 1 5BB41087
P 7100 1500
F 0 "R2" V 6893 1500 50  0000 C CNN
F 1 "100k" V 6984 1500 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 7030 1500 50  0001 C CNN
F 3 "~" H 7100 1500 50  0001 C CNN
	1    7100 1500
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5BB410DF
P 6800 2250
F 0 "R3" V 6593 2250 50  0000 C CNN
F 1 "100k" V 6684 2250 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 6730 2250 50  0001 C CNN
F 3 "~" H 6800 2250 50  0001 C CNN
	1    6800 2250
	0    1    1    0   
$EndComp
$Comp
L Device:R R5
U 1 1 5BB41137
P 7550 2700
F 0 "R5" V 7343 2700 50  0000 C CNN
F 1 "100k" V 7434 2700 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 7480 2700 50  0001 C CNN
F 3 "~" H 7550 2700 50  0001 C CNN
	1    7550 2700
	0    1    1    0   
$EndComp
Connection ~ 7400 2700
$Comp
L Device:R R4
U 1 1 5BB411F4
P 6850 3350
F 0 "R4" V 6643 3350 50  0000 C CNN
F 1 "100k" V 6734 3350 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 6780 3350 50  0001 C CNN
F 3 "~" H 6850 3350 50  0001 C CNN
	1    6850 3350
	0    1    1    0   
$EndComp
Connection ~ 6700 3350
$Comp
L Device:R R6
U 1 1 5BB4128A
P 7600 4000
F 0 "R6" V 7393 4000 50  0000 C CNN
F 1 "100k" V 7484 4000 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 7530 4000 50  0001 C CNN
F 3 "~" H 7600 4000 50  0001 C CNN
	1    7600 4000
	0    1    1    0   
$EndComp
Connection ~ 7450 4000
Wire Wire Line
	7000 3200 7200 3200
Wire Wire Line
	7200 3200 7200 3500
Wire Wire Line
	7200 3500 7000 3500
Wire Wire Line
	7000 3500 7000 4300
Wire Wire Line
	6300 4300 7000 4300
Connection ~ 7000 4300
Wire Wire Line
	7000 3350 7000 3450
Wire Wire Line
	7000 3450 6850 3450
Wire Wire Line
	6850 3450 6850 4250
Wire Wire Line
	7750 4000 7750 4250
Connection ~ 7750 4250
Wire Wire Line
	7750 4250 6850 4250
$Comp
L Device:R R7
U 1 1 5BB45AC1
P 8200 3350
F 0 "R7" V 7993 3350 50  0000 C CNN
F 1 "100k" V 8084 3350 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 8130 3350 50  0001 C CNN
F 3 "~" H 8200 3350 50  0001 C CNN
	1    8200 3350
	0    1    1    0   
$EndComp
Connection ~ 8050 3350
$Comp
L Device:R R8
U 1 1 5BB45B27
P 9100 2950
F 0 "R8" V 8893 2950 50  0000 C CNN
F 1 "100k" V 8984 2950 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 9030 2950 50  0001 C CNN
F 3 "~" H 9100 2950 50  0001 C CNN
	1    9100 2950
	0    1    1    0   
$EndComp
Connection ~ 9250 2950
Wire Wire Line
	9250 2950 9250 3550
Connection ~ 8950 2950
$Comp
L Device:R R9
U 1 1 5BB45BCE
P 9100 3550
F 0 "R9" V 8893 3550 50  0000 C CNN
F 1 "100k" V 8984 3550 50  0000 C CNN
F 2 "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal" V 9030 3550 50  0001 C CNN
F 3 "~" H 9100 3550 50  0001 C CNN
	1    9100 3550
	0    1    1    0   
$EndComp
Connection ~ 9250 3550
Wire Wire Line
	9250 3550 9250 4250
Wire Wire Line
	8350 3350 8350 4250
Connection ~ 8350 4250
Wire Wire Line
	8350 4250 7750 4250
Wire Wire Line
	7700 2700 9250 2700
Connection ~ 9250 2700
Wire Wire Line
	9250 2700 9250 2950
Wire Wire Line
	6950 2250 9250 2250
Connection ~ 9250 2250
Wire Wire Line
	9250 2250 9250 2700
Connection ~ 9250 1500
Wire Wire Line
	9250 1500 9250 2250
Wire Wire Line
	7000 4300 7050 4300
Wire Wire Line
	6250 4300 6300 4300
Wire Wire Line
	4550 4300 6250 4300
Connection ~ 6250 4300
Wire Wire Line
	6250 2250 6250 4300
Wire Wire Line
	8550 3550 8550 4300
Wire Wire Line
	7650 3350 7650 4300
Wire Wire Line
	7050 4000 7050 4300
Wire Wire Line
	6300 3350 6300 4300
Wire Wire Line
	7000 2700 7000 3200
Connection ~ 7050 4300
Wire Wire Line
	7050 4300 7650 4300
Wire Wire Line
	8550 2950 8450 2950
Wire Wire Line
	8450 2950 8450 4300
Connection ~ 8450 4300
Wire Wire Line
	8450 4300 8550 4300
Wire Wire Line
	4350 700  4350 1050
Wire Wire Line
	4350 700  6950 700 
Connection ~ 6250 550 
Wire Wire Line
	6250 550  9450 550 
Wire Wire Line
	6200 550  6250 550 
Wire Wire Line
	6600 1500 6950 1500
Connection ~ 6600 1500
Wire Wire Line
	7250 1500 9250 1500
Wire Wire Line
	8950 3550 8950 3050
Wire Wire Line
	8950 3050 5050 3050
Connection ~ 8950 3550
$EndSCHEMATC
