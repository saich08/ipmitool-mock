
class SEL(object):
    def __init__(self, sel_id, date, time, sensor, message, state):
        self.sel_id = sel_id
        self.date = date
        self.time = time
        self.sensor = sensor
        self.message = message
        self.state = state

    def __str__(self):
        sel_id = str(self.sel_id)
        date = str(self.date)
        time = str(self.time)
        sensor = str(self.sensor)
        message = str(self.message)
        state = str(self.state)

        return f'{sel_id.ljust(5)}| {date.ljust(11)}| {time.ljust(9)}| {sensor.ljust(9)} | {message}  | {state}'
