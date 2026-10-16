import tkinter as tk

def area():
    base = float(entrada1.get())
    altura = float(entrada2.get())
    area = base * altura
    resultado.config(text=f"Area: {area:.2f}")

def perimetro():
    base = float(entrada1.get())
    altura = float(entrada2.get())
    perimetro = 2 * (base + altura)
    resultado.config(text=f"Perímetro: {perimetro:.2f}")

janela = tk.Tk()
janela.title("Area e perimetro do retangulo")
janela.geometry("360x280")

tk.Label(janela,text="Base:").pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela,text="Altura:").pack()

entrada2=tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="Calcular área", command=area).pack(pady=12)

tk.Button(janela, text="Calcular perímetro", command=perimetro).pack(pady=12)

resultado = tk.Label(janela, text="Resultado:")
resultado.pack()

janela.mainloop()