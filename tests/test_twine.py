# Twine configuration tests.
import os
import shutil
import subprocess


# Create twine configuration.
def test_create_twine_configuration():

        subprocess.check_call('amanita muscaria -w', env=os.environ.copy(),
                              shell=True)

        #assert 'legacy_tox_ini' in open(os.path.join('muscaria',
        #                                             'pyproject.toml')).read()
        shutil.rmtree(os.path.join('muscaria'))
