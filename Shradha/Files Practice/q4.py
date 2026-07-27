'''
1.Create a new file "practice.txt" using Python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

2.WAF that replaces all occurrences of "Java" with "Python" in the above file.

3.Search if the word "learning" exists in the file or not.

4.WAF to find in which line of the file does the word "learning" occur first.Print -1 if the word is not found.
'''

def checkForWord():
    word="learning"
    with open("practice.txt","r") as f:
        data=f.read()
    
        if(data.find(word) != -1): #checks if the index is not negative means positive so foundextract
            print("Found!")
        else:
            print("Not Found!")
            
def checkForLine():
    word="xlearning"
    data=True
    lineNo =1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(lineNo)
                return
            lineNo+=1
    return -1

print(checkForLine())
            




