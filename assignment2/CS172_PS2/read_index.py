#!/usr/bin/python3

import os
import sys
import ast
from parsing import get_dictionary, get_doc

# This file should contain code to receive either a document-id or 
# word or both and output the required metrics. See the assignment 
# description for more detail.

term_dictionary = {}
docno_dictionary = {}

def get_content():
    global term_dictionary
    global docno_dictionary

    term_dictionary = get_dictionary()
    docno_dictionary = get_doc()
    return term_dictionary

def getInput(arguments):
    if len(arguments) <= 2 :
        print("Error Invalid number of arguments.")
        return
    get_content()    

    if len(arguments) <=3:
        query_type = arguments[1]
        query = arguments[2]
    
        print("Query Type: "+str(query_type))
        print("Query: "+str(query))

        if query_type == "--term":
            term_attr = get_term_attributes(query)
            if len(term_attr) != 0:
                display_term_attr(query,term_attr)
        elif query_type == "--doc":
            doc_attr = get_doc_attributes(query)
            if len(doc_attr) != 0:
                display_doc_attr(query, doc_attr)
        else:
            print("Error in Input")
    elif len(arguments) > 3:
        # print("Handle multiple arguments here..\n")
        query_type = []
        query_term_doc = []
        query_type.append(arguments[1])
        query_type.append(arguments[3])
        query_term_doc.append(arguments[2])
        query_term_doc.append(arguments[4])


        
        if "--term" in query_type and "--doc" in query_type:
            term_attr = get_term_attributes(query_term_doc[0])
            total_freq = term_attr.pop()
            if len(term_attr) != 0:
                for doc in term_attr:
                    if doc[0] == query_term_doc[1]:
                        display_term_doc_attr(query_term_doc[0],doc)
                        return
            print("Error, term not in document")
        else:
            print("Error in input")
    else:
        print("Error in Input.")
        
    return


def display_term_attr(query,term_attr):
    print("Listing for term:"+str(query))
    print("Number of documents containing term: "+str(len(term_attr)-1)) 
    print("Term frequency in corpus: "+str(term_attr[len(term_attr)-1]))


def display_doc_attr(query, doc_attr):
    print("Listing for document:"+str(query))
    print("Total terms: "+str(doc_attr[0]))
    print("Distinct terms: "+str(doc_attr[1]))

def display_term_doc_attr(term, doc):
    print("Inverted list for term: ",term)
    print("In document: ",doc[0])
    print("Term frequency in document: ",doc[len(doc)-1][1])
    print("Position(s): ",doc[len(doc)-1][0])


def get_term_attributes(token):
    if token not in term_dictionary:
        return []
    else:
        return term_dictionary[token]

def get_doc_attributes(document):
    if document not in docno_dictionary:
        return []
    else:
        return docno_dictionary[document]


def main():
    # get_content()
    getInput(sys.argv)
    
if __name__ == "__main__":
    main()