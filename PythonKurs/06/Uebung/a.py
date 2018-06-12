#/bin/python3

cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):
    summe = 0.0
    
    for s in l:
        summe += s

    return summe
    
print(list_sum(cart_prices))

