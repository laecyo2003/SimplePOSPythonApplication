# SISTEMA DE PONTO DE VENDA (PDV) E DE GERENCIAMENTO DE FIADOS

produtos = [
    {'nome': 'Arroz', 'preco': 4.5, 'quantidade': 30},
    {'nome': 'Feijão', 'preco': 6.4, 'quantidade': 20},
    {'nome': 'Farinha de mandioca', 'preco': 3.8, 'quantidade': 10},
    {'nome': 'Biscoito', 'preco': 2.0, 'quantidade': 30},
    {'nome': 'Bolacha', 'preco': 3.0, 'quantidade': 50},
    {'nome': 'bola', 'preco': 40.0, 'quantidade': 27},
    {'nome': 'desodorante', 'preco': 5.0, 'quantidade': 10},
    {'nome': 'água', 'preco': 1.5, 'quantidade': 100},
    {'nome': 'refrigerante', 'preco': 6.0, 'quantidade': 75},
    {'nome': 'linhaça', 'preco': 8.0, 'quantidade': 23}
]
#Os produtos serão armazenados na lista produtos, onde cada produto é um dicionário e pode ser identificado pelo índice da lista
def AdicionarProdutoVenda(produtos):
    venda.append(produto)
    produto_na_venda['qtd_produto_venda'] in venda = qtd_produto_venda
    produto['quantidade'] = produto['quantidade'] - qtd_produto_venda
    valor_final_venda = valor_final_venda + produto['preco']

def RealizarVenda(produtos):
    venda = []
    valor_final_venda = 0
    print('Produtos disponíveis para venda')
    for produto in produtos:
        print(produto['nome'], '---', produto['preco'])
    opcao = int(input("1 --- Adicionar novo produto à venda\n2 --- Remover produto da venda\n3 --- Encerrar venda"))
    while opcao == 1:
        produto_venda = input("Digite o nome do produto a ser adicionado na venda: ")
        # Pegar o nome do produto inserido pelo usuário e buscar na lista de produtos.
        qtd_produto_venda = int(input("Digite a quantidade deste produto: "))
        # No mesmo produto, buscar quantidade em estoque para subtrair a quantidade da venda da quantidade em estoque
        for produto in produtos:
            if produto['nome'] == produto_venda:
                AdicionarProdutoVenda()
                venda.append(produto)
                produto_na_venda['qtd_produto_venda'] in venda = qtd_produto_venda
                produto['quantidade'] = produto['quantidade'] - qtd_produto_venda
                valor_final_venda = valor_final_venda + produto['preco']

        opcao = int(input("1 --- Adicionar novo produto à venda\n2 --- Remover produto da venda\n3 --- Encerrar venda"))
    for produto_na_venda in venda:
        print(produto_na_venda['nome'], '---', produto_na_venda['qtd_produto_venda'])
    print(f"O valor final da venda é: {valor_final_venda}")

    



def CadastrarProduto(produtos):
    produto = {
        'nome':input("Digite o nome do produto: "),
        'preco': float(input("Digite o preço do produto: ")),
        'quantidade': int(input("Digite a quantidade em estoque: "))

    }
    produtos.append(produto)
    print("Produto cadastrado!")












opcao = int(input("1 --- Realizar uma venda\n2 --- Cadastrar um produto\n3 --- Consultar Fiados\n0 --- Encerrar programa"))
if opcao == 1:
    RealizarVenda(produtos)
elif opcao == 2:
    CadastrarProduto(produtos)
elif opcao == 3:
    ConsultarFiados()
else:
    print("O programa está sendo encerrado")

