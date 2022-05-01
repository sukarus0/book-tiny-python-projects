#!/usr/bin/env python3
"""
Author : sukarus <sukarus@tiny-python-5c9f86c9df-j7xmd>
Date   : 2022-05-01
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bringing the items',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')
    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    isSorted = args.sorted

    if isSorted:
        items.sort()

    items_str=''
    if (len(items)==1):
        items_str = items[0]
    elif (len(items)==2):
        items_str = f'{items[0]} and {items[1]}' 
    else:
        items[-1]=f'and {items[-1]}'
        items_str = ', '.join(items)

    print(f'You are bringing {items_str}.')



# --------------------------------------------------
if __name__ == '__main__':
    main()
