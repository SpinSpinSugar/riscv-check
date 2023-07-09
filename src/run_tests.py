import os
from dataclasses import dataclass
from colorama import init, Fore
init(autoreset=True)

#TODO clean
TMP_DIR = 'tmp'
curDir = os.getcwd()
#print(curDir)
TMP_DIR = curDir + '/tests/' + TMP_DIR
#print(TMP_DIR)

os.chdir(TMP_DIR)

extDirs = os.listdir(TMP_DIR)


@dataclass
class Statistics:
    teest_counter: int = 0
    passed_counter: int = 0
stat = Statistics()

for extDir in extDirs:
    filelist = os.listdir(extDir)
    if not filelist:
        continue
    for file in os.listdir(extDir):
        test_number = 0
        test_number += 1
        commandName = file.split('.')[0]
        with open(f'{extDir}/{file}', 'r', encoding='utf-8') as asmFile:
            asmText = asmFile.read()
            fooPos = asmText.find('test')
            res = asmText.find(commandName, fooPos)
            falseRes = asmText.find(f'__{commandName}', fooPos) + 2 
        #print(res)
        stat.test_counter += 1
        if res not in [-1, falseRes]:
            print(Fore.GREEN + f'TEST #{test_number} PASSED: {commandName} is generated')
            stat.passed_counter += 1
        else:
            print(Fore.RED + f'TEST #{test_number} FAILED: {commandName} is not supported')
            print(Fore.RED + f'Error in file {extDir}/{file}')
            #if falseResi:
            #	print(Fore.RED + f'Used __{commandName}')
print(f'Stats: Passed {stat.passed_counter}/{stat.test_counter} tests')
