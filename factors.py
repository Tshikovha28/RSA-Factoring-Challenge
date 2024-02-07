#!/usr/bin/env python3

import sys

def factorize(n):
    if n % 2 == 0:
        return 2, n // 2

    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return i, n // i

    return n, 1

def print_usage_and_exit():
    print("Usage: {} <file>".format(sys.argv[0]))
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    for number in numbers:
        try:
            n = int(number)
            p, q = factorize(n)
            print(f"{n}={p}*{q}")
        except ValueError:
            print(f"Error: Invalid number format - {number}")

if __name__ == "__main__":
    main()

