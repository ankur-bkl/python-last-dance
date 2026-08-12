message = "b" #global variable

def greet(name):
    global message # use to declare as gloabal if needed
    message ="a" #local variable

greet("Mosh")
print(message)