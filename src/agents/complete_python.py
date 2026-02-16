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


