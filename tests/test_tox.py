# Travis configuration tests.
import os
import shutil
import subprocess


# Create direnv configuration when direnv is not installed.
def test_create_tox_configuration():

        # Create travis configuration.
        subprocess.check_call('amanita muscaria -x', env=os.environ.copy(),
                              shell=True)

        assert 'legacy_tox_ini' in open(os.path.join('muscaria',
                                                     'pyproject.toml')).read()
        shutil.rmtree(os.path.join('muscaria'))
