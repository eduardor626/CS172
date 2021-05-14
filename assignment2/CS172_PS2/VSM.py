#
# How to run? Lets assume you wrote the code in Python. To run:
# python VSM.py < query−file > < name−of−results−file >
# 
# Your program should have TWO command line arguments:
# path to query file (path to query_list.txt)
# name of output file / results file 


import os
import sys
import ast
from read_index import get_content, get_term_attributes, get_doc_attributes


def get_input(arguments):
    if len(arguments) < 3:
        print("Error, invalid number of arguments.")
        return
    print(arguments)


def main():
    get_input(sys.argv)
    
if __name__ == "__main__":
    main()