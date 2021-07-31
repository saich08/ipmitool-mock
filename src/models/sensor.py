
class Sensor(object):
    def __init__(self, name, value, unit, status, lower_non_recoverable=None, lower_critical=None,
                 lower_non_critical=None, upper_non_critical=None, upper_critical=None, upper_non_recoverable=None):
        self.name = name
        self.value = value
        self.unit = unit
        self.status = status

        self.lower_non_recoverable = lower_non_recoverable
        self.lower_critical = lower_critical
        self.lower_non_critical = lower_non_critical

        self.upper_non_critical = upper_non_critical
        self.upper_critical = upper_critical
        self.upper_non_recoverable = upper_non_recoverable

    def __str__(self):
        name = str(self.name)
        value = str(self.value)
        unit = str(self.unit)
        status = str(self.status)

        lower_non_recoverable = "{:.3f}".format(self.lower_non_recoverable) if self.lower_non_recoverable else 'na'
        lower_critical = "{:.3f}".format(self.lower_critical) if self.lower_critical else 'na'
        lower_non_critical = "{:.3f}".format(self.lower_non_critical) if self.lower_non_critical else 'na'

        upper_non_critical = "{:.3f}".format(self.upper_non_critical) if self.upper_non_critical else 'na'
        upper_critical = "{:.3f}".format(self.upper_critical) if self.upper_critical else 'na'
        upper_non_recoverable = "{:.3f}".format(self.upper_non_recoverable) if self.upper_non_recoverable else 'na'

        return f'{name.ljust(17)}| {value.ljust(11)}| {unit.ljust(11)}| {status.ljust(6)}| ' \
               f'{lower_non_recoverable.ljust(10)}| {lower_critical.ljust(10)}| {lower_non_critical.ljust(10)}| ' \
               f'{upper_non_critical.ljust(10)}| {upper_critical.ljust(10)}| {upper_non_recoverable}'
