#!/usr/bin/env python3
"""A script that add and multiplies all numbers entered by the user"""


def calculator():
    """A calculator that adds and multiplies all numbers entered by the user."""
    add = 0
    mul = 1

    while True:
        try:
            arr = [float(i) for i in input("Enter a number or charater to stop: ").split()]
            add += sum(arr)
            mul *= arr[0]
        except ValueError:
            break
    print(f"Sum of entered numbers: {add}")
    print(f"Multiplication of entered numbers: {mul}")
if __name__ == "__main__":
    calculator()

 