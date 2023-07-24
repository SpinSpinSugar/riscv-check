"""RISC-V CHECK argparse wrapper"""
import argparse
import sys

def parse_args():
    """Wrapper for standard parser"""
    parser = argparse.ArgumentParser(description='Compiler options')
    parser.add_argument('compiler', type=str, help='Compiler name')
    parser.add_argument('march', type=str, help='Architecture parameter')
    parser.add_argument('mabi', type=str, help='ABI parameter')
    parser.add_argument('opt_level', type=str, help='Optimization level')
    parser.add_argument('--format',
                        type=str,
                        default='default',
                        help='output as type of formatted output')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    sys.exit()
