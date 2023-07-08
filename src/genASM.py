import os
import shutil

compilerName = input('Provide compiler name (default = riscv64-unknown-linux-gnu-gcc: ')
if not compilerName:
	compilerName = 'riscv64-unknown-linux-gnu-gcc'
	print('Using default: ', compilerName)

march = input('Provide -march arguments (default = rv64imafdc_zicsr): ')
if not march:
	march = 'rv64imafdc_zicsr'
	print('Using default: ', march)

mabi = input('Provide -mabi arguments (default = lp64d): ')
if not mabi:
	mabi = 'lp64d'
	print('Using default: ', mabi)

optLevel = input('Provide optimization level (default = 0): ')
if not optLevel:
	optLevel = '0'
	print('Using default: ', optLevel)
print()


currentDir = os.getcwd()

testsDir = ''
if currentDir.endswith('src'):
	testsDir = currentDir + '/../tests'
if currentDir.endswith('riscv-check'):
	testsDir = currentDir + '/tests'
assert(testsDir)
#print(currentDir, testsDir)

os.chdir(testsDir)
extensionsList = os.listdir()
#print(extensionsList)

#Creating tmp dir for assembly files
tmpDir = 'tmp'

if tmpDir in extensionsList:
	shutil.rmtree(tmpDir)
	extensionsList.remove(tmpDir)

os.mkdir(tmpDir)
for ext in extensionsList:
	os.mkdir(tmpDir + f'/{ext}')

#Run compiler for generate assembly files
for curDir in extensionsList:
	fileList = os.listdir(curDir)
	for file in fileList:
		fileName =  curDir + '/' + file
		clearFilename = fileName.split('.')[0]
		#print(fileName)
		params = f'-march={march} -mabi={mabi} -O{optLevel} -S {fileName}'
		outputParams = f'-o tmp/{clearFilename}.s'
		#print(f'{compilerName} {params} {outputParams}')
		stream = os.popen(f'{compilerName} {params} {outputParams}')
		stream.close()
