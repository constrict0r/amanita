# Travis configuration tests.
import os
import shutil
import subprocess


# Create travis configuration.
def test_create_travis_configuration():

        subprocess.check_call('amanita muscaria -t', env=os.environ.copy(),
                              shell=True)

        assert os.path.isfile(os.path.join('muscaria', '.travis.yml'))
        shutil.rmtree(os.path.join('muscaria'))
