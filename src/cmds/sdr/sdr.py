import random

from models.sdr import SDRV1


class SDRMock(object):
    def __init__(self):
        self.ipmi_sdr_readings = []

        self.ipmi_sdr_readings.append(
            SDRV1('System Fan 1', random.randint(9000, 10000), 'RPM', 'ok')
        )
        self.ipmi_sdr_readings.append(
            SDRV1('System Fan 2', random.randint(9000, 10000), 'RPM', 'ok')
        )

        self.ipmi_sdr_readings.append(
            SDRV1('PS1 Input Power', random.randint(100, 120), 'Watts', 'ok')
        )
        self.ipmi_sdr_readings.append(
            SDRV1('PS2 Input Power', random.randint(100, 120), 'Watts', 'ok')
        )

        self.ipmi_sdr_readings.append(
            SDRV1('PS1 Temperature', random.randint(20, 30), 'degrees C', 'ok')
        )
        self.ipmi_sdr_readings.append(
            SDRV1('PS2 Temperature', random.randint(20, 30), 'degrees C', 'ok')
        )

        self.ipmi_sdr_readings.append(
            SDRV1('PS1 Status', '0x00', '', 'ok')
        )
        self.ipmi_sdr_readings.append(
            SDRV1('PS2 Status', '0x00', '', 'ok')
        )

    def __str__(self):
        return '\n'.join(map(str, self.ipmi_sdr_readings))
