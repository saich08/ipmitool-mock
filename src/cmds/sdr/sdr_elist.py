import random

from models.sdr import SDRV2


class SDRElistMock(object):
    def __init__(self):
        self.ipmi_sdr_readings = []

        self.ipmi_sdr_readings.append(
            SDRV2('System Fan 1', '0Ah', 'ok', '10.1', random.randint(9000, 10000), 'RPM')
        )
        self.ipmi_sdr_readings.append(
            SDRV2('System Fan 2', '0Bh', 'ok', '10.2', random.randint(9000, 10000), 'RPM')
        )

        self.ipmi_sdr_readings.append(
            SDRV2('PS1 Input Power', '01h', 'ok', '11.1', random.randint(100, 120), 'Watts')
        )
        self.ipmi_sdr_readings.append(
            SDRV2('PS2 Input Power', '02h', 'ok', '11.2', random.randint(100, 120), 'Watts')
        )

        self.ipmi_sdr_readings.append(
            SDRV2('PS1 Temperature', '01h', 'ok', '11.1', random.randint(20, 30), 'degrees C')
        )
        self.ipmi_sdr_readings.append(
            SDRV2('PS2 Temperature', '02h', 'ok', '11.2', random.randint(20, 30), 'degrees C')
        )

        self.ipmi_sdr_readings.append(
            SDRV2('PS1 Status', '01h', 'ok', '11.1', 'Presence detected', '')
        )
        self.ipmi_sdr_readings.append(
            SDRV2('PS2 Status', '02h', 'ok', '11.2', 'Presence detected', '')
        )

    def __str__(self):
        return '\n'.join(map(str, self.ipmi_sdr_readings))
