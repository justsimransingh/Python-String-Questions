'''
8. Write a Python function that takes a list of words and returns the length of the
longest one
'''
s=input('Enter list of words differentiating by spaces')
l=s.split(' ')
length=0
for i in l:
    if len(i) > length:
        length=len(i)
        longest=i
print(longest)
