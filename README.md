# riscv-check
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
=========
Simple script for testing RISC-V codegeneration of RISC-V extensions (currently bitmanip only)

## How to use:
```
git clone https://github.com/SpinSpinSugar/riscv-check
python3 run_me.py
(if nothing happens when script trying to download packages: just restart, it's python bug")
optional: python3 clearTemps.py
```

### How to add your test
```
cd tests
mkdir %YOUR RISC-V EXTENSION NAME%, for example zba
cd %YOUR RISC-V EXTENSION NAME%
mkdir %INSTRUCTION_NAME%, for example andn
touch %TEST_NAME%.c, for example andn
```

### File format (function name is important!!!)
```
int test(args...) {
	//your code that you expect compiler to convert to INSTRUCTION_NAME assembly line
}
```

### Try me:
* python3 run_me.py riscv64-unknown-linux-gnu-gcc rv64gv_zba_zbb_zbc_zbs lp64d 3
#for Syntacore's clang
* python3 run_me.py "%PATH%/sc-dt_2022.12-sp1/llvm/bin/clang --target=riscv64" rv64gv_zba_zbb_zbc_zbs lp64d 3
* ALSO: --format=csv



### Bitmanip march for testing:
* rv64id_zba_zbb_zbc_zbs

