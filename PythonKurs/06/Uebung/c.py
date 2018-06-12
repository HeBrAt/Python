#/bin/python3


shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_shelf(article):
    for x in range(0, len(shelf)):
        if shelf[x] == "leer":
            shelf[x] = article
            return

    shelf.append(article)
    return

add_shelf("Rubik's Cube")
print(shelf)
