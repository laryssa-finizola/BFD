a = 0
b = 1

for _ in range(8):
    proximo_termo = a + b
    
    print(proximo_termo)
    a = b
    b = proximo_termo

print()