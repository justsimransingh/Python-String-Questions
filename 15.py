'''
15. Write a Python program to count repeated characters in a string. Go to the
editor
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
'''

s=input('Enter string:')
x=set(s)
for i in x:
    if s.count(i)>1:
        print(i,s.count(i))
        
        
