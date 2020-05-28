#1. Write a Python program to calculate the length of a string.
string=input("Enter a string:")
count=0
for _ in string:
    count+=1
print("Length counted without built-in function",count)
print("Length counted with built-in function",len(string))
