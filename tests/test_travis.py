# Travis configuration tests.
import os
import shutil
import subprocess


# Create direnv configuration when direnv is not installed.
def test_create_travis_configuration():

        # Create travis configuration.
        subprocess.check_call('amanita muscaria -t', env=os.environ.copy(),
                              shell=True)

        assert os.path.isfile(os.path.join('muscaria', '.travis.yml'))
        shutil.rmtree(os.path.join('muscaria'))
