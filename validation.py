# Validação de entrada do usuário
def RealizarNovaVenda():
    print("Uma nova venda é realizada aqui")

def CadastrarProduto():
    print("Um novo produto é cadastrado aqui")

def ConsultarFiados():
    print("Os fiados são consultados aqui")

def EncerrarPrograma():
    breakpoint

def ObterEntradaUsuario():
    entrada_usuario = input(f"1 --- Realizar nova venda\n2 --- Cadastrar produto\n3 --- Consultar fiados\n0 --- Encerrar o programa\n")
    entrada_usuario = ValidarEntradaUsuarioContraString(entrada_usuario)
    entrada_usuario = ValidarEntradaUsuarioEscopoPrograma(entrada_usuario)
    entrada_usuario = int(entrada_usuario)
    return entrada_usuario

def ValidarEntradaUsuarioContraString(entrada_usuario):
    if (entrada_usuario < '0') or (entrada_usuario > '9'):
        while (entrada_usuario < '0') or (entrada_usuario > '9'):
            entrada_usuario = input(f"Você não inseriu um valor numérico. Você deve inserir um valor numérico entre 0 e 9: " )
    
    return entrada_usuario


def ValidarEntradaUsuarioEscopoPrograma(entrada_usuario):
    while(entrada_usuario != '1') and (entrada_usuario != '2') and (entrada_usuario != '3') and (entrada_usuario != '0'):
        entrada_usuario = input("Você inseriu uma opção inválida!\nPor favor, insira uma das seguintes opções:\n1 --- Realizar nova venda\n2 --- Cadastrar produto\n3 --- Consultar fiados\n0 --- Encerrar o programa\n")
        entrada_usuario = ValidarEntradaUsuarioContraString(entrada_usuario)
    return entrada_usuario
    

opcao = ObterEntradaUsuario()
if opcao == 1:
    RealizarNovaVenda()
elif opcao == 2:
    CadastrarProduto()
elif opcao == 3:
    ConsultarFiados()

elif opcao == 0: 
    EncerrarPrograma()

