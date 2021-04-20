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
for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]
    
x = 1
print("Length of all files = "+str(len(allfiles)))

for file in allfiles:

    print("in file number = "+str(x))
    with open(file, 'r', encoding='ISO-8859-1') as f:
        filedata = f.read()
        result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

        docID = 1
        #for every document-- get the doc# and the doc#'s text
        print("There are  "+str(len(result))+" documents in this document")
        for document in result[0:1]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            # Retrieve contents of TEXT tag
            text = "".join(re.findall(text_regex, document))\
                      .replace("<TEXT>", "").replace("</TEXT>", "")\
                      .replace("\n", " ")

            text = text.translate(str.maketrans('', '', string.punctuation))
            

            # step 1 - lower-case words, remove punctuation, remove stop-words, etc. 
            text = text.lower() # lower-case words
            words = text.split()

            for word in words: 
                if word not in word_dic:
                    word_dic[word] = 1
                    word=""
                else:
                    word_dic[word] = word_dic[word] + 1

            print("DocID: "+str(docID))
            print("Doc#: "+docno)
            # print("Text: "+text)
            docID = docID+1

            
    x = x +1
    print("size of dic = "+str(len(word_dic)))


print(sorted(word_dic))
            
            # step 2 - create tokens 
            # step 3 - build index
            