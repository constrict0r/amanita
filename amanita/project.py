# -*- coding: utf-8 -*-

"""Project creation."""
import subprocess


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

    # Construct0r: create the project.
    def __init__(self, destination, direnv=True, venv=True):

        # Create package folder structure.
        try:
            assert subprocess.call('poetry new -- ' +
                                   destination, shell=True) == 0
        except AssertionError:
            print('seringa')

        print('adios')
        # Virtual enviroment.
#        self.venv_setup(destination)

    # Configure virtual enviroment.
    @staticmethod
    def venv_setup(destination):

        print(destination)
