import os
from dataclasses import dataclass
from colorama import init, Fore
init(autoreset=True)

#TODO clean #=pylint: disable=fixme 
curDir = os.getcwd()
#print(curDir)
TMP_DIR = ''
if curDir.endswith('src'):
    TMP_DIR = curDir + '/../tests/tmp'
elif curDir.endswith('riscv-check'):
    TMP_DIR = curDir + '/tests/tmp'
else:
    exit(1)
os.chdir(TMP_DIR)
#print(TMP_DIR)

@dataclass
class Statistics:
    test_counter: int = 0
    passed_counter: int = 0
total_stat = Statistics()

extList = os.listdir(TMP_DIR)
for extDir in extList:
    instrDirList = os.listdir(extDir)
    #print(instrDirList)
    for instrDir in instrDirList:
        testsList = os.listdir(f'{extDir}/{instrDir}')
        test_number = 0
        #print(testsList)
        ext_stat = Statistics()
        print(instrDir)
        for file in testsList:
            test_number += 1
            commandName = file.removesuffix('.s')
            # FIXME
            with open(f'{extDir}/{instrDir}/{commandName}.s', 'r', encoding='utf-8') as asmFile:
                asmText = asmFile.read()
                fooPos = asmText.find('test')
                res = asmText.find(instrDir, fooPos)
                falseRes = asmText.find(f'__{instrDir}', fooPos) + 2
                falseRes_builtin = asmText.find(f'\t__builtin_riscv')
            #print(res)
            ext_stat.test_counter += 1
            total_stat.test_counter += 1
            if (res not in [-1, falseRes]) and (falseRes_builtin == -1):
                print(Fore.GREEN + f'TEST #{test_number} PASSED: {commandName} is generated')
                ext_stat.passed_counter += 1
                total_stat.passed_counter += 1
            else:
                print(Fore.RED + f'TEST #{test_number} FAILED: {commandName} is not supported')
                #print(Fore.RED + f'Error in file {extDir}/{instrDir}/{file}')
                #if falseResi:
                #	print(Fore.RED + f'Used __{commandName}')
        print(f'Stats for {instrDir}: Passed {ext_stat.passed_counter}/{ext_stat.test_counter} tests\n')
print(f'Total: Passed {total_stat.passed_counter}/{total_stat.test_counter} tests')

