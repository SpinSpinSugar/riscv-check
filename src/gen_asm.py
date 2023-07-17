"""This module creates tmp directories and asm files"""
import os
import shutil
import sys
import asyncio
from dataclasses import dataclass
import riscv_check_argparse

@dataclass
class ExtensionWithInstructions:
    """Small wrapper"""
    ext: str = ''
    instr_list: list = None

class DirManager:
    """Class to manage"""
    tmp_dir: str = 'tmp'
    tests_dir: str = ''
    current_dir: str = ''

    def __init__(self):
        self.tmp_dir = 'tmp'
        self.tests_dir = ''
        self.current_dir = os.getcwd()

    def _calculate_tests_dir(self):
        if self.current_dir.endswith('src'):
            self.tests_dir = self.current_dir + '/../tests'
        elif self.current_dir.endswith('riscv-check'):
            self.tests_dir = self.current_dir + '/tests'
        else:
            raise RuntimeError('Please, run program in appropriate directory')
        assert self.tests_dir
    def chdir(self, directory: str):
        """Change directory"""
        os.chdir(directory)
        self.current_dir = directory
    def gen_tmp_dirs(self):
        """Generate directories for asm files in /tests/tmp"""
        self._calculate_tests_dir()
        prev_dir = os.getcwd()
        self.chdir(self.tests_dir)
        extensions_list = os.listdir()
        self._clear_tmp(extensions_list)
        extensions_with_instr = self._gen_extensions_with_instr_list(extensions_list)
        os.mkdir(self.tmp_dir)
        for e_instr in extensions_with_instr:
            ext = e_instr.ext
            instr_list = e_instr.instr_list
            os.mkdir(f'{self.tmp_dir}/{ext}')
            for instr_name in instr_list:
                os.mkdir(f'{self.tmp_dir}/{ext}/{instr_name}')
        self.chdir(prev_dir)
        return extensions_with_instr

    def _clear_tmp(self, ext_list: []):
        """Clear tmp"""
        if self.tmp_dir in ext_list:
            shutil.rmtree(self.tmp_dir)
            ext_list.remove(self.tmp_dir)

    def _gen_extensions_with_instr_list(self, ext_list : list) -> list:
        """Internal useful method to paste together extension name and list of instructions"""
        res = []
        for ext in ext_list:
            ext_and_instr = ExtensionWithInstructions(ext, os.listdir(f'{self.tests_dir}/{ext}'))
            res.append(ext_and_instr)
        return res

async def main():
    """Generates asm files in tmp dir"""
    args = riscv_check_argparse.parse_args()
    dir_manager = DirManager()
    ext_and_instr_list = dir_manager.gen_tmp_dirs()
    await gen_asm(ext_and_instr_list, args, dir_manager)

async def _call_compiler(args, dir_manager: DirManager, ext: str, instr: str, test_file: str):
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
    return await asyncio.create_subprocess_shell(f'{compiler_name} {params} {output_params}')


async def gen_asm(ext_and_instr_list: list, args, dir_manager: DirManager):
    """Parses .c files in tests/* and calls _call_compiler"""
    tests_dir = dir_manager.tests_dir
    prev_dir = dir_manager.current_dir
    dir_manager.chdir(tests_dir)

    #Run compiler to generate assembly files

    tasks = []
    for e_instr in ext_and_instr_list:
        ext = e_instr.ext
        instr_list = e_instr.instr_list
        for instr in instr_list:
            for test_file in os.listdir(f'{tests_dir}/{ext}/{instr}'):
                tasks.append(await _call_compiler(args, dir_manager, ext, instr, test_file))
    for task in tasks:
        await task.wait()
    dir_manager.chdir(prev_dir)

if __name__=='__main__':
    sys.exit(asyncio.run(main()))
