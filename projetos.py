def menu():
    print("\n---Menu---")
    print("1 - Soma")
    print("0 - Sair")
    return int(input(">>"))

def soma():
    a = int(input("Digite um numero: "))
    b = int(input("Digite outro numero: "))
    return a+b

while True:
    opcao = menu()
    
    if opcao == 0:
        print("Encerrando o programa...")
        break
    
    elif opcao == 1:
        print("Resultado: ", soma())
    
    else:
        print("Opção inválida")

