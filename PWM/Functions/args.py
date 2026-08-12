def multiply(*numbers): # *args inside function it becomes a tuple
    result =1
    for number in numbers:
        # print(number)
        result*=number
    return result

# multiply(1,2,3,5,6,6,7)
print(multiply(1,2,3,5,6,6,7))