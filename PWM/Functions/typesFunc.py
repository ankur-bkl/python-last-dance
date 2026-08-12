# 1- perfrom a task
# 2- return a value

def get_greeting(name):
    return f"Hi {name}"

message =get_greeting("ankur")

print(message)

file = open("context.txt","w")
file.write(message)