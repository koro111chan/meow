def add (num1 , num2) :
    sum = num1+num2
    return sum 

def sub (num1 , num2) :
    sum = num1-num2
    return sum 

 #************************************

num1 = int (input("inter your first number")) 
operation = input("enter your sign")
num2 = int (input("inter your second number")) 
if (operation == "+") :
    sum_add = add(num1,num2)
    print("addition result is", sum_add)  
 
elif(operation == "-") :    
    sum_sub = sub(num1,num2)
    print("subtraction result is", sum_sub)  
 
#*************************************



 