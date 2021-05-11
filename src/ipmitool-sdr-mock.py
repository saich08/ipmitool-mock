import click

from sdr.sdr import SDRMock
from sdr.sdr_elist import SDREListMock


@click.group()
def main():
    pass


@main.group('sdr', invoke_without_command=True, help='sdr help')
@click.pass_context
def sdr(ctx):
    if ctx.invoked_subcommand is None:
        sdr_mock = SDRMock()
        sdr_mock_result = str(sdr_mock)

        print(sdr_mock_result)


@sdr.command('elist', help='sdr elist help')
def sdr_elist():
    sdr_elist_mock = SDREListMock()
    sdr_elist_mock_result = str(sdr_elist_mock)

    print(sdr_elist_mock_result)


if __name__ == '__main__':
    main()
