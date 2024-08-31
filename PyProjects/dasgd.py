while True:
    print("[1] Cardápio \n[2] Realizar pedido \n[3] Sair do Sistema \n[0] Finalizar pedido")
    menu = int(input())
    
    if menu == 1:
        while True:
            print("[1] Pizza Grande")
            print("[2] Pizza Média")
            print("[3] Pizza Pequena")
            print("[4] Refrigerante 2 LT")
            print("[5] Refrigerante Lata")
            print("[6] Refrigerante 600 ml")
            print("[7] Hot Dog Especial")
            print("[8] Hot Dog Simples")
            print("[9] Chocolate\n")
            break
      
    elif menu == 2:
        vlr = 0
        escolha = int(input("Digite sua escolha: "))
        while escolha != 0:
            if escolha == 1:
                vlr += 65.00
            elif escolha == 2:
                vlr += 45.00
            elif escolha == 3:
                vlr += 35.00
            elif escolha == 4:
                vlr += 15.00
            elif escolha == 5:
                vlr += 6.00
            elif escolha == 6:
                vlr += 9.00
            elif escolha == 7:
                vlr += 12.00
            elif escolha == 8:
                vlr += 8.00
            elif escolha == 9:
                vlr += 5.00
            escolha = int(input("Digite sua escolha:"))
            
    elif menu == 0:
        print("Sua compra foi finalizada e deu um total de R$ ", vlr)

        print("Escolha a Forma de Pagamento!")
        print('===FORMAS DE PAGAMENTO===')
        print('[1] À VISTA DINHEIRO/CHEQUE')
        print('[2] À VISTA CARTÃO')
        print('[3] 2x NO CARTÃO')
        print('[4] 3x OU MAIS NO CARTÃO')
        opção = int(input('Qual é a opção:'))
        
        if opção == 1:
            desconto = vlr - (vlr * 0.1)
            print(f'Sua compra de R${vlr:.2f} vai custar R${desconto:.2f} no final.')
        elif opção == 2:
            print(f'Sua compra de R${vlr:.2f} vai custar R${vlr - (0.05 * vlr):.2f} no final.')
        elif opção == 3:
            print(f'Sua compra de R${vlr:.2f} vai custar R$ {vlr / 2} cada parcela.')
        elif opção == 4:
            parcelas = int(input('Quantas parcelas:'))
            vlr_final = vlr + (vlr * 0.2)
            ndp = vlr_final / parcelas
            print(f'Sua compra será parcelada em {parcelas}x de R${ndp} COM JUROS.')
            print(f'Sua compra de {vlr} vai custar R${vlr_final}')

    elif menu == 3:
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Por favor, digite uma opção válida")