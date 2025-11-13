# °F=(°C×1,8)+32

graus_celsius = float(input("Digite a temperatura em graus Celsius: "))

def celsius_para_fahrenheit(graus_celsius):
    graus_fahrenheit = (graus_celsius * 1.8) + 32
    return graus_fahrenheit

print(f"A temperatura em graus Fahrenheit é: {celsius_para_fahrenheit(graus_celsius)} °F")