#2. Write a Python program to count the number of characters (character frequency) in a string.
string=input("Enter string:")
s=set()
d={}
for i in set(string):
    if i not in s:
        d[i]=string.count(i)
print(d)

'''
string=input("Enter string:")
d={}
for i in set(string):
    d.update({i:s.count(i)})
print(d)
'''
