# -*- coding: utf-8 -*-

"""Creates customizable projects"""
import os
import pathlib
import shutil
import sys
import subprocess

import click
import amanita


class Project:
    """Create customizable python projects."""

    # Project directories.
    ROOT_DIR = pathlib.Path(__file__).parents[1]
    RESOURCES_DIR = os.path.join(str(ROOT_DIR), 'resources')

    # Create the project.
    @staticmethod
    def create(path, direnv=False, tox=False, travis=False,
               twine=False, venv=False, venv_path=None, venv_only=False):
        """Create customizable python projects.

        Each project includes a package directory layout and optionally:

        - A virtual enviroment inside or outside the project.

        - `Direnv <https://direnv.net>`_ configuration.

        - `tox <https://tox.readthedocs.io/en/latest>`_ configuration.

        - `travis <https://travis-ci.org>`_ configuration.

        - `twine <https://pypi.org/project/twine>`_ configuration.

        Args:
            path (str): Path where to create the project.
            direnv (bool): Configure direnv.
            tox (bool): Add tox configuration.
            travis (bool): Create travis ci configuration.
            twine (bool): Create twine configuration.
            venv (bool): Create a virtual enviroment inside the project folder.
            venv_path (str): Create a virtual enviroment on the given path.
            venv_only (bool): Only create a virtual enviroment on PATH.

        Returns:
            bool: True for success, False otherwise.
        """

        if venv_only:
            # Only create a virtual enviroment.
            amanita.project.Project.venv_setup(path)

        else:
            # Create package folder structure.
            try:
                assert subprocess.call('poetry new -- ' +
                                       path, shell=True) == 0

            except AssertionError:
                click.echo(click.style('An error occured creating the ' +
                                       'project.', fg='red'))
                sys.exit(1)

            # Create virtual enviroment outside.
            if venv_path is not None:
                amanita.project.Project.venv_setup(venv_path)

            # Create virtual enviroment inside.
            elif venv is True:
                amanita.project.Project.venv_setup(path)
                venv_path = path

            # Create direnv configuration.
            if direnv and venv_path is not None:
                amanita.project.Project.direnv_setup(path, venv_path)

            # Create tox configuration.
            if tox:
                amanita.project.Project.tox_setup(path)

            # Create travis configuration.
            if travis:
                amanita.project.Project.travis_setup(path)

            # Create twine configuration.
            if twine:
                amanita.project.Project.twine_setup(path)

        return True

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

        try:
            if os.path.isdir(os.path.join(path, '.venv')):
                assert not os.listdir(os.path.join(path, '.venv'))

        except AssertionError:
            click.echo(
                click.style('An error occurred creating ', fg='red') +
                click.style('the virtual enviroment:\n', fg='green') +
                click.style('Destination ', fg='red') +
                click.style(os.path.abspath(os.path.join(path, '.venv')),
                            fg='yellow') +
                click.style(' exists and is not empty.', fg='red'))
            sys.exit(1)

        try:
            Env.build_venv(os.path.join(path, '.venv'))

            click.echo('Created virtualenv ' + click.style('.venv',
                       fg='green') + ' in ' + click.style(path, fg='blue'))

        except PermissionError:
            click.echo(click.style('Error creating the ', fg='red') +
                       click.style('virtual enviroment: ', fg='green') +
                       click.style('Permission denied writing to ', fg='red') +
                       click.style(path, fg='yellow'))
            sys.exit(1)

        except NotADirectoryError:
            click.echo(click.style('Error creating the virtual enviroment: ',
                                   fg='red') +
                       click.style(path, fg='yellow') +
                       click.style(' is not a directory', fg='red'))
            sys.exit(1)

        return True

    # Create direnv configuration.
    @staticmethod
    def direnv_setup(path, venv_path):
        """Creates direnv configuration on the given path.

        This function creates the configuration even if
        direnv is not installed, but returns false if it is not installed.

        Args:
            path (str): Path where to create the direnv configuration.
            venv_path (str): Path to an existing virtual enviroment.

        Returns:
            bool: True for success, False if direnv is not installed.
        """

        if sys.platform == "linux" or sys.platform == "linux2":

            if '.venv' not in venv_path:
                venv_path = os.path.join(venv_path, '.venv')

            # Create direnv configuration.
            direnv_file = open(os.path.join(path, '.envrc'), 'w+')
            direnv_file.write('source ' + os.path.abspath(venv_path) +
                              '/bin/activate')
            direnv_file.close()

            click.echo('Created direnv configuration ' +
                       click.style('.envrc', fg='green') + ' in ' +
                       click.style(path, fg='blue'))

            # Configure ~/.bashrc if not already configured for direnv.
            home = str(pathlib.Path.home())
            bashrc = open(os.path.join(home, '.bashrc'), 'r')
            bashrc_lines = bashrc.readlines()
            bashrc.close()

            found = False
            for line in bashrc_lines:
                if 'direnv' in line:
                    found = True

            if not found:
                bashrc = open(os.path.join(home, '.bashrc'), 'a')
                bashrc.write('eval "$(direnv hook bash)"')
                bashrc.close()

                click.echo('Added direnv configuration to ' +
                           click.style('~/.bashrc', fg='green'))

                click.echo('You must run: ' +
                           click.style('source ~/.bashrc ', fg='yellow') +
                           'or ' +
                           click.style('restart session ', fg='green') +
                           'to activate it')

            try:
                assert subprocess.call('dpkg-query -l direnv',
                                       stdout=open(os.devnull, 'wb'),
                                       shell=True) == 0

                subprocess.call('direnv allow ' + path, shell=True)

            except AssertionError:
                click.echo(click.style('Warning: Direnv not installed. ',
                                       fg='yellow'))
                click.echo(click.style('The .envrc file was created ',
                                       fg='green') +
                           click.style('but it will not work until ',
                                       fg='red') +
                           click.style('direnv is installed: ', fg='red') +
                           click.style('sudo apt install direnv -y',
                                       fg='blue'))
                return False

        return True

    # Get plain path to directory where pyproject.toml resides.
    def get_plain_path(path):
        """Ensures path does not contains pyproject.toml in it.

        Args:
            path (str): Path where pyproject.toml resides.

        Returns:
            string: Plain path to directory where pyproject.toml resides.
        """
        # Remove pyproject.toml if is part of path.
        if 'pyproject.toml' in str(path):
            return path.replace('pyproject.toml', '')

        return path

    # Add dependecy to pyproject.toml.
    def add_dependency(path, dependency):
        """Adds a python dependency to pyproject.toml

        Args:
            project_path (str): Path where pyproject.toml resides.
            dependency (str): Dependency name.

        Returns:
            bool: True for success, False otherwise.
        """
        original_path = os.getcwd()
        plain_path = amanita.project.Project.get_plain_path(path)
        os.chdir(plain_path)

        try:
            assert subprocess.call('poetry add ' + dependency,
                                   env=os.environ.copy(), shell=True) == 0

        except AssertionError:
            click.echo('An error occured adding ' +
                       click.style(dependency + ' dependency', fg='red') +
                       ' to ' +
                       click.style(os.path.join(plain_path, 'pyproject.toml'),
                                   fg='blue'))
            sys.exit(1)

        click.echo('Added ' + click.style(dependency + ' dependecy',
                                          fg='green') +
                   ' to ' + click.style(os.path.join(plain_path,
                                                     'pyproject.toml'),
                                        fg='blue'))
        os.chdir(original_path)
        return True

    # Create tox configuration.
    @staticmethod
    def tox_setup(path):
        """Creates tox configuration on the project path.

        Args:
            path (str): Path where pyproject.toml resides.

        Returns:
            bool: True for success, False otherwise.
        """
        # Add tox dependency to pyproject.yml.
        plain_path = amanita.project.Project.get_plain_path(path)
        amanita.project.Project.add_dependency(plain_path, 'tox')

        # Add tox configuration to pyproject.yml.
        import fileinput

        resources_dir = amanita.project.Project.RESOURCES_DIR
        with open(os.path.join(plain_path, 'pyproject.toml'),
                  'a') as fout, fileinput.input(os.path.join
                                                (resources_dir,
                                                 'tox-template.toml')) as fin:
            for line in fin:
                fout.write(line)

        click.echo('Added ' + click.style('tox configuration', fg='green') +
                   ' to ' + click.style(os.path.join(plain_path,
                                                     'pyproject.toml'),
                                        fg='blue'))
        return True

    # Create travis configuration.
    @staticmethod
    def travis_setup(path):
        """Creates travis configuration on the project path.

        Args:
            path (str): Path where to create the travis configuration.

        Returns:
            bool: True for success, False otherwise.
        """
        shutil.copyfile(os.path.join(amanita.project.Project.RESOURCES_DIR,
                                     'travis-template.yml'),
                        os.path.join(path, '.travis.yml'))

        click.echo('Created travis configuration ' + click.style('.travis.yml',
                                                                 fg='green') +
                   ' in ' + click.style(path, fg='blue'))
        return True

    # Create twine configuration.
    @staticmethod
    def twine_setup(path):
        """Setups twine configuration on the project path.

        This function adds twine dependency to pyproject.toml and
        add text on README.md about twine usage.

        Args:
            path (str): Path where pyproject.toml resides.

        Returns:
            bool: True for success, False otherwise.
        """
        # Add twine dependency to pyproject.yml.
        plain_path = amanita.project.Project.get_plain_path(path)
        amanita.project.Project.add_dependency(plain_path, 'twine')
