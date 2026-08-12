def student(**user): # it stores into dictionary
    
    for key in user: # for printing keys
        print(key)
        
    for val in user.values(): # for printing values
        print(val)
        
    for key,val in user.items(): # for printing key,values
        print(key," - ",val)
    
student(name="Ankur",id=114,course="BCA") # can pass argument as keyword argument