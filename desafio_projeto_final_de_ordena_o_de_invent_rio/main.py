# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1=items[0:9]
bubblegum_price="$1.50"

candy2=items[11:20]
chocolate_price="$2.00"

dry_goods=items[22:27]
pasta_price="$5.40"

category1=categories[0:11]
category2=categories[13:24]


print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")
