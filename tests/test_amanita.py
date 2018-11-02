# Amanita tests.
import subprocess
import os
from amanita import amanita


def test_enjoy(capfd):

    amanita.enjoy()
    out, err = capfd.readouterr()
    assert "___.....___" in out


def test_console_amanita():

    subprocess.check_call(["amanita"], env=os.environ.copy(), shell=True)
