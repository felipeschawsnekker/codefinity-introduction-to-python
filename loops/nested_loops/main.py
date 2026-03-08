produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries=[produce,dairy]

for item in groceries:
    print(item)
    for items in item:
        print("Item name:",items)
        print("")