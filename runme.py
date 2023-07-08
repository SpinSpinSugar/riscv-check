import os

os.system('python3 src/genASM.py')
#os.wait()
os.system('python3 src/runtests.py')

print('\nYou can check generated ASM in /tests/tmp')
