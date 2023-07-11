import os
import sys
import subprocess


# create virtual enviroment:
venv_proc = subprocess.Popen([sys.executable, '-m', 'venv', '.env'])
venv_proc.wait()

venv_activate_proc = subprocess.Popen(['/bin/sh', '.env/bin/activate'], stdin=subprocess.PIPE, shell=True)
venv_activate_proc.stdin.close()
venv_activate_proc.wait()
print('VENV activated')

colorama_install_proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
colorama_install_proc.wait()


os.system('python3 src/gen_asm.py')
#os.wait()
os.system('python3 src/run_tests.py')

print('\nYou can check generated ASM in /tests/tmp')
