# -*- coding: utf-8 -*-

"""Creates customizable projects"""
import os
import sys
import subprocess

import click
import amanita


class Project:
    """Create customizable python projects."""

    # Create the project.
    @staticmethod
    def create(path, direnv=False, venv=False, venv_path=None):
        """Create customizable python projects.

       Each project includes a package directory layout and optionally:

       - A virtual enviroment inside or outside the project folder.
       - `Direnv <https://direnv.net>`_ console switcher configuration (linux).

       Args:
           path (str): Path where to create the project.
           direnv (bool): Configure direnv.
           venv (bool): Create a virtual enviroment inside the project folder.
           venv_path (str): Create a virtual enviroment on the given path.
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
            amanita.project.Project.venv_setup(path)

        if venv_path is not None:
            amanita.project.Project.venv_setup(venv_path)

    # Create virtual enviroment.
    @staticmethod
    def venv_setup(path):
        """Creates a virtual enviroment on a given path.

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
