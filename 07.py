'''
7. Write a Python program that accepts a comma separated sequence of
words as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white
'''
s=input('Enter comma separated sequence of words:')
l=s.split(',')
l=set(l)
l=list(l)
l.sort()
print(l)
