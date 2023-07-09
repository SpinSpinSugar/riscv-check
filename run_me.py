import os

os.system('python3 src/gen_asm.py')
#os.wait()
os.system('python3 src/run_tests.py')

print('\nYou can check generated ASM in /tests/tmp')
