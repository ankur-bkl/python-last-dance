'''
1.Create a new file "practice.txt" using Python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.

2.WAF that replaces all occurrences of "Java" with "Python" in the above file.

3.Search if the word "learning" exists in the file or not.

4.WAF to find in which line of the file does the word "learning" occur first.Print -1 if the word is not found.

5.From a file containing numbers separated by commas, print the count of even numbers.

'''

with open("practice.txt","r") as f:
    data= f.read()
    # print(data)
    
    nums =data.split(",")
    count=0
    for val in nums:
        if (int(val) % 2 == 0) :
            count+=1
    print(count)       
    
    
# split without using split function

# num=""
# for i in range(len(data)):
#     if(data[i]==","):
#         print(num)
#         num= ""
#     else:
#         num+=data[i]

