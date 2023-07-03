#Task 3: Multiple keyword arguments of different types
#a single function 'greet' that greets a person differently depending on the time of the day
import datetime

def greet(*args, **kwargs) -> str:
    if 'name' in kwargs and 'date' in kwargs:
        name = kwargs['name']
        date = kwargs['date']
        if date.time() < datetime.time(12, 0):
            return f"Good Morning, {name}!"
        elif date.time() < datetime.time(18, 0):
            return f"Good Afternoon, {name}!"
        else:
            return f"Good Night, {name}!"
    else:
        return "Missing name or date argument."


print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))
print(greet())