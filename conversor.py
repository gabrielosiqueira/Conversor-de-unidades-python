def converter_unidades():
    print("Bem vindo ao conversor de unidades!")
    print("Escolha o tipo de conversão: ")
    print("1 - Comprimento")
    print("2 - Massa")
    print("3 - Temperatura")
    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        print("\nConversão de Comprimento:")
        print("1 - Metros para Quilômetros")
        print("2 - Quilômetros para Metros")
        print("3 - Metros para Milhas")
        print("4 - Milhas para Metros")
        opcao = input("Escolha uma opção: ")
        valor = float(input("Digite o valor:"))

        if opcao == "1":
            print(f"{valor} metros são {valor / 1000} quilômetros.")
        elif opcao == "2":
            print(f"{valor} quilômetros são {valor * 1000} metros.")
        elif opcao == "3":
            print(f"{valor} metros são {valor * 0.000621371} milhas.")
        elif opcao == "4":
            print(f"{valor} milhas são {valor / 0.000621371} metros.")
        else:
            print("Opção inválida!")

    elif escolha == "2":
        print("\nConversão de Massa:")
        print("1 - Quilogramas para Gramas")
        print("2 - Gramas para Quilogramas")
        print("3 - Quilogramas para Libras")
        print("4 - Libras para Quilogramas")
        opcao = input("Escolha uma opção: ")
        valor = float(input("Digite o valor: "))

        if opcao == "1":
            print(f"{valor} quilogramas são {valor * 1000} gramas.")
        elif opcao == "2":
            print(f"{valor} gramas são {valor / 1000} quilogramas.")
        elif opcao == "3":
            print(f"{valor} quilogramas são {valor * 2.20462} libras")
        elif opcao == "4":
            print(f"{valor} libras são {valor / 2.20462} quilogramas.")
        else:
            print("Opção inválida!")

    elif escolha == "3":
        print("\nConversão de Temperatura:")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("3 - Celsius para Kelvin")
        print("4 - Kelvin para Celsius")
        opcao = input("Escolha uma opção: ")
        valor = (float(input("Digite o valor: ")))

        if opcao == "1":
            print(f"{valor}°C são {(valor * 9/5) + 32}°F.")
        elif opcao == "2":
            print(f"{valor}°F são {(valor - 32) * 5/9}°C.")
        elif opcao == "3":
            print(f"{valor} K são {valor - 273.15}°C.")
        elif opcao == "4":
            print(f"{valor} K são {valor - 273.15}°C")
        else:
            print("Opção inválida!")
        
    else:
        print("Tipo de conversão inválido!")

converter_unidades()