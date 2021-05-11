import random


class IPMISensorV1(object):
    def __init__(self, name, value, unit, status):
        self.name = name
        self.value = value
        self.unit = unit
        self.status = status

    def __str__(self):
        reading = f'{self.value} {self.unit}'
        report = f'{self.name.ljust(17)}| {reading.ljust(18)}| {self.status}'

        return report


class SDRMock(object):
    def __init__(self):
        self.ipmi_sensors_readings = []

        # generate mock sensor readings
        self.ipmi_sensors_readings.append(
            IPMISensorV1('System Fan 1', random.randint(9000, 10000), 'RPM', 'ok')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV1('System Fan 2', random.randint(9000, 10000), 'RPM', 'ok')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV1('System Fan 3', random.randint(9000, 10000), 'RPM', 'ok')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV1('System Fan 4', random.randint(9000, 10000), 'RPM', 'ok')
        )

        self.ipmi_sensors_readings.append(
            IPMISensorV1('PS1 Input Power', random.randint(100, 120), 'Watts', 'ok')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV1('PS2 Input Power', random.randint(100, 120), 'Watts', 'ok')
        )

        self.ipmi_sensors_readings.append(
            IPMISensorV1('PS1 Temperature', random.randint(20, 30), 'degrees C', 'ok')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV1('PS2 Temperature', random.randint(20, 30), 'degrees C', 'ok')
        )

        self.ipmi_sensors_readings.append(IPMISensorV1('PS1 Status', '0x00', '', 'ok'))
        self.ipmi_sensors_readings.append(IPMISensorV1('PS2 Status', '0x00', '', 'ok'))

    def __str__(self):
        return '\n'.join(map(str, self.ipmi_sensors_readings))
