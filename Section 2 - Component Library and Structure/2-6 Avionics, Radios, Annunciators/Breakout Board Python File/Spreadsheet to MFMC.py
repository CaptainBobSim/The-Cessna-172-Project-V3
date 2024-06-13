spreadsheet_data = """
GND		GND
5V		5V
Test 1	Digital pin 2 (PWM)	LED / Output
UnNamed_DIN	Digital pin 3 (PWM)	LED 7-Segment
UnNamed_CS	Digital pin 4 (PWM)	LED 7-Segment
Named_CLK	Digital pin 5 (PWM)	LED 7-Segment
Name 2	Digital pin 6 (PWM)	Servo
DaAirspeed_IN1	Digital pin 7 (PWM)	Stepper
DaAirspeed_IN2	Digital pin 8 (PWM)	Stepper
DaAirspeed_IN3	Digital pin 9 (PWM)	Stepper
DaAirspeed_IN4	Digital pin 10 (PWM)	Stepper
LcdDisplay_SDA	Digital pin 20 (SDA)	LCD Display
LcdDisplay_SCL	Digital pin 21 (SCL)	LCD Display
This is a name	Digital pin 11 (PWM)	Button
Name 3_A	Digital pin 12 (PWM)	Encoder
Name 3_B	Digital pin 13 (PWM)	Encoder
Throttle	Analog pin 0	Analog Input
Blank	Digital pin 18 (TX1)	Empty
blah2	Digital pin 14 (TX3)	LED / Output
Trim	Analog pin 1	Analog Input
Joystick	Analog pin 2	Analog Input
"""

import xml.etree.ElementTree as ET

def create_xml_from_data(data):
    lines = data.strip().split('\n')
    root = ET.Element('Config', {
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xmlns:xsd': "http://www.w3.org/2001/XMLSchema"
    })
    module_type = ET.SubElement(root, 'ModuleType')
    module_type.text = 'MobiFlight Mega'
    module_name = ET.SubElement(root, 'ModuleName')
    module_name.text = 'test file'
    power_saving_time = ET.SubElement(root, 'PowerSavingTime')
    power_saving_time.text = '600'

    # Track the pins for the LED module and stepper
    led_module_pins = {}
    stepper_pins = {}
    lcd_display_added = False
    encoder_pins = {}

    for line in lines:
        parts = line.split('\t')
        if parts[0] in ["Blank", "5V", "GND"]:
            continue

        name, pin_info, component_type = parts[0], parts[1], parts[2] if len(parts) > 2 else ""
        pin_number = pin_info.split()[2]
        analog_pin_map = {
            '0': '54', '1': '55', '2': '56', '3': '57', '4': '58',
            '5': '59', '6': '60', '7': '61', '8': '62', '9': '63',
            '10': '64', '11': '65', '12': '66', '13': '67', '14': '68', '15': '69'
        }

        # Handle names with underscores
        name_parts = name.split('_')
        base_name = name_parts[0]

        if component_type == 'Button':
            ET.SubElement(root, 'Button', {'Name': name, 'Pin': pin_number})
        elif component_type == 'LED / Output':
            ET.SubElement(root, 'Output', {'Name': name, 'Pin': pin_number})
        elif component_type == 'LED 7-Segment':
            led_module_pins[name_parts[1]] = pin_number
            if all(k in led_module_pins for k in ['DIN', 'CS', 'CLK']):
                ET.SubElement(root, 'LedModule', {
                    'Name': base_name,
                    'ModelType': '0',
                    'DinPin': led_module_pins['DIN'],
                    'ClsPin': led_module_pins['CS'],
                    'ClkPin': led_module_pins['CLK'],
                    'Brightness': '15',
                    'NumModules': '1'
                })
        elif component_type == 'Servo':
            ET.SubElement(root, 'Servo', {'Name': name, 'DataPin': pin_number})
        elif component_type == 'Stepper':
            stepper_pins[name_parts[1]] = pin_number
            if all(k in stepper_pins for k in ['IN1', 'IN2', 'IN3', 'IN4']):
                ET.SubElement(root, 'Stepper', {
                    'Name': base_name,
                    'Pin1': stepper_pins['IN1'],
                    'Pin2': stepper_pins['IN2'],
                    'Pin3': stepper_pins['IN3'],
                    'Pin4': stepper_pins['IN4'],
                    'BtnPin': '0',
                    'Mode': '0',
                    'Backlash': '0',
                    'Deactivate': 'false',
                    'Profile': '0'
                })
        elif component_type == 'LCD Display' and not lcd_display_added:
            ET.SubElement(root, 'LcdDisplay', {
                'Name': base_name,
                'Address': '39',
                'Cols': '16',
                'Lines': '2'
            })
            lcd_display_added = True
        elif component_type == 'Encoder':
            encoder_pins[name_parts[1]] = pin_number
            if all(k in encoder_pins for k in ['A', 'B']):
                ET.SubElement(root, 'Encoder', {
                    'Name': base_name,
                    'PinLeft': encoder_pins['A'],
                    'PinRight': encoder_pins['B'],
                    'EncoderType': '0'
                })
        elif component_type == 'Analog Input':
            ET.SubElement(root, 'AnalogInput', {
                'Name': name,
                'Pin': analog_pin_map[pin_number],
                'Sensitivity': '5'
            })

    xml_str = ET.tostring(root, encoding='utf-8').decode('utf-8')
    return f'<?xml version="1.0" encoding="utf-8"?>\n{xml_str}'

xml_output = create_xml_from_data(spreadsheet_data)
print(xml_output)
