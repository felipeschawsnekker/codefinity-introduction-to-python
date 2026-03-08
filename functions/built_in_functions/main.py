# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for item_name in products:
    price=float(products[item_name][0])
    quantity_sold=int(products[item_name][1])
    total_sales=price*quantity_sold
    total_sales_list.append(price*quantity_sold)
    
    
    print ("Item name: ",item_name)
    print(f"Price: ${price:.2f}")
    print("Quantity sold: ",quantity_sold)
    print(f"Total sales for {item_name}: ${total_sales:.1f}")
    print(" ")
    
print(total_sales_list)
total_sum=sum(total_sales_list)
max_sales=max(total_sales_list)
min_sales=min(total_sales_list)
print(f"Total sum of all sales: ${total_sum:.2f}")
print(f"Maximum sales: ${max_sales:.2f}")
print(f"Minimum sales: ${min_sales:.2f}")

    