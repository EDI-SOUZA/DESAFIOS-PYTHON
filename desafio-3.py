"""🧩 Desafio 3 – Tabuada Automática com Validação
O programa deve:

Pedir um número para o usuário.

Mostrar a tabuada desse número de 1 a 10.

Se o usuário digitar algo que não é número, mostrar uma mensagem de erro com try/except.

Ao final, perguntar se o usuário quer fazer outra tabuada."""

while True:
    
    operacao = input("Criar nova Tabuada ou Sair? 1 - Para Tabuada 2 - Sair\n")

   
    if operacao == "2":
        print("Encerrando a calculadora. Até mais!")
        break  
    
    if operacao == "1":
        print("Certo, vamos fazer outra tabuada!")
        
        try:
            numero = float(input("Digite um número para ver a tabuada:\n"))
        except ValueError:
            print("⚠️ Você precisa digitar valores numéricos!\n")
            continue  

       
        print(f"\nTabuada de {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    
   
    if operacao not in ["1", "2"]:
        print("⚠️ Operação inválida! Tente novamente.\n")
        continue  

    
