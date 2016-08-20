# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

import argparse
import sys
import click
from commands.sample import sample as cmd_sample

class {{ cookiecutter.project_slug|capitalize }}(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
        description='{{ cookiecutter.project_name }}',
        usage='''{{ cookiecutter.python_cmd }} <command> [<args>]
        
The most commonly used git commands are:
    sample     A simple sample command to override
        ''')
        epilogue='''Credits :
        
author: {{ cookiecutter.full_name }}
version: {{ cookiecutter.version }}
        '''.format(__version__)
        parser.add_argument('command', help='Sub command to run')
        parser.add_argument('--version', help='Print version', action='version', version='{{ cookiecutter.project_name }} {version}'.format(version=__version__))
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            click.echo('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()
        
    def sample(self):
        cmd_sample()

def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    click.echo("@@ {{ cookiecutter.project_name }} @@")
    if '{{ cookiecutter.cli_tool }}' == "y":
        {{ cookiecutter.project_slug|capitalize }}()
    elif '{{ cookiecutter.cli_tool }}' == "n":
        click.echo('Play with me')


if __name__ == "__main__":
    main()
