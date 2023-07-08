# riscv-check

Simple script for autotesting codegen

## TODO:
* multiple tests for one instruction
* Improve analysis (not just find substr with INSTRUCTION_NAME)

## How to use:
* git clone https://github.com/SpinSpinSugar/riscv-check
* if not installed: pip install colorama
* python3 runme.py
* optional: python3 clearTemps.py

### How to add your test
* cd tests
* mkdir %YOUR RISC-V EXTENSION NAME%, for example zba
* touch %INSTRUCTION_NAME%.c, for example ctz.c

### File format (function name is important!!!)
* int test(args...) {
	//your code that you expect compiler to convert to INSTRUCTION_NAME assembly line
}

### Bitmanip march for testing:
* rv64id_zba_zbb_zbc_zbs