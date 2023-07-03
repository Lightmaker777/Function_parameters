#Task 2: Multiple positional arguments of different types
#a single function getParity that does the same thing as the two functions in the previous task. This new function will accept a new positional argument of type String that will contain the type of parity we want to get (either odd or even).
def getParity(number, parity):    
    if parity == 'odd':
        return number % 2 != 0
    elif parity == 'even':
        return number % 2 == 0
    else:
        return "Parity indicated is unknown."
    
print(getParity(3, 'odd'), getParity(3, 'even'))  # True False
print(getParity(4, 'odd'), getParity(4, 'even'))  # False True
print(getParity(-2, 'number'))  # Parity indicated is unknown