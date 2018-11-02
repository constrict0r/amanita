# Amanita tests.

from amanita import amanita


def test_enjoy(capfd):

    print('hello')
    print('bye')
    amanita.enjoy()
    out, err = capfd.readouterr()
    assert "___.....___" in out
