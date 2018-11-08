# -*- coding: utf-8 -*-

"""Main amanita CLI."""

import os
import sys

import click

from amanita import __version__
from amanita import project


def version_msg():
    """Return the amanita version, location and Python powering it."""
    python_version = sys.version[:3]
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = u'amanita %(version)s from {} (Python {})'
    return message.format(location, python_version)


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.version_option(__version__, u'-V', u'--version', message=version_msg())
@click.argument('destination', required=True)
@click.option(
     u'-d', u'--direnv', is_flag=True,
     help=u'Install and configure direnv console enviroment switcher.')
@click.option(
     u'-e', '--venv', is_flag=True,
     help=u'Create and configure a virtual enviroment.')
# TODO: add --dry-run
def main(destination, direnv, venv):
    """Creates a customizable python project"""

    project.Project(destination, direnv, venv)
