"""Console script for bertosaurus."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for bertosaurus."""
    click.echo("Replace this message by putting your code into "
               "bertosaurus.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
