
class SDRV1(object):
    def __init__(self, name, value, unit, status):
        self.name = name
        self.value = value
        self.unit = unit
        self.status = status

    def __str__(self):
        name = str(self.name)
        reading = f'{self.value} {self.unit}'
        status = str(self.status)

        return f'{name.ljust(17)}| {reading.ljust(18)}| {status}'


class SDRV2(object):
    def __init__(self, name, sensor_number, status, entity_id, value, unit):
        self.name = name
        self.sensor_number = sensor_number
        self.status = status
        self.entity_id = entity_id
        self.value = value
        self.unit = unit

    def __str__(self):
        name = str(self.name)
        sensor_number = str(self.sensor_number)
        status = str(self.status)
        entity_id = str(self.entity_id)
        reading = f'{self.value} {self.unit}'

        return f'{name.ljust(17)}| {sensor_number.ljust(4)}| {status.ljust(3)}|{entity_id.rjust(5)} | {reading}'
