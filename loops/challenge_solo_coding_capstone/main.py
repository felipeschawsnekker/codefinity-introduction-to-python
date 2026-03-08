# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item_name in inventory:
    print("Item Name: ",item_name)
    print("Current Stock: ",inventory[item_name][0])
    if inventory[item_name][0]<30:
        print("It needs restocking")
        print(f"{item_name} need restocking.")
    elif inventory[item_name][0]>100:
        print(f"{item_name} should be sold at the discounted price of {inventory[item_name][2]}.")
    elif inventory[item_name][0]>=30 and inventory[item_name][0]<=100:
        print(f"{item_name} should be sold at the regular price of {inventory[item_name][1]}.")
    else:
        print("")
        
    print("Regular Price: ",inventory[item_name][1])
    print("Discounted Price: ",inventory[item_name][2])
    print(" ")
    
    
