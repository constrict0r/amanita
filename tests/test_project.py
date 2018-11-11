# Project tests.
import os
import pytest
import subprocess
import shutil


from amanita import project


# Create project.
def test_create_project():

    subprocess.check_call('amanita muscaria',
                          env=os.environ.copy(),
                          shell=True)
    shutil.rmtree(os.path.join('muscaria'))


# Create virtual enviroment.
def test_create_venv():

    project.Project.venv_setup(os.path.join(''))
    if not os.path.exists('.venv'):
        return False
    shutil.rmtree(os.path.join('.venv'))


# Create virtual enviroment with non existing path
@pytest.mark.xfail
def test_create_venv_nonexist():

    project.Project.venv_setup('/dev/null')


# Create virtual enviroment with non permission
@pytest.mark.xfail
def test_create_venv_forbidden():

    project.Project.venv_setup('/root')


# Overwrite virtual enviroment.
def test_overwrite_venv():

    project.Project.venv_setup(os.path.join(''))
    project.Project.venv_setup(os.path.join(''))
    if not os.path.exists('.venv'):
        return False
    shutil.rmtree(os.path.join('.venv'))


# Create project with virtual enviroment.
def test_create_project_venv():

    subprocess.check_call('amanita muscaria -e',
                          env=os.environ.copy(),
                          shell=True)
    if not os.path.exists('muscaria/.venv'):
        return False
    shutil.rmtree(os.path.join('muscaria'))
