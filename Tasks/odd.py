#!/usr/bin/env python3
"""A script that prints out odd numbers from 1 to 50"""

def print_odd_number():
    """Prints out odd numbers from 1 to 50."""
    for i in range(1,50):
        if i % 2 != 0:
            print(i, end=', ')
        
if __name__ == '__main__':
    print_odd_number()