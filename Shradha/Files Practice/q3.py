'''
1.Create a new file "practice.txt" using Python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

2.WAF that replaces all occurrences of "Java" with "Python" in the above file.

3.Search if the word "learning" exists in the file or not.

'''

def checkForWord():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
    
        if(data.find(word) != -1): #checks if the index is not negative means positive so foundextract
            print("Found!")
        else:
            print("Not Found!")
            



