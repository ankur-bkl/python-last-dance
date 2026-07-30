#Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def average(self):
        print("Average: ",(float(self.sub1)+float(self.sub2)+float(self.sub3))/3)
        
s1=Student(input("Enter the name: "),input("Enter the marks of Subject 1: "),input("Enter the marks of Subject 2: "),input("Enter the marks of Subject 3: "))
print(s1.name)
print(s1.sub1,s1.sub2,s1.sub3)
s1.average()