import os 
os.system ('cls')


from colorama import Fore, Style, init


init(autoreset= True)

frutas = ['Maçã','Uva', 'Banana', 'Laranja', 'Morango']
quantidades = [10,14,9,13,8]



nome_produto= input('Digite o nome da fruta que deseja:')


if nome_produto in frutas:
    indice = frutas.index(nome_produto)
    quantidade = quantidades [indice]


    if quantidade < 10:
        print(Fore.RED + f"O produto {nome_produto} tem {quantidade} unidades no estoque.")
    else:
      print(Fore.GREEN + f"O produto {nome_produto} tem {quantidade} unidades no estoque.")
else:
    print(Fore.YELLOW +"O produto não existe na lista." )