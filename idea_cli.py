# SISTEMA DE PONTO DE VENDA (PDV) E DE GERENCIAMENTO DE FIADOS
import sqlite3

database = sqlite3.connect("EmpresaGerenciamento.db") # Criando o banco de dados EmpresaGerenciamento

handler = database.cursor() # Definindo o cursor do banco de dados

#handler.execute("CREATE TABLE produtos (produto_id, nome, preço, quantidade_estoque)") --- Tabela de produtos em estoque criada
handler.execute("CREATE TABLE clientes_fiados (cf_id, cf_nome, cf_telefone, cf_endereço, cf_total_devido)")
handler.execute("CREATE TABLE compras_clientes_fiados (cf_compra_id, descrição_compra, valor_total_compra)")
handler.execute("CREATE TABLE itens_compra ")



'''def AdicionarProdutoVenda(produtos):
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
'''
result = handler.execute("SELECT name FROM sqlite_master")
print(result.fetchone())













