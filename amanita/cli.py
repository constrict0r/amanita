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
@click.argument('path', required=True)
@click.option(
     u'-d', u'--direnv', is_flag=True, default=False,
     help=u'Configure direnv console enviroment switcher.')
@click.option(
    u'-t', '--travis', is_flag=True, default=False,
    help=u'Create travis ci configuration.')
@click.option(
     u'-v', '--venv', is_flag=True, default=False,
     help=u'Create and configure a virtual enviroment inside the project.')
@click.option(
     u'-e', '--venv-path', default=None,
     help=u'Create and configure a virtual enviroment on the given path.')
@click.option(
    u'--venv-only', is_flag=True, default=False,
    help=u'Only create a virtual enviroment on PATH.')
@click.option(
    u'-x', '--tox', is_flag=True, default=False,
    help=u'Add tox configuration.')
def main(path, direnv, tox, travis, venv, venv_path, venv_only):
    """Creates a customizable python project

    Package main entry point.
    """

    project.Project.create(path, direnv, tox, travis, venv, venv_path,
                           venv_only)
