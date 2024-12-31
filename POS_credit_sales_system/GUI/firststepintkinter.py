import tkinter

window = tkinter.Tk() # Instanciando uma janela
window.title("My first app")
window.geometry("300x100+30+30")

label_message =  tkinter.Label(window, text="This is my first app!") # Criando e posicionando um label, um widget
label_message.pack()

window.mainloop() # Loop para exibir a janela na tela

