# ANO BISSEXTO: (ANO % 4 == 0 E ANO % 100 != 0) OU (ANO % 400 == 0)

ano = int(input("Digite o ano: "))

def eh_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    elif ano % 400 == 0:
        return True
    else:
        return False

print(f"O ano {ano} é bissexto? {eh_bissexto(ano)}")