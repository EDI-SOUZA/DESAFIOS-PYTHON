"""🧩 Desafio 2 – Mini Calculadora
Faça um programa que:

Peça dois números ao usuário.

Peça qual operação ele quer fazer: +, -, * ou /.

Mostre o resultado da operação com uma mensagem bonita."""


print("-----------------------------------------------")
print("-----------------CALCULADORA-------------------")
print("-----------------------------------------------\n")

while True:
    operacao = input("Qual operação deseja realizar?\nDigite:\n1 - Para Soma\n2 - Para Subtração\n3 - Para Multiplicação\n4 - Para Divisão\nOu Sair para encerrar:\n")

    if operacao.lower() == "sair":
        print("Encerrando a calculadora. Até mais!")
        break

    if operacao not in ["1", "2", "3", "4"]:
        print("⚠️ Operação inválida! Tente novamente.\n")
        continue

    try:
        primeiro_numero = float(input("Informe o primeiro número: "))
        segundo_numero = float(input("Informe o segundo número: "))
    except ValueError:
        print("⚠️ Você precisa digitar valores numéricos!\n")
        continue

    if operacao == "1":
        resultado = primeiro_numero + segundo_numero
        print(f"✅ {primeiro_numero} + {segundo_numero} = {resultado}\n")
    elif operacao == "2":
        resultado = primeiro_numero - segundo_numero
        print(f"✅ {primeiro_numero} - {segundo_numero} = {resultado}\n")
    elif operacao == "3":
        resultado = primeiro_numero * segundo_numero
        print(f"✅ {primeiro_numero} x {segundo_numero} = {resultado}\n")
    elif operacao == "4":
        if segundo_numero == 0:
            print("⚠️ Não é possível dividir por zero!\n")
        else:
            resultado = primeiro_numero / segundo_numero
            print(f"✅ {primeiro_numero} ÷ {segundo_numero} = {resultado}\n")
