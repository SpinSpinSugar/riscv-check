#!/usr/bin/env python3.11
"""This module collects arguments and runs whole program"""
import os
import sys
from src import riscv_check_argparse

def main():
    """Parse args then generate asm then run tests"""
    args = riscv_check_argparse.parse_args()
    compiler_name = args.compiler
    march = args.march
    mabi = args.mabi
    opt_lvl = args.opt_level
    os.system(f'python3 src/gen_asm.py {compiler_name} {march} {mabi} {opt_lvl}')
    os.system('python3 src/run_tests.py')
    print('You can check generated ASM in /tests/tmp')

if __name__ == '__main__':
    sys.exit(main())
