#!/usr/bin/env python3
"""Useful script to purge tmp"""
import shutil
import os
import sys

def main():
    """Purge tmp dir"""
    tmp_dir = os.getcwd() + '/tests/tmp'
    print(tmp_dir)
    shutil.rmtree(tmp_dir)

if __name__ == '__main__':
    sys.exit(main())
