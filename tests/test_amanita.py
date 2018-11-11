# Amanita tests.
import os
import subprocess
import pytest

from amanita import amanita


# Enjoy.
def test_enjoy(capfd):

    print(amanita.enjoy())
    out, err = capfd.readouterr()
    assert "___.....___" in out


# Console script without arguments.
@pytest.mark.xfail
def test_console_no_args():

    subprocess.check_call('amanita', env=os.environ.copy(), shell=True)


# Console script with arguments.
def test_console_args(capfd):

    console_output = subprocess.check_output('amanita --version',
                                             env=os.environ.copy(),
                                             shell=True)
    print(console_output)
    out, err = capfd.readouterr()
    assert 'amanita' in out


