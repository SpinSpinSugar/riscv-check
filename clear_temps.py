import shutil
import os

tmpDir = os.getcwd() + '/tests/tmp'
print(tmpDir)
shutil.rmtree(tmpDir)
