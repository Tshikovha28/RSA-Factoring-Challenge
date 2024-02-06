#!bin/bash

import sys

def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    for number in numbers:
        n = int(number)
        p, q = factorize(n)
        print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main()
