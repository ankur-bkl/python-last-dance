'''
1.Create a new file "practice.txt" using Python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

2.WAF that replaces all occurrences of "Java" with "Python" in the above file.

'''

with open("practice.txt","r") as f:
    data=f.read()
newData = data.replace("Java","Python")
print(newData)

# overwriting the data
with open("practice.txt","w") as f:
    data=f.write(newData)