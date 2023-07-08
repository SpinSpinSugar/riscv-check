import os

import colorama
from colorama import init, Fore, Style
init(autoreset=True)

#TODO clean
tmpDir = 'tmp'
curDir = os.getcwd()
#print(curDir)
tmpDir = curDir + '/tests/' + tmpDir
#print(tmpDir)

os.chdir(tmpDir)

extDirs = os.listdir(tmpDir)
for extDir in extDirs:
	filelist = os.listdir(extDir)
	if not filelist:
		continue
	for file in os.listdir(extDir):
		commandName = file.split('.')[0]
		asmText = open(f'{extDir}/{file}', 'r').read()
		fooPos = asmText.find('test')
		res = asmText.find(commandName, fooPos)
		falseRes = asmText.find(f'__{commandName}', fooPos) + 2
		
		#print(res)
		if res != -1 and res != falseRes:
			print(Fore.GREEN + f'TEST PASSED: {commandName} is generated')
		else:
			print(Fore.RED + f'TEST FAILED: {commandName} is not supported')
			print(Fore.RED + f'Error in file {extDir}/{file}')
			
			#if falseResi:
			#	print(Fore.RED + f'Used __{commandName}')


