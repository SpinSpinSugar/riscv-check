"""Separated class"""
import os
import shutil
import warnings

class DirManager:
    """Class to manage creating tmp dirs"""
    tmp_dir: str = 'tmp'
    tests_dir: str = ''
    current_dir: str = ''
    calculated: bool = False
    def __init__(self, autocalc: bool = True):
        self.tmp_dir = 'tmp'
        self.tests_dir = ''
        self.current_dir = os.getcwd()
        self.calculated = False
        if autocalc:
            self._calculate_tests_dir()
    def _calculate_tests_dir(self):
        """Method to calculate paths"""
        # sorry
        if self.current_dir.endswith('src'):
            self.tests_dir = self.current_dir + '/../tests'
        elif self.current_dir.endswith('riscv-check'):
            self.tests_dir = self.current_dir + '/tests'
        else:
            raise RuntimeError('Please, run program in appropriate directory')
        assert self.tests_dir
        if self.current_dir.endswith('src'):
            self.tmp_dir = self.current_dir + '/../tmp'
        elif self.current_dir.endswith('riscv-check'):
            self.tmp_dir = self.current_dir + '/tmp'
        else:
            raise RuntimeError('Please, run program in appropriate directory')
        assert self.tests_dir
        self.calculated = True
    def chdir(self, directory: str):
        """Change directory"""
        os.chdir(directory)
        self.current_dir = directory

    def gen_tmp_dirs(self):
        """Generate directories for asm files in /tests/tmp"""
        if not self.calculated:
            warnings.warn("Please, call calculate_tests_dir before this method")
        prev_dir = os.getcwd()
        self.chdir(self.tests_dir)
        extensions_list = os.listdir()
        self._clear_tmp()
        extensions_with_instr = self._gen_extensions_with_instr_list(extensions_list)
        os.mkdir(self.tmp_dir)
        for e_instr in extensions_with_instr:
            ext = e_instr['ext']
            instr_list = e_instr['instr_list']
            os.mkdir(f'{self.tmp_dir}/{ext}')
            for instr_name in instr_list:
                os.mkdir(f'{self.tmp_dir}/{ext}/{instr_name}')
        self.chdir(prev_dir)
        return extensions_with_instr

    def _clear_tmp(self):
        """Clear tmp"""
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)

    def _gen_extensions_with_instr_list(self, ext_list : list[str]) -> list[dict]:
        """Internal useful method to paste together extension name and list of instructions"""
        res = []
        for ext in ext_list:
            ext_and_instr = {'ext': ext, 'instr_list': os.listdir(f'{self.tests_dir}/{ext}')}
            res.append(ext_and_instr)
        return res
