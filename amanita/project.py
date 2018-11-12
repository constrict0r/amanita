# -*- coding: utf-8 -*-

"""Creates customizable projects"""
import os
import sys
import subprocess

import click


class Project:
    """Create python projects from simple package to web application."""

    # Create the project.
    def __init__(self, path, direnv=False, venv=False, venv_path=''):
        """Create a customizable project.

        Creates a python project with basic package directory layout
        and optionally:
         - A virtual enviroment inside or outside the project directory.

        Args:
            path (str): Path where to create the project.
            direnv: Configure direnv?
            venv: Create a virtual enviroment?
        """

        # Create package folder structure.
        try:
            assert subprocess.call('poetry new -- ' +
                                   path, shell=True) == 0

        except AssertionError:
            click.echo(click.style('An error occured creating the project',
                                   fg='red'))
            sys.exit(1)

        # Create virtual enviroment.
        if venv is True:
            self.venv_setup(path)
        elif venv_path is not None:
            self.venv_setup(venv_path)

    # Create virtual enviroment.
    @staticmethod
    def venv_setup(path):
        """Create a virtual enviroment.

        Creates a virtual enviroment on a given path.

        Args:
            path (str): Path where to create the virtual enviroment.

        Returns:
            bool: True for success, False otherwise.
        """
        from poetry.utils.env import Env

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

        return True
