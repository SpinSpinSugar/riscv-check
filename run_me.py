"""This module collects arguments and runs whole program"""
from src import gen_asm
from src import run_tests
def main() -> None:
    """Parse args then generate asm then run tests"""
    gen_asm.main()
    run_tests.main()
    print('You can check generated ASM in /tmp')

if __name__ == '__main__':
    main()
