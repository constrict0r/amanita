# Amanita tests.
import subprocess
import os
from amanita import amanita


# Enjoy.
def test_enjoy(capfd):

    amanita.enjoy()
    out, err = capfd.readouterr()
    assert "___.....___" in out


# Console script without parameters.
def test_console_no_args():

    subprocess.check_call(['amanita'], env=os.environ.copy(),  shell=True)


# Console script with parameters.
def test_console_args():

    subprocess.check_call(['amanita', 'a'], env=os.environ.copy(),  shell=True)
