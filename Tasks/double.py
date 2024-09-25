#!/usr/bin/env python3
"""A script that doubles the number given to it."""

def double_number():
    """Doubles the number entered by the user."""
    num = float(input('Enter a number: '))
    doubled_num = num * 2
    print(f'The double of {num} is {doubled_num}')


if __name__ == '__main__':
    double_number()