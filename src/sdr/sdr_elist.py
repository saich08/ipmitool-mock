import random


class IPMISensorV2(object):
    def __init__(self, name, sensor_number, status, entity_id, value, unit):
        self.name = name
        self.sensor_number = sensor_number
        self.status = status
        self.entity_id = entity_id
        self.value = value
        self.unit = unit

    def __str__(self):
        reading = f'{self.value} {self.unit}'
        report = f'{self.name.ljust(17)}| {self.sensor_number} | ' \
                 f'{self.status} |{self.entity_id.rjust(5)} | {reading}'

        return report


class SDREListMock(object):
    def __init__(self):
        self.ipmi_sensors_readings = []

        # generate mock sensor readings
        self.ipmi_sensors_readings.append(
            IPMISensorV2('System Fan 1', '0Ah', 'ok', '10.1', random.randint(9000, 10000), 'RPM')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV2('System Fan 2', '0Bh', 'ok', '10.2', random.randint(9000, 10000), 'RPM')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV2('System Fan 3', '0Ch', 'ok', '10.3', random.randint(9000, 10000), 'RPM')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV2('System Fan 4', '0Dh', 'ok', '10.4', random.randint(9000, 10000), 'RPM')
        )

        self.ipmi_sensors_readings.append(
            IPMISensorV2('PS1 Input Power', '01h', 'ok', '11.1', random.randint(100, 120),
                         'Watts')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV2('PS2 Input Power', '02h', 'ok', '11.2', random.randint(100, 120),
                         'Watts')
        )

        self.ipmi_sensors_readings.append(
            IPMISensorV2('PS1 Temperature', '01h', 'ok', '11.1', random.randint(20, 30),
                         'degrees C')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV2('PS2 Temperature', '02h', 'ok', '11.2', random.randint(20, 30),
                         'degrees C')
        )

        self.ipmi_sensors_readings.append(
            IPMISensorV2('PS1 Status', '01h', 'ok', '11.1', 'Presence detected', '')
        )
        self.ipmi_sensors_readings.append(
            IPMISensorV2('PS2 Status', '02h', 'ok', '11.2', 'Presence detected', '')
        )

    def __str__(self):
        return '\n'.join(map(str, self.ipmi_sensors_readings))
