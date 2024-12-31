import tkinter

main_window = tkinter.Tk() # Janela principal, container
main_window.title("Tela inicial")
main_window.geometry("500x400+200+100") #modelo: 'largura x altura + offset(x) (deslocamento da janela em relação à esquerda) + offset(y) (deslocamento da janela em relação à margem superior da tela)'. Tudo em pixels
main_window.config(bg="#ba5857") # Definindo uma coisa de fundo para a janela
main_window.maxsize(1920,1080)  # Tamanho máximo da janela para redimensionamento
main_window.minsize(300, 100)    # Tamanho mínimo da janela para redimensionamento
main_window.resizable(False, False) # Passa dois valores boleanos. Largura True or False e Altura True or False. Ordem (altura, largura)
#main_window.state('zoomed') # Faz a janela iniciar em tela cheia. Pode não funcionar em qualquer SO
main_window.attributes('-alpha', 0.90) # Atribuir transparência à janela.
main_window.iconbitmap("image.bmp") # Adicionando um ícone à janela


main_window.mainloop() # Loop de execução para exibir a janela