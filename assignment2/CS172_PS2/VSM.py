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
import string 
from read_index import get_content,get_term_attributes
import math

term_dict = {}
stopwords_set = set()
relevant_terms ={}
doc_set = {}

with open('stopwords.txt') as f:
    lines = f.readlines()
    for word in lines:
        word = word.rstrip()
        stopwords_set.add(word)

def get_input(arguments):
    if len(arguments) < 3:
        print("Error, invalid number of arguments.")
        return
    #TODO: Error checking here if file not found or invalid args
    arguments.pop(0)
    return arguments
    

def read_in_queries(arguments):
    if arguments is None or len(arguments) < 2:
        return

    global term_dict

    path = arguments[0]
    output_file = arguments[1]
    file = open(path, 'r')
    lines = file.readlines()
    term_dict = get_content()
    # print('term dict size ,',len(term_dict))
    
    for line in lines:
        query_text = sanitize(line)
        query_no = query_text.pop(0)
        # print("Q0:",query_no)
        # print("Term Vector:",query_text)
        # print('Length of Query:',len(query_text))
        output_set = update_doc_terms(query_text)


        for item in output_set:
            score = get_similarity_score(len(query_text),item,output_set[item])
            output_set[item] = score

        output_set = sorted(output_set.items(), key=lambda x: x[1], reverse=True)
        top_10 = output_set[:10]
        output_ranking(query_no,top_10,output_file)
        clear()
        
    return

def output_ranking(query_no, top_list, output_file):
        i = 1
        query_no = str(query_no) + " Q0 "

        f = open(output_file,'a')
        for element in top_list:
            doc_vals = str(element[0]) +" "+str(i)+" "+str(element[1])+" Exp"
            f.write(query_no+doc_vals+'\n')
            i = i + 1
        f.close()

def clear():
    global relevant_terms
    global doc_set
    relevant_terms.clear()
    doc_set.clear()


def get_similarity_score(query_size,document,dot_product):
    score = dot_product/(math.sqrt(query_size)*math.sqrt(dot_product))
    return round(score,6)

def update_doc_terms(query_terms):
    global relevant_terms
    global doc_set
    for term in query_terms:
        if term not in relevant_terms:
            term_info = get_term_attr(term,term_dict)
            if term_info:
                relevant_terms[term] = term_info

    for value in relevant_terms:
        # taking out the irrelevant frequency count
        relevant_terms[value].pop(len(relevant_terms[value])-1)
        for document in relevant_terms[value]:
            doc_no = document[0]
            if doc_no in doc_set:
                doc_set[doc_no] = doc_set[doc_no] + 1
            else:
                doc_set[doc_no] = 1
    
    return doc_set
            
        
def sanitize(lines):
    text = lines.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words = text.split()
    term_vector = []

    for word in words:
        if word not in stopwords_set:
            term_vector.append(word)

    return term_vector

def get_term_attr(token,term_dict):
    if token not in term_dict:
        return []
    else:
        return term_dict[token]

def main():
    arguments = get_input(sys.argv)
    read_in_queries(arguments)
    
if __name__ == "__main__":
    main()