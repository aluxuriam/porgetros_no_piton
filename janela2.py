import tkinter as tk
from tkinter import messagebox
 
# Função para realizar os cálculos
def calcular(operacao):
    try:
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
 
        if operacao == "soma":
            resultado = numero1 + numero2
 
        elif operacao == "subtracao":
            resultado = numero1 - numero2
 
        elif operacao == "multiplicacao":
            resultado = numero1 * numero2
 
        elif operacao == "divisao":
            if numero2 == 0:
                messagebox.showerror("Erro", "Não é possível dividir por zero!")
                return
            resultado = numero1 / numero2
 
        resultado_label.config(text=f"Resultado: {resultado}")
 
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")
 
 
# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("500x400")
 
# Título
titulo = tk.Label(
    janela,
    text="Calculadora",
    font=("Arial", 20)
)
titulo.pack(pady=20)
 
# Primeiro número
label1 = tk.Label(
    janela,
    text="Digite o primeiro número:"
)
label1.pack()
 
entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)
 
# Segundo número
label2 = tk.Label(
    janela,
    text="Digite o segundo número:"
)
label2.pack()
 
entrada2 = tk.Entry(janela)
entrada2.pack(pady=5)
 
# Botão Somar
botao_soma = tk.Button(
    janela,
    text="Calcular soma",
    command=lambda: calcular("soma")
)
botao_soma.pack(pady=5)
 
# Botão Subtrair
botao_subtracao = tk.Button(
    janela,
    text="Subtração",
    command=lambda: calcular("subtracao")
)
botao_subtracao.pack(pady=5)
 
# Botão Multiplicar
botao_multiplicacao = tk.Button(
    janela,
    text="Multiplicação",
    command=lambda: calcular("multiplicacao")
)
botao_multiplicacao.pack(pady=5)
 
# Botão Dividir
botao_divisao = tk.Button(
    janela,
    text="Divisão",
    command=lambda: calcular("divisao")
)
botao_divisao.pack(pady=5)
 
# Resultado
resultado_label = tk.Label(
    janela,
    text="Resultado:",
    font=("Arial", 14)
)
resultado_label.pack(pady=15)
 
# Iniciar o programa
janela.mainloop()