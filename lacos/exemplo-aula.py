import random

a = 1
b = 2
c = 3
d = 4

random_file = random.randint(a,d)

a = input("primeiro filme: ")
b = input("segundo filme: ")
c = input("terceiro filme: ")
d = input("quarto filme: ")


while True: 
    if random_file == 1: 
        print(a)
    elif random_file == 2:
        print(b)
    elif random_file == 3:
        print(c)
    else: 
        print(d)
    break 



