numero1 = float(input("Digite o primeiro número: "))
operador = input("Digite um operador (+ - * /): ")
numero2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma de {numero1} + {numero2} = {round(resultado, 2)}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração de {numero1} - {numero2} = {round(resultado, 2)}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação de {numero1} * {numero2} = {round(resultado, 2)}")
elif operador == "/":
    resultado = numero1 / numero2
    print(f"O resultado da divisão de {numero1} / {numero2} = {round(resultado, 2)}")
else:
    print(f"{operador} não é um operador, tente novamente!")