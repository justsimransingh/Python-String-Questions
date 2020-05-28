'''
4. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
string=input('Enter string:')
string=string.lower()
print(string)
index=string.find('r')
print(string[0:index+1] + string[index+1:].replace('r','$'))
