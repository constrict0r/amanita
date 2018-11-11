# -*- coding: utf-8 -*-

"""Project creation."""
import os
import sys
import subprocess

import click


class Project:
    """Template to create python projects"""

    # Variables for customizing the project.
    direnv = False
    emacs = False
    pypi = False
    repository = False
    sphinx = False
    tox = False
    travis = False
    venv = False
    web = False

    # Create the project.
    def __init__(self, destination, direnv=False, venv=False):

        # Create package folder structure.
        try:
            assert subprocess.call('poetry new -- ' +
                                   destination, shell=True) == 0

        except AssertionError:
            click.echo(click.style('An error occured creating the project',
                                   fg='red'))
            sys.exit(1)

        # Create virtual enviroment.
        if venv is True:
            self.venv_setup(destination)

    # Create virtual enviroment.
    @staticmethod
    def venv_setup(path):

        from poetry.utils.env import Env

        # TODO: test this:
        # path = '/dev/null'

        # This will overwrite an existing virtual enviroment.
        try:
            Env.build_venv(os.path.join(path, ".venv"))

            click.echo('Created virtualenv ' + click.style('.venv',
                       fg='green') + ' in ' + click.style(path, fg='blue'))

        except PermissionError:
            click.echo(click.style('Error creating the virtual enviroment: ',
                                   fg='red') +
                       click.style('Permission denied writing to ', fg='red') +
                       click.style(path, fg='green'))
            sys.exit(1)

        except NotADirectoryError:
            click.echo(click.style('Error creating the virtual enviroment: ',
                                   fg='red') +
                       click.style(path, fg='cyan') +
                       click.style(' is not a directory', fg='red'))
            sys.exit(1)
