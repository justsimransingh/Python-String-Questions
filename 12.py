'''
12. Write a Python function to create the HTML string with tags around the
word(s).
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''
def add_tags(tag,content):
    print('<{0}>{1}</{0}>'.format(tag,content))
tag=input('Enter tag:')
content=input('Enter content:')
add_tags(tag,content)
