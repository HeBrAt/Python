#/bin/python3


def prices_list(name, price):
    liste = []
    for x in range(1, 11):
        liste.append(str(x) + " x " + name + " : " + str(int(x) * float(price))) 
    return liste

print(prices_list("Wunderkeks", 0.79))
