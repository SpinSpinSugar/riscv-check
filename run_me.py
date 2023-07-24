"""This module collects arguments and runs whole program"""
from src import gen_asm
from src import run_tests
from src.formats.csvformat import CSVFormat
from src.formats.default_format import DefaultFormat
import src.riscv_check_argparse as aparse

def main() -> None:
    """Parse args then generate asm then run tests"""
    args = aparse.parse_args()
    output_format = args.format
    gen_asm.main(args)
    tests = run_tests.main()

    match output_format:
        case 'csv':
            csv_screen = CSVFormat()
            csv_screen.print()
        case 'default':
            terminal_screen = DefaultFormat(tests)
            terminal_screen.print()
        case _:
            raise RuntimeError('Unsupported output format')


    print('You can check generated ASM in /tmp')

if __name__ == '__main__':
    main()
