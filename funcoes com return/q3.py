a = int(input("digite um numero: "))
b = int(input("digite um numero: "))

def maior(a,b):
    if a > b:
        return "A é maior que B"
    elif b > a:
        return "B é maior que A"
    else:
        return " A = B"
    
print(maior(a,b))