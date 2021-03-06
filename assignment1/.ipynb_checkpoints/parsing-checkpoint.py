#!/usr/bin/python3
import re
import os
import zipfile
# import string library function 
import string 

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

# define punctuation
stopwords_set = set()

#where we'll store all our words from the text
word_dic = {}
#where we'll store all our docno's and unique terms, total terms , etc.
docno_dic = {}

# inverted indices to map the ids
# tokenization process is as a conversion from a document to a sequence of (term_id, doc_id, position) 
# tuples which need to be stored in your inverted index.
termIndex = {}
docIndex = {}

with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
    zip_ref.extractall()

# putting the stopwords into a set data structure for easy comparison
with open('stopwords.txt') as f:
    lines = f.readlines()
    for word in lines:
        word = word.rstrip()
        stopwords_set.add(word)
   
# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
def get_dictionary():    
    global docno_dic

    for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
        allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]
    
    x = 1
    # print("Length of all files = "+str(len(allfiles)))

    for file in allfiles:

        # print("in file number = "+str(x))
        with open(file, 'r', encoding='ISO-8859-1') as f:
            filedata = f.read()
            result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

             #for every document-- get the doc# and the doc#'s text
            # print("There are  "+str(len(result))+" documents in this document")
            for document in result[0:]:
                
                # Retrieve contents of DOCNO tag
                docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()

                # Retrieve contents of TEXT tag
                text = "".join(re.findall(text_regex, document))\
                          .replace("<TEXT>", "").replace("</TEXT>", "")\
                          .replace("\n", " ")

                #remove punctuation, lowercase everything, split words up in the text
                text = text.translate(str.maketrans('', '', string.punctuation))
                text = text.lower() 
                words = text.split() #maintains the order of the original text

                # create a local dictionary for the current TEXT 
                local_dic = {}

                # but first lets define how many times a word occurs and at what position
                for i, word in enumerate(words,start=1):
                    if word in local_dic:
                        frequency = local_dic[word][1] + 1
                        local_dic[word][0].append(i)
                        local_dic[word][1] = frequency

                    else:
                        if word not in stopwords_set:
                            local_dic[word] = [[i],1]

                total_terms = 0

                for term in local_dic:
                    mytuple = (docno,local_dic[term])
                    frequency_of_term = len(local_dic[term][0])
                    total_terms = total_terms + frequency_of_term

                    if term not in word_dic:
                        word_dic[term] = [mytuple]
                    else:
                        word_dic[term].append(mytuple)
            
                
                # print("Text: "+text)
                docno_dic[docno] = (total_terms,len(local_dic))                
            
        x = x + 1 #increment what file we are on

    for term in word_dic:
        total_qty = 0
        for tup in word_dic[term]:
            total_qty = total_qty + tup[1][1]
        word_dic[term].append(total_qty)
        # print(term+'->'+str(word_dic[term]))
    return word_dic

def get_doc():
    global docno_dic
    return docno_dic

    
    # try:
    #     text_file = open('text_file.txt', 'wt')
    #     # text_file.write(str(word_dic))
    #     for key in word_dic:
    #         text_file.write(str(key)+":"+str(word_dic[key])+"\n")
    #     text_file.close()

    #     text_file_doc = open('doc_file.txt','wt')
    #     text_file_doc.write(str(docno_dic))
    #     text_file_doc.close()
    # except:
    #     print("Unable to write to file")
