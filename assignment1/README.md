# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Eduardo Rocha
## Team member 2 - Sameh Fazli

Explanation of your design:
```
We decided to parse the documents in the parsing.py script and then send the relevant data 
to the read_index.py script. We hold our data as key->value pairs. Where our key's are 
the terms in the documents and the value's are a list of tuples. These tuples contain information
about the attributes of the term. 
There is also another data structure which holds the information of each document, such as total
number of words and unique number of words. 

To run our code make sure the parsing.py and read_index.py scripts are initialized. 
1) ./read_index.py --term <term>
2) ./read_index.py --doc <docno>
3) ./read_index.py --term <term> --doc <docno>
```

Language used: 
```
Python3.5
```