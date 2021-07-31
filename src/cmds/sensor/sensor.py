import random

from models.sensor import Sensor


class SensorMock(object):
    def __init__(self):
        self.ipmi_sensor_readings = []

        self.ipmi_sensor_readings.append(
            Sensor('System Fan 1', random.randint(9000, 10000), 'RPM', 'ok', 300, 500, 700, 25300, 25400, 25500)
        )
        self.ipmi_sensor_readings.append(
            Sensor('System Fan 2', random.randint(9000, 10000), 'RPM', 'ok', 300, 500, 700, 25300, 25400, 25500)
        )

        self.ipmi_sensor_readings.append(
            Sensor('PS1 Input Power', random.randint(100, 120), 'Watts', 'ok', 0, 0, 0, 1700, 1800, 2200)
        )
        self.ipmi_sensor_readings.append(
            Sensor('PS2 Input Power', random.randint(100, 120), 'Watts', 'ok', 0, 0, 0, 1700, 1800, 2200)
        )

        self.ipmi_sensor_readings.append(
            Sensor('PS1 Temperature', random.randint(20, 30), 'degrees C', 'ok', 0, 5, 16, 53, 60, 65)
        )
        self.ipmi_sensor_readings.append(
            Sensor('PS2 Temperature', random.randint(20, 30), 'degrees C', 'ok', 0, 5, 16, 53, 60, 65)
        )

        self.ipmi_sensor_readings.append(
            Sensor('PS1 Status', '0x1', 'discrete', '0x0100')
        )
        self.ipmi_sensor_readings.append(
            Sensor('PS2 Status', '0x1', 'discrete', '0x0100')
        )

    def __str__(self):
        return '\n'.join(map(str, self.ipmi_sensor_readings))
