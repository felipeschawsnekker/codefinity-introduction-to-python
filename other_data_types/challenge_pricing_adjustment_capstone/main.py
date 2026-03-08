grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

#Check and Update Price
category,price,quantity = grocery_inventory["Eggs"]
if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category, price - 1, quantity)

print("Updated inventory:", grocery_inventory)

#Add a New Item
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

#Manage Stock
category,price,quantity=grocery_inventory["Milk"]
if quantity<10:
    print("milk needs to be restocked. increasing stock by 20 units.")
    grocery_inventory["Milk"]=(category,price,quantity+20)
else:
    print("Milk has sufficient stock.")
    
#Remove Item Based on Price
category,price,quantity=grocery_inventory["Apples"]
if price>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price")

#Final Print
print(f"Updated Inventory: {grocery_inventory}")
