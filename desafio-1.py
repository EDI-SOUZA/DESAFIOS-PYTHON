"""🧩 Desafio 4 – Verificador de Números Primos
O objetivo desse desafio é criar um programa que verifica se um número dado é primo ou não."""

import math

def verificar_primo(numero):
    
    if numero <= 1:
        return False
    
    
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:  
            return False
    
    return True  


while True:
    try:
        numero = int(input("Digite um número para verificar se é primo: "))
        
        if verificar_primo(numero):
            print(f"✅ O número {numero} é primo!")
        else:
            print(f"❌ O número {numero} não é primo!")
        
        continuar = input("\nDeseja verificar outro número? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa. Até mais!")
            break
    except ValueError:
        print("⚠️ Erro! Por favor, insira um número válido.\n")
