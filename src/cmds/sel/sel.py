from datetime import datetime

from models.sel import SEL


class SELMock(object):
    def __init__(self):
        self.ipmi_sel_readings = []

        today = datetime.now()

        self.ipmi_sel_readings.append(
            SEL(1, today.strftime('%m/%d/%Y'), today.strftime('%H:%M:%S'), 'Fan #0x96', 'Lower Critical going low',
                'Asserted')
        )
        self.ipmi_sel_readings.append(
            SEL(2, today.strftime('%m/%d/%Y'), today.strftime('%H:%M:%S'), 'Fan #0x96',
                'Lower Non-recoverable going low', 'Asserted')
        )
        self.ipmi_sel_readings.append(
            SEL(3, today.strftime('%m/%d/%Y'), today.strftime('%H:%M:%S'), 'Fan #0x96',
                'Lower Non-recoverable going low', 'Deasserted')
        )

    def __str__(self):
        return '\n'.join(map(str, self.ipmi_sel_readings))
