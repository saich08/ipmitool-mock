import click

from cmds.sdr import SDRMock, SDRElistMock
from cmds.sensor import SensorMock
from cmds.sel import SELMock


@click.group()
@click.option('-U', '--username', help='')
@click.option('-P', '--password', help='')
def main(username, password):
    pass


@main.group('sdr', invoke_without_command=True, help='Print Sensor Data Repository entries and readings')
@click.pass_context
def sdr(ctx):
    if ctx.invoked_subcommand is None:
        sdr_mock = SDRMock()
        print(sdr_mock)


@sdr.command('elist', help='')
def sdr_elist():
    sdr_elist_mock = SDRElistMock()
    print(sdr_elist_mock)


@main.group('sensor', invoke_without_command=True, help='Print detailed sensor information')
def sensor():
    sensor_mock = SensorMock()
    print(sensor_mock)


@main.group('sel', invoke_without_command=True, help='Print System Event Log (SEL)')
def sensor():
    sel_mock = SELMock()
    print(sel_mock)


if __name__ == '__main__':
    main()
