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
from read_index import get_content,get_term_attributes

term_dict = {}


def get_input(arguments):
    if len(arguments) < 3:
        print("Error, invalid number of arguments.")
        return
    #TODO: Error checking here if file not found or invalid args
    arguments.pop(0)
    return arguments
    

def read_in_queries(arguments):
    path = arguments[0]
    print(path)
    file = open(path, 'r')
    lines = file.readlines()
    for line in lines:
        print(line)

def get_term_attr(token,term_dict):
    if token not in term_dict:
        return []
    else:
        return term_dict[token]

def main():
    arguments = get_input(sys.argv)
    read_in_queries(arguments)
    # term_dict = get_content()




    
if __name__ == "__main__":
    main()