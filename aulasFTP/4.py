import tkinter as tk

def precofinal():
    valor =float(entrada1.get())
    percentual =float(entrada2.get())
    desconto=valor*percentual/100
    final=valor-desconto
    resultado1.config(text=f"Preço final: R$ {final:.2f}")

def desconto():
    valor =float(entrada1.get())
    percentual=float(entrada2.get())
    desconto=valor* percentual/ 100
    resultado2.config(text=f"Desconto: R$ {desconto:.2f}")

janela=tk.Tk()
janela.title("Calculadora de desconto")
janela.geometry("380x230")

tk.Label(janela, text="Preço(R$):").pack()
entrada1=tk.Entry(janela)
entrada1.pack()

tk.Label(janela,text="Desconto(%):").pack()
entrada2=tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="Preço final", command=precofinal).pack(pady=12)

tk.Button(janela, text="Desconto", command=desconto).pack(pady=5)

resultado1=tk.Label(janela, text="Resultado:")
resultado1.pack()

resultado2=tk.Label(janela, text=" ")
resultado2.pack()

janela.mainloop()