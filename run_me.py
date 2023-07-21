"""This module collects arguments and runs whole program"""
from src import gen_asm
from src import run_tests
from src.screens.terminal_screen import TerminalScreen

def main() -> None:
    """Parse args then generate asm then run tests"""
    gen_asm.main()
    tests = run_tests.main()
    terminal_screen = TerminalScreen(tests)
    terminal_screen.print()
    print('You can check generated ASM in /tmp')

if __name__ == '__main__':
    main()
