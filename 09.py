'''
9. Write a Python program to remove the nth index character from a nonempty
string.
'''

s=input('Enter String:')
index=int(input("Enter the index of which character you want to remove"))
if index > -1:
    s=s.replace(s[index],'',1)
else:
    s=s[::-1].replace(s[index],'',1)
    s=s[::-1]
print(s)
