# Project tests.
import os
import pytest
import subprocess
import shutil

from amanita import project


# Create project.
def test_create_project():

    if os.path.isdir('muscaria'):
        shutil.rmtree(os.path.join('muscaria'))

    subprocess.check_call('amanita muscaria',
                          env=os.environ.copy(),
                          shell=True)
    shutil.rmtree(os.path.join('muscaria'))


# Create project with existing directory.
def test_create_project_existing_directory():
    os.mkdir('muscaria')
    subprocess.check_call('amanita muscaria',
                          env=os.environ.copy(),
                          shell=True)
    shutil.rmtree(os.path.join('muscaria'))


# Create project with existing non-empty directory.
@pytest.mark.xfail
def test_create_project_existing_directory_non_empty():
    subprocess.check_call('amanita amanita',
                          env=os.environ.copy(),
                          shell=True)


# Create project with non permission.
@pytest.mark.xfail
def test_create_project_forbidden():
    subprocess.check_call('amanita /root',
                          env=os.environ.copy(),
                          shell=True)


# Create virtual enviroment.
def test_create_venv():

    project.Project.venv_setup(os.path.join(''))
    assert os.path.isdir('.venv')
    shutil.rmtree(os.path.join('.venv'))


# Create virtual enviroment with nonexisting path.
@pytest.mark.xfail
def test_create_venv_nonexistent():

    project.Project.venv_setup('/dev/null')


# Create virtual enviroment with non permission.
@pytest.mark.xfail
def test_create_venv_forbidden():

    project.Project.venv_setup('/root')


# Overwrite virtual enviroment.
def test_overwrite_venv():

    project.Project.venv_setup(os.path.join(''))
    project.Project.venv_setup(os.path.join(''))
    assert os.path.isdir('.venv')
    shutil.rmtree(os.path.join('.venv'))


# Create project with virtual enviroment.
def test_create_project_venv():

    subprocess.check_call('amanita muscaria -v',
                          env=os.environ.copy(),
                          shell=True)
    assert os.path.isdir('muscaria/.venv')
    shutil.rmtree(os.path.join('muscaria'))


# Create project with virtual enviroment outside the project directory.
def test_create_project_venv_out():

    subprocess.check_call('amanita muscaria -e venv',
                          env=os.environ.copy(),
                          shell=True)
    assert os.path.isdir('venv')
    shutil.rmtree(os.path.join('muscaria'))
    shutil.rmtree(os.path.join('venv'))


# Create project with virtual enviroment outside the project.
# with nonexisting path.
@pytest.mark.xfail
def test_create_project_venv_out_nonexistent():

    subprocess.check_call('amanita muscaria -e /dev/null',
                          env=os.environ.copy(),
                          shell=True)


# Create project with virtual enviroment outside the project.
# with non permission.
@pytest.mark.xfail
def test_create_project_venv_out_forbidden():

    shutil.rmtree(os.path.join('muscaria'))
    subprocess.check_call('amanita muscaria -e /root',
                          env=os.environ.copy(),
                          shell=True)


# Create project with virtual enviroment inside and
# outside the project directory.
def test_create_project_venv_in_out():

    shutil.rmtree(os.path.join('muscaria'))
    subprocess.check_call('amanita muscaria -v -e venv',
                          env=os.environ.copy(),
                          shell=True)
    assert os.path.isdir('muscaria/.venv')
    assert os.path.isdir('venv')
    shutil.rmtree(os.path.join('muscaria'))
    shutil.rmtree(os.path.join('venv'))
