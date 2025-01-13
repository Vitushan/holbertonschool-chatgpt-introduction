#!/usr/bin/python3
import sys

def factorial(n):

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if len(sys.argv) > 1:
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error : the factorial is not define for the negative numbers.")
        else:
            f = factorial(number)
            print(f)
    except ValueError:
        print("Error : stdin is a integer.")
else:
    print("Usage : ./factorial.py <integer_positif>")
