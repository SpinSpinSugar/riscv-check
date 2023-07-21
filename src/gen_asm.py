"""This module creates tmp directories and asm files"""
import os
import sys
import asyncio
from typing import Coroutine
import src.riscv_check_argparse as aparse
import src.dir_manager as dm

def get_compiler_coro(args,
                      dir_manager: dm.DirManager,
                      ext: str,
                      instr: str,
                      test_file: str) -> Coroutine:
    """Call compiler with forwarded arguments and create asm files in appropriate directory"""
    compiler_name = args.compiler
    march = args.march
    mabi = args.mabi
    opt_lvl = args.opt_level
    tests_dir = dir_manager.tests_dir
    tmp_dir = dir_manager.tmp_dir
    params = f'-march={march} -mabi={mabi} -O{opt_lvl} -S {tests_dir}/{ext}/{instr}/{test_file}'
    pure_filename = test_file.removesuffix('.c')
    output_params = f'-o {tmp_dir}/{ext}/{instr}/{pure_filename}.s'
    return asyncio.create_subprocess_shell(f'{compiler_name} {params} {output_params}')

async def gen_asm(ext_and_instr_list: list[dict], args, dir_manager: dm.DirManager):
    """Parses .c files in tests/* and calls _call_compiler"""
    tests_dir = dir_manager.tests_dir
    prev_dir = dir_manager.current_dir
    dir_manager.chdir(tests_dir)

    #Run compiler to generate assembly files
    tasks = []
    for e_instr in ext_and_instr_list:
        ext = e_instr['ext']
        instr_list = e_instr['instr_list']
        for instr in instr_list:
            for test_file in os.listdir(f'{tests_dir}/{ext}/{instr}'):
                tasks.append(await get_compiler_coro(args, dir_manager, ext, instr, test_file))
    for task in tasks:
        await task.wait()
    dir_manager.chdir(prev_dir)

def main():
    """Generates asm files in tmp dir"""
    args = aparse.parse_args()
    dir_manager = dm.DirManager()
    ext_and_instr_list = dir_manager.gen_tmp_dirs()
    asyncio.run(gen_asm(ext_and_instr_list, args, dir_manager))

if __name__=='__main__':
    sys.exit(main())
