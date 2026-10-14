import tkinter as tk

def dobro():
    valor = float(entrada.get())
    resultado1.config(text=f" Dobro: {valor * 2}")
def triplo():
    valor = float(entrada.get())
    resultado2.config(text=f" Triplo: {valor * 3}")

janela = tk.Tk()
janela.title("Dobro e Triplo")
janela.geometry("350x250")

texto = tk.Label(janela, text="número:")
texto.pack(pady=5)
entrada = tk.Entry(janela)
entrada.pack(pady=5)

botao1 = tk.Button(janela, text="dobro", command=dobro)
botao1.pack(pady=10) 

botao2 = tk.Button(janela, text="triplo", command=triplo)
botao2.pack(pady=10) 

resultado1 = tk.Label(janela, text=" ")
resultado1.pack(pady=5)

resultado2 = tk.Label(janela, text=" ")
resultado2.pack(pady=5)

janela.mainloop()