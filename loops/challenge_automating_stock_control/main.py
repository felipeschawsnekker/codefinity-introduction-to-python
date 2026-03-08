# Initialize the inventory dictionary with stock details
discount_threshold = 100
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

for item_name in inventory:
    #Item": [current stock, minimum stock, 
    #restock quantity, on sale (True/False)]
    current_stock = inventory[item_name][0]
    minimum_required_stock=inventory[item_name][1]
    restock_quantity=inventory[item_name][2]
    sale_status=inventory[item_name][3]
    necessary_to_restock=minimum_required_stock-current_stock

    #RESTOCKING
    while current_stock<minimum_required_stock:
        current_stock+=restock_quantity
        inventory.update()
        if current_stock>=minimum_required_stock:
            if(restock_quantity-necessary_to_restock>0):
                restock_quantity-=necessary_to_restock
            else:
                restock_quantity=0
            print(f"Processing {item_name}")
            
    inventory[item_name][0]=current_stock
    inventory[item_name][1]=minimum_required_stock
    inventory[item_name][2]=restock_quantity
    inventory[item_name][3]=sale_status
    if(current_stock>discount_threshold and inventory[item_name][3]==False):
        inventory[item_name][3]=True
        
        
print("Processing completed")

print(inventory)

    


