RISC-V Check
==============
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint) [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

Description
---------
Simple script for testing RISC-V codegeneration of RISC-V extensions (currently bitmanip only)
## Quick start:
```sh
git clone https://github.com/SpinSpinSugar/riscv-check
```
Setup venv:
```sh
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
Example (gcc):
```sh
python3 riscv_check.py riscv64-unknown-linux-gnu-gcc rv64gv_zba_zbb_zbc_zbs lp64d 3
python3 riscv_check.py --format="csv" riscv64-unknown-linux-gnu-gcc rv64gv_zba_zbb_zbc_zbs lp64d 3
```
Example (clang):
```sh
python3 riscv_check.py --params="--target=riscv64" clang rv64gv_zba_zbb_zbc_zbs lp64d 3
python3 riscv_check.py --params="--target=riscv64" --format=csv clang rv64gv_zba_zbb_zbc_zbs lp64d 3 
```

### How to add your test
```sh
cd tests
# for example zba
mkdir %YOUR RISC-V EXTENSION NAME%
cd %YOUR RISC-V EXTENSION NAME%
# for example andn
mkdir %INSTRUCTION_NAME%
# for example andn64.c
touch %TEST_NAME%.c
```
File format (function name is important!!!):
```C
#include <stdint.h>
int64_t test(args...) {
	//your code that you expect compiler to convert to INSTRUCTION_NAME assembly line
}
```

### Bitmanip march for testing:
* rv64id_zba_zbb_zbc_zbs
