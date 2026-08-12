# printing numbers from 1 to a given number n,
# replacing multiples of 3 with "Fizz", 
# multiples of 5 with "Buzz", 
# and multiples of both 3 and 5 with "FizzBuzz"

def fizzBuzz(n):
    for num in range(1,n+1):
        if num%3 == 0:
            print("Fizz",num)
        elif num%5 == 0:
            print("Buzz",num)
        elif num%3==0  & num%5==0:
            print("FizzBuzz",num)
        else:
            print(num)

fizzBuzz(int(input("Enter the number: ")))