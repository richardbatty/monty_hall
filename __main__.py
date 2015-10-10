import sys

import lib.game_runner as game_runner

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print game_runner.compare_strategies()

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()
