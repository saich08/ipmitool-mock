import click

from cmds.sdr import SDRMock, SDRElistMock
from cmds.sensor import SensorMock


@click.group()
def main():
    pass


@main.group('sdr', invoke_without_command=True, help='sdr help')
@click.pass_context
def sdr(ctx):
    if ctx.invoked_subcommand is None:
        sdr_mock = SDRMock()
        print(sdr_mock)


@sdr.command('elist', help='sdr elist help')
def sdr_elist():
    sdr_elist_mock = SDRElistMock()
    print(sdr_elist_mock)


@main.group('sensor', invoke_without_command=True, help='sensor help')
def sensor():
    sensor_mock = SensorMock()
    print(sensor_mock)


if __name__ == '__main__':
    main()
