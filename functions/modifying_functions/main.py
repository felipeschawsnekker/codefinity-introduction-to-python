def apply_discount(price,discount=0.05):
    return price*(1-discount)

def apply_tax(price,tax=0.07):
    return price*(1+tax)

def calculate_total(price,discount=0.05,tax=0.07):
    discounted=apply_discount(price,discount)
    total=apply_tax(discounted,tax)
    return total

def talk(total_price,mode):
    print(f"Total cost with {mode} discount and tax: ${total_price:.2f}")
    
total_price_default=calculate_total(120)
talk(total_price_default,"default")

total_price_custom=calculate_total(100, discount=0.10, tax=0.08)
talk(total_price_custom,"custom")
    