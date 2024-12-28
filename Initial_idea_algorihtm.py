produtos = [
    {'ID': '01', 'nome': 'Arroz', 'preco': 4.5, 'imagem': 'Arroz.png', 'quantidade': 30},
    {'ID': '02', 'nome': 'Feijão', 'preco': 6.4, 'imagem': 'Feijão.png', 'quantidade': 20},
    {'ID': '03', 'nome': 'Farinha de mandioca', 'preco': 3.8, 'imagem': 'farinha de mandioca.png', 'quantidade': 10},
    {'ID': '04', 'nome': 'Biscoito', 'preco': 2.0, 'imagem': 'biscoito.png', 'quantidade': 30},
    {'ID': '05', 'nome': 'Bolacha', 'preco': 3.0, 'imagem': 'bolacha.png', 'quantidade': 50},
    {'ID': '06', 'nome': 'bola', 'preco': 40.0, 'imagem': 'bola.png', 'quantidade': 27},
    {'ID': '07', 'nome': 'desodorante', 'preco': 5.0, 'imagem': 'desodorante.png', 'quantidade': 10},
    {'ID': '08', 'nome': 'água', 'preco': 1.5, 'imagem': 'agua.png', 'quantidade': 100},
    {'ID': '09', 'nome': 'refrigerante', 'preco': 6.0, 'imagem': 'refrigerante.png', 'quantidade': 75},
    {'ID': '10', 'nome': 'linhaça', 'preco': 8.0, 'imagem': 'linhaça.png', 'quantidade': 23}
]

def CadastrarProduto():
    produto = {}
    produto['ID'] = input("Digite o ID do produto: ") # deve ser único para cada produto
    produto['nome'] = input("Digite o nome do produto: ")
    produto['preco'] = float(input("Digite o preço do produto: "))
    produto['imagem'] = input("Insira uma foto do produto: ")
    produto['quantidade'] = int(input("Digite a quantidade de amostras disponíveis do produto: "))
    print (produto)

def RealizarVenda(produtos):
    print("Produtos disponíveis para a venda: ")
    for i in range(len(produtos)):
        print(f"Produto: {produtos[i]['nome']}, preço: R$ {produtos[i]['preco']:.2f} ---> Código de venda: {i}")
    lista_produtos_venda = []
    valor_total_venda = 0
    codigo_produto_na_venda = int(input("Digite o código do produto para adicioná-lo à venda. Quando terminar de adicionar todos os produtos à venda, digite -1: "))
    lista_produtos_venda.append(produtos[codigo_produto_na_venda]) # Acessar a lista produtos com todos os produtos na posição que o usuário inseriu 
    valor_total_venda = valor_total_venda + produtos[codigo_produto_na_venda]['preco']
    print(f"Produtos na venda: {lista_produtos_venda}")
    print(f"Valor total da venda: {valor_total_venda}")
    while codigo_produto_na_venda != -1:
        codigo_produto_na_venda = int(input("Digite o código do produto para adicioná-lo à vendao ou digite -1 para encerrar a venda: "))
        if codigo_produto_na_venda != -1:
            lista_produtos_venda.append(produtos[codigo_produto_na_venda]) # Acessar a lista produtos com todos os produtos na posição que o usuário inseriu 
            valor_total_venda = valor_total_venda + produtos[codigo_produto_na_venda]['preco']
        else:
            break
        print(f"Produtos na venda: {lista_produtos_venda}")
        print(f"Valor total da venda: {valor_total_venda}")
    print(f"Venda finalizada")
    print(f"Os produtos na venda são:")
    for i in range(len(lista_produtos_venda)):
          print(lista_produtos_venda[i]['nome'])
    print(f"O valor final da venda é: R$ {valor_total_venda}")
    
def ConsultarProduto(produto_objeto_da_consulta, produtos):
    for i in range(len(produtos)):
        if produto_objeto_da_consulta == produtos[i]['nome']:
            print(f"O produto {produto_objeto_da_consulta} existe no banco de dados. Estas são suas informações:")
            print(produtos[i])
    print(f"O produto {produto_objeto_da_consulta} não existe no banco de dados. Gostaria de adiconá-lo?")
    opcao = int(input("Digite 1 para adicionar o produto ao banco de dados ou 2 para encerrar a execução do programa: "))
    if opcao == 1:
        CadastrarProduto()
    else:
        print("O programa está sendo encerrado")
        

opcao = int(input("Digite 1 para Realizar uma venda\nDigite 2 para cadastrar um produto\nDigite 3 para consultar um produto: "))

if opcao == 1:
    RealizarVenda(produtos)
elif opcao == 2:
    qtd_cadastros = int(input("Digite quantos produtos você quer cadastrar: "))
    for i in range(qtd_cadastros):
        CadastrarProduto()
elif opcao == 3:
    produto_a_consultar = input("Digite o nome do produto que você deseja consultar: ")
    ConsultarProduto(produto_a_consultar, produtos)
else:
    print("Você inseriu uma opção inválida. O programa irá se encerrar.")

