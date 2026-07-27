def raiseToPower(baseNum,powNum):
    result=1
    for index in range(powNum):
        result=result*baseNum
    return result
# print(raiseToPower(3,2))
    
print(raiseToPower(int(input("Enter the base num: ")), int(input("Enter the power: "))))