#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the given integer n. If n is 0, returns 1.

    Raises:
        RecursionError: If the maximum recursion depth is exceeded.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    """
    The main entry point of the script. It reads an integer from the command line argument,
    computes its factorial using the factorial function, and prints the result.
    
    Usage:
        ./factorial_recursive.py <number>
        
    Example:
        ./factorial_recursive.py 4
        Output: 24
    """
    # Read the input number from command line arguments
    number = int(sys.argv[1])

    # Calculate the factorial of the input number
    f = factorial(number)

    # Print the result
    print(f)
