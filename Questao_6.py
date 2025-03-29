def gerenciar_lista_compras():
    lista_compras = []
    
    while True:
        print("\nOpções:")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Visualizar lista")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            item = input("Digite o nome do item: ")
            lista_compras.append(item)
            print(f"{item} adicionado à lista.")
        
        elif opcao == "2":
            item = input("Digite o nome do item a ser removido: ")
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"{item} removido da lista.")
            else:
                print("Item não encontrado na lista.")
        
        elif opcao == "3":
            print("\nLista de compras:")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
        
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

gerenciar_lista_compras()
