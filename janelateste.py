import tkinter as tk
 
def somar():
    numero1 = float(entrada1.get())
    numero2 = float(entrada2.get())
    resultado.config(text=f"Resultado: {numero1 + numero2}")
 
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("500x400")
 
titulo = tk.Label(janela, text="Calculadora", font=("Arial", 20))
titulo.pack(pady=20)
 
tk.Label(janela, text="Digite o primeiro número:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)
 
tk.Label(janela, text="Digite o segundo número:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack(pady=5)
 
botao = tk.Button(
    janela,
    text="Calcular soma",
    command=somar
)
botao.pack(pady=15)
 
resultado = tk.Label(janela, text="Resultado:", font=("Arial", 14))
resultado.pack(pady=10)
 
janela.mainloop()