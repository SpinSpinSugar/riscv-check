import os
import shutil

COMPILER_NAME = input('Provide compiler name (default = riscv64-unknown-linux-gnu-gcc: ')
if not COMPILER_NAME:
    COMPILER_NAME = 'riscv64-unknown-linux-gnu-gcc'
    print('Using default: ', COMPILER_NAME)

MARCH = input('Provide -march arguments (default = rv64imafdc_zicsr): ')
if not MARCH:
    MARCH = 'rv64imafdc_zicsr'
    print('Using default: ', MARCH)

"""
XLEN = 0
if MARCH.find('32') != -1:
    XLEN = 32
elif MARCH.find('64') != -1:
    XLEN = 64
else:
    raise NotImplementedError('not 32 or 64 bit arch,128 support not added')
"""

MABI = input('Provide -mabi arguments (default = lp64d): ')
if not MABI:
    MABI = 'lp64d'
    print('Using default: ', MABI)

OPT_LEVEL = input('Provide optimization level (default = 0): ')
if not OPT_LEVEL:
    OPT_LEVEL = '0'
    print('Using default: ', OPT_LEVEL)
print()


currentDir = os.getcwd()

TESTS_DIR = ''
if currentDir.endswith('src'):
    TESTS_DIR = currentDir + '/../tests'
if currentDir.endswith('riscv-check'):
    TESTS_DIR = currentDir + '/tests'

assert TESTS_DIR
#print(currentDir, TESTS_DIR)

os.chdir(TESTS_DIR)
extensionsList = os.listdir()
#print(extensionsList)

#Creating tmp dir for assembly files
TMP_DIR = 'tmp'

if TMP_DIR in extensionsList:
    shutil.rmtree(TMP_DIR)
    extensionsList.remove(TMP_DIR)

instrList = []
for ext in extensionsList:
    instrList.append((ext, os.listdir(f'{TESTS_DIR}/{ext}'))
)

#print(instrList)

os.mkdir(TMP_DIR)
for instrDir in instrList:
    os.mkdir(TMP_DIR + f'/{instrDir[0]}')
    for instrName in instrDir[1]:
        os.mkdir(TMP_DIR + f'/{instrDir[0]}/{instrName}') 


#Run compiler for generate assembly files
for instr in instrList:
    for instrName in instr[1]:
        #print(instr[1])
        #print(f'{TESTS_DIR}/{instr[0]}/{instrName}')
        for testFile in os.listdir(f'{TESTS_DIR}/{instr[0]}/{instrName}'):
            filename_no_ext = testFile.removesuffix('.c')
            params = f'-march={MARCH} -mabi={MABI} -O{OPT_LEVEL} -S {TESTS_DIR}/{instr[0]}/{instrName}/{testFile}'
            outputParams = f'-o {TMP_DIR}/{instr[0]}/{instrName}/{filename_no_ext}.s'
            #print(f'{COMPILER_NAME} {params} {outputParams}')
            stream = os.popen(f'{COMPILER_NAME} {params} {outputParams}')
            stream.close()

