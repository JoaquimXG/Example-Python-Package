import click

from sample_package.one import one
from sample_package.sub_package import three

@click.command()
def main():
    print("This is main")
    one()
    three()

exit(main())