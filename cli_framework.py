# import click

# @click.command()
# def cli-framework():
#     print("Hello World!")

import argparse

class CLI:
    def __init__(self, prog_name):
        self.parser = argparse.ArgumentParser(prog=prog_name)
        self.args = None

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def run(self):
        self.args = self.parser.parse_args()
        # Add your unique code here


if __name__ == '__main__':
    cli = CLI(prog_name='my_program')
    cli.add_argument('--foo', help='foo help message')
    cli.add_argument('--bar', help='bar help message')
    cli.run()