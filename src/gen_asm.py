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

XLEN = 0
if MARCH.find('32') != -1:
    XLEN = 32
elif MARCH.find('64') != -1:
    XLEN = 64
else:
    raise NotImplementedError('not 32 or 64 bit arch,128 support not added')

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

os.mkdir(TMP_DIR)
for ext in extensionsList:
    os.mkdir(TMP_DIR + f'/{ext}')

#Run compiler for generate assembly files
for curDir in extensionsList:
    fileList = os.listdir(curDir)
    for file in fileList:
        fileName =  curDir + '/' + file
        clearFilename = fileName.split('.')[0]
        #print(fileName)
        params = f'-DXLEN={XLEN} -march={MARCH} -mabi={MABI} -O{OPT_LEVEL} -S {fileName}'
        outputParams = f'-o {TMP_DIR}/{clearFilename}.s'
        #print(f'{compilerName} {params} {outputParams}')
        stream = os.popen(f'{COMPILER_NAME} {params} {outputParams}')
        stream.close()

