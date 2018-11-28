# Project tests.
import os
import pytest
import subprocess

from amanita import project


# Create direnv configuration when direnv is not installed.
def test_create_direnv_configuration_direnv_not_installed():

        # Uninstall direnv.
        subprocess.call('sudo apt-get remove direnv -y',
                        shell=True)

        result = project.Project.direnv_setup('', '')
        assert result is False

        assert os.path.isfile('.envrc')
        os.remove('.envrc')


# Create direnv configuration when direnv is installed.
@pytest.mark.skip
def test_create_direnv_configuration_direnv_installed():

        # Uninstall direnv.
        subprocess.call('sudo apt-get install direnv -y',
                        shell=True)

        result = project.Project.direnv_setup('', '')
        assert result is True

        assert os.path.isfile('.envrc')
        os.remove('.envrc')
