#!/usr/bin/env python3
"""
Author : sukarus <sukarus@tiny-python-5c9f86c9df-j7xmd>
Date   : 2022-04-24
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.word

    #    print(f'word = "{pos_arg}"')
    if pos_arg[0] in "aeiouAEIOU":
        print(f"Ahoy, Captain, an {pos_arg} off the larboard bow!")
    else:
        print(f"Ahoy, Captain, a {pos_arg} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
