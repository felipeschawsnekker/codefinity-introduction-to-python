prices = [29.99, 45.50, 12.75, 38.20]

for i in range (len(prices)):
    if(i==0):
        prices[i]*=1-0.10
    elif(i==1):
        prices[i]*=1-0.20
    elif(i==2):
        prices[i]*=1-0.15
    elif(i==3):
        prices[i]*=1-0.05
    else:
        print("No value")
    print(f"Updated price for item {i}: ${prices[i]:.2f}:")
