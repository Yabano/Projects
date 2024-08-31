from os import system

system("cls")

valor_pedido = 0

while True:
    print("Opções:")
    print("[1] Cardápio | [2] Realizar pedido | [3] Sair do Sistema | [0] Finalizar pedido")
    menu = int(input())
    
    if menu == 1:
            system("cls")
            print("Cardápio:")
            print("[1] Pizza Grande\n[2] Pizza Média\n[3] Pizza Pequena\n[4] Refrigerante 2 LT\n")
            print("[5] Refrigerante Lata\n[7] Hot Dog Especial\n[8] Hot Dog Simples\n[9] Chocolate\n")
      
    elif menu == 2:
        
        while True:
            escolha = int(input("Digite sua escolha: "))
            
            if escolha == 1: valor_pedido += 65.00

            elif escolha == 2: valor_pedido += 45.00

            elif escolha == 3: valor_pedido += 35.00

            elif escolha == 4: valor_pedido += 15.00

            elif escolha == 5: valor_pedido += 6.00

            elif escolha == 6: valor_pedido += 9.00

            elif escolha == 7: valor_pedido += 12.00

            elif escolha == 8: valor_pedido += 8.00

            elif escolha == 9: valor_pedido += 5.00
            
            else: break
        system("cls")
            
    elif menu == 0:
        system("cls")
        print(f"Sua compra foi finalizada e deu um total de R$ {valor_pedido}\n")
        print("===FORMAS DE PAGAMENTO===")
        print("[1] À VISTA DINHEIRO/CHEQUE | [2] À VISTA CARTÃO | [3] 2x NO CARTÃO | [4] 3x OU MAIS NO CARTÃO\n")
        opção = int(input("Qual é a opção: "))
        
        if opção == 1:
            desconto = valor_pedido - (valor_pedido * 0.1)
            print(f"\nSua compra de R${valor_pedido:.2f} vai custar R${desconto:.2f} no final.\n")
            
        
        elif opção == 2: 
            print(f"Sua compra de R${valor_pedido:.2f} vai custar R${valor_pedido - (0.05 * valor_pedido):.2f} no final.") 
            

        elif opção == 3: 
            print(f"Sua compra de R${valor_pedido:.2f} vai custar R$ {valor_pedido / 2} cada parcela.")
            

        elif opção == 4:
            parcelas = int(input("Quantas parcelas: "))
            valor_final = valor_pedido + (valor_pedido * 0.2)
            ndp = valor_final / parcelas
            print(f"\nSua compra será parcelada em {parcelas}x de R${ndp} COM JUROS.")
            print(f"\nSua compra de {valor_pedido} vai custar R${valor_final}")
            
        break
    elif menu == 3:
        print("Saindo do sistema...")
        break
        
    else:
        system("cls")
        print("Opção inválida. Por favor, digite uma opção válida")