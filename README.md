
You are to write a program that takes a list of strings containing integers and words and returns a sorted version of the list. The output should maintain the positions of strings and numbers as they appeared in the original string (See examples below).

The goal is to sort this list in such a way that all words are in alphabetical order and all integers are in numerical order. Furthermore, if the nth element in the list is an integer it must remain an integer, and if it is a word it must remain a word.

## Examples
### input
python main.py car truck 8 4 bus 6 1
### output 
bus car 1 4 truck 6 8

### input
python main.py  8 4 6 1 -2 9 5
### output
-2 1 4 5 6 8 9
### input
python main.py 1
### output 
1
