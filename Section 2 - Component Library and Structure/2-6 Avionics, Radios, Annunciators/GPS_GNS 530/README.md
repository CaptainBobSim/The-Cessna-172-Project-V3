[Build Video Here](https://youtu.be/dMBtQhVhItA)

Purchase the Circuit Board Here: http://captainbobsim.com/product/gns-530-circuit-board/

Get a Kit Here: http://captainbobsim.com/product/gns-530-kit/
Get a fully assembled unit here: http://captainbobsim.com/product/gns-530-assembled/

Welcome to the Simulator of your dreams!

To navigate all of the files on your journey towards homecockpitness,
Source Files is where you'll find all of the raw files if you want to make any customizations for yourself. I provided the circuit board outline as a dxf if anyone wants to cut their own perfboard instead of getting a PCB. I'd highly recommend a PCB however as there are approximately 130 traces.

Bill 'o Materials:

Black, White, and Clear PLA
Arduino Pro Mega 2560x11 LED White, 3mm
x8 47ƒ¶ Resistors
x14 6x6x7 LED Tactile Push Buttons
x2 IDC 40 - Male
x4 Pin Headers Row - Female
Pin Headers Row - Male
x2 ALPS_EC11EBB24C03
x2 Encoder Plum 15mm
5 Inch 640x480 LCD Display with controller
GNS 530 PCB
x8 M3 8mm Countersunk
x4 M3 Heat Set Insert (Height 4mm)
x4 20mm F to F Standoff
x6 M3 12mm Countersunk
x4 M2 8mm Countersunk
10k ƒ¶ resistor
Photoresistor (Optional)
DC Shunt
HDMI Cable 2m
12V Power Cable

Pinout for Onboard Arduino:

| Pin | Function           |                       |              |
| --- | ------------------ | --------------------- | ------------ |
| 1   | GND                | GND                   |              |
| 2   | 5V                 | 5V                    |              |
| 3   | COM_SWAP           | Digital pin 10 (PWM)  | Button       |
| 4   | COM_POWER (BLANK!) | Digital pin 11 (PWM)  | Empty        |
| 5   | COM_A              | Digital pin 12 (PWM)  | Encoder      |
| 6   | COM_B              | Digital pin 44 (PWM)  | Encoder      |
| 7   | COM_PRESS          | Digital pin 45 (PWM)  | Button       |
| 8   | NAV_SWAP           | Digital pin 46 (PWM)  | Button       |
| 9   | NAV_A              | Digital pin 47        | Encoder      |
| 10  | NAV_B              | Digital pin 48        | Encoder      |
| 11  | NAV_PRESS          | Digital pin 49        | Button       |
| 12  | L-FINE_A           | Digital pin 50 (MISO) | Encoder      |
| 13  | L-FINE_B           | Digital pin 51 (MOSI) | Encoder      |
| 14  | L-ROUGH_A          | Digital pin 52 (SCK)  | Encoder      |
| 15  | L-ROUGH_B          | Digital pin 53 (SS)   | Encoder      |
| 16  | L_PRESS            | Digital pin 33        | Button       |
| 17  | CDI                | Digital pin 34        | Button       |
| 18  | OBS                | Digital pin 35        | Button       |
| 19  | MSG                | Digital pin 36        | Button       |
| 20  | FPL                | Digital pin 37        | Button       |
| 21  | VNAV               | Digital pin 38        | Button       |
| 22  | PROC               | Digital pin 39        | Button       |
| 23  | R_FINEA            | Digital pin 40        | Encoder      |
| 24  | R_FINEB            | Digital pin 41        | Encoder      |
| 25  | R_ROUGHA           | Digital pin 42        | Encoder      |
| 26  | R_ROUGHB           | Digital pin 43        | Encoder      |
| 27  | R_PRESS            | Analog pin 5          | Button       |
| 28  | ENT                | Analog pin 6          | Button       |
| 29  | CLR                | Analog pin 7          | Button       |
| 30  | MENU               | Analog pin 10         | Button       |
| 31  | DIRECT             | Analog pin 11         | Button       |
| 32  | RNG_DN             | Analog pin 12         | Button       |
| 33  | RNG_UP             | Analog pin 13         | Button       |
| 34  | ___(BLANK)___      |                       | Empty        |
| 35  | ___(BLANK)___      |                       | Empty        |
| 36  | ___(BLANK)___      |                       | Empty        |
| 37  | ___(BLANK)___      |                       | Empty        |
| 38  | ___(BLANK)___      |                       | Empty        |
| 39  | PHOTORESISTOR      | Analog pin 14         | Analog Input |
| 40  | ANALOG_EXTRA       | Analog pin 15         | Analog Input |


Pinout for EXTRA PINS Pin Header.
| Pin | Function             | Arduino Pin  |
|-----|----------------------|--------------|
|   1 | GND                  |              |
|   2 | 5V                   |              |
|   3 | Digital pin 2 (PWM)  |    Button    |
|   4 | Digital pin 3 (PWM)  |     Empty    |
|   5 | Digital pin 4 (PWM)  |    Encoder   |
|   6 | Digital pin 5 (PWM)  |    Encoder   |
|   7 | Digital pin 14 (TX3) |    Button    |
|   8 | Digital pin 15 (RX3) |    Button    |
|   9 | Digital pin 16 (TX2) |    Encoder   |
|  10 | Digital pin 17 (RX2) |    Encoder   |
|  11 | Digital pin 18 (TX1) |    Button    |
|  12 | Digital pin 19 (RX1) |    Encoder   |
|  13 | Digital pin 20 (SDA) |    Encoder   |
|  14 | Digital pin 21 (SCL) |    Encoder   |
|  15 | Digital pin 22       |    Encoder   |
|  16 | Analog pin 0         |    Button    |
|  17 | Analog pin 1         |    Button    |
|  18 | Analog pin 2         |    Button    |
|  19 | Analog pin 3         |    Button    |
|  20 | Analog pin 4         |    Button    |
|  21 | Digital pin 23       |    Button    |
|  22 | Digital pin 24       |    Button    |
|  23 | Digital pin 6 (PWM)  |    Encoder   |
|  24 | Digital pin 7 (PWM)  |    Encoder   |
|  25 | Digital pin 8 (PWM)  |    Encoder   |
|  26 | Digital pin 9 (PWM)  |    Encoder   |
|  27 | Digital pin 25       |    Button    |
|  28 | Digital pin 26       |    Button    |
|  29 | Digital pin 27       |    Button    |
|  30 | Digital pin 28       |    Button    |
|  31 | Digital pin 29       |    Button    |
|  32 | Digital pin 30       |    Button    |
|  33 | Digital pin 31       |    Button    |
|  34 | Digital pin 32       |     Empty    |
|  35 |                      |     Empty    |
|  36 |                      |     Empty    |
|  37 |                      |     Empty    |
|  38 |                      |     Empty    |
|  39 | Analog pin 8         | Analog Input |
|  40 | Analog pin 9         | Analog Input |


YOU MAY NOT SELL THESE WITHOUT PERMISSION
**[Copyright _ Non Commerical_ Not for Resale](https://creativecommons.org/licenses/by-nc/4.0/)**
Contact CaptainBobSim@gmail.com for licensing details.
