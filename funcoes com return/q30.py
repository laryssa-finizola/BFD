nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

def gerar_email(nome, sobrenome):
    email = nome.lower() + "." + sobrenome.lower() + "@email.com"
    return email

print(gerar_email(nome, sobrenome))