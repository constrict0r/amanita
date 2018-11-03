# Amanita tests.import subprocess
import subprocess
import os
from amanita import amanita


# Enjoy.
def test_enjoy(capfd):

    print(amanita.enjoy())
    out, err = capfd.readouterr()
    assert "___.....___" in out


# Console script without arguments.
def test_console_no_args():

    subprocess.check_call(['amanita'], env=os.environ.copy(),  shell=True)


# Console script with arguments.
def test_console_args():

    subprocess.check_call(['amanita --version'],
                          env=os.environ.copy(),
                          shell=True)
