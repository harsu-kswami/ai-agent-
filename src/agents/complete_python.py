# loops

orders = ["first", "second", "third"]

for name in orders:
    print(f"This is the {name} order.")
    
# range question
for i in range(5):
    print(f"This is iteration number {i}.")
    
# enumerate use like a dicitionary mapping of two lists, one with the index and one with the value

for index, name in enumerate(orders):
    print(f"Order {index + 1}: {name}")


# zip is bigger version of enumerate, it can take multiple lists and combine them into a single iterable of tuples. Each tuple contains one element from each of the input lists.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


# while loops 
temperature = 30

while temperature > 20:
    print(f"The temperature is {temperature} degrees. It's too hot!")
    temperature -= 1  # Decrease the temperature by 1 degree each iteration
    
# continue and break statements

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    if i > 7:
        break  # Stop the loop if i is greater than 7
    print(i)

# walrus 
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression. This can be useful in loops and conditional statements.

value = 14
remainder = value%5

if remainder:
    print(f"The remainder of {value} divided by 5 is {remainder}.")
    
# convert into walrus operator:

value = 14
if (remainder := value % 5):
    print(f"The remainder of {value} divided by 5 is {remainder}.")
    
    
# using dicitionary instead of repeated cases

users = [
    {"id":1, "total": 100, "coupon": "P20"},
    {"id":2, "total": 150, "coupon": "F20"},
    {"id":3, "total": 200, "coupon": "X20"},
] 

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"User {user['id']} gets a discount of {discount}.")





# functions 

# features := 