#palindromo = uma palavra ou frase que pode ser lida tanto da esquerda para a direita quanto da direita para a esquerda
#ex: arara, radar, ovo, asa, anilina, socos

palavra = (input("Digite uma palavra: "))

def verificar_palindromo(palavra):
    if palavra == palavra[::-1]:
        return "É palíndromo"
    else:
        return "Não é palíndromo"
    
print(verificar_palindromo(palavra))