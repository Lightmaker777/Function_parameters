#Task 1: Simple functions with single positional arguments
#two simple functions isOdd and isEven that each take a single Integer and return a Boolean indicating whether the passed value is odd or is even.

def isOdd(num):  
    return num % 2 != 0
      

def isEven(num):
    return num % 2 == 0
    
   
        


print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))
