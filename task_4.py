#Task 4: Packing and unpacking positional arguments
# a function sumAll that gets the sum of all values in different lists. The function will accept any number of lists, each containing a variable amount of integers

def sumAll(*args) -> int:
    total_sum = 0
    for lst in args:
        for num in lst:
            if isinstance(num, int):
                total_sum += num
    return total_sum
test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

print(sumAll(*test1))  
print(sumAll(*test2))  
