'''
13. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''

def insert_string_middle(s,middle):
    l=len(s)//2
    print(s[:l] + middle + s[l:])
string=input('Enter string:')
middle=input('Enter the middle string:')
insert_string_middle(string,middle)
