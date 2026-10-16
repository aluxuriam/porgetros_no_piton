import tkinter as tk

def ctof():
    celsius = float(entrada.get())
    tahrenheit = (celsius * 1.8) + 32
    resultado.config(text=f"{tahrenheit:.1f}°F")

def ftoc():
    fahrenheit = float(entrada.get())
    celsius = (fahrenheit - 32) / 1.8
    resultado.config(text=f"{celsius:.1f}°C")

janela = tk.Tk()
janela.title("Conversor de temperatura")
janela.geometry("380x240")

tk.Label(janela, text="Temperatura (°C ou °F):").pack()
entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Celsius para Fahrenheit", command=ctof).pack(pady=12)
tk.Button(janela, text="Fahrenheit para Celsius", command=ftoc).pack(pady=12)
resultado = tk.Label(janela, text="Resultado:")
resultado.pack()

janela.mainloop()