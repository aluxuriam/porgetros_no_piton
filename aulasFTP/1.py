import tkinter as tk

def calcular_media():
    nota1 = (entrada1.get())
    nota2 = (entrada2.get())
    nota3 = (entrada3.get())
    nota4 = (entrada4.get())
    
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        nota4 = float(nota4)
    except ValueError:
        resultado.config(text="Digite notas validas!")
        return
      
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    if media >= 6:
        resultado.config(text=f"Média: {media:.2f} - Aprovado")
    else:
        resultado.config(text=f"Média: {media:.2f} - Reprovado")

janela = tk.Tk()
janela.title("Boletim de Notas")
janela.geometry("350x400")

texto1 = tk.Label(janela, text="digite a primeira nota:")
texto1.pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack(pady=5)

texto2 = tk.Label(janela, text="digite a segunda nota:")
texto2.pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack(pady=5)

texto3 = tk.Label(janela, text="digite a terceira nota:")
texto3.pack(pady=5)
entrada3 = tk.Entry(janela)
entrada3.pack(pady=5)

texto4 = tk.Label(janela, text="digite a quarta nota:")
texto4.pack(pady=5)
entrada4 = tk.Entry(janela)
entrada4.pack(pady=5)

botao = tk.Button(janela, text="Verificar Média", command=calcular_media)
botao.pack(pady=20)

resultado = tk.Label(janela, text="Média: ")
resultado.pack(pady=5)

janela.mainloop()
