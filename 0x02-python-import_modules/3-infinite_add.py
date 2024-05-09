#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    """
    A program that prints the result of the addition of all arguments
    """
    num_args = len(sys.argv) - 1
    int_args = [int(arg) for arg in sys.argv[1:]]  
    print(sum(int_args))