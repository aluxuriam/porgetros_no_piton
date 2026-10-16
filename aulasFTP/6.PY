import tkinter as tk

def cadastrar():
    nome=entrada1.get().strip()
    turma=entrada2.get().strip()
    idade=entrada3.get().strip()
    if nome=="" or turma=="" or idade=="":
        mensagem.config(text="Preencha todos os campos!")
        return
    try:
        idade = int(idade)
        if idade < 0:
            mensagem.config(text="Digite uma idade valida")
            return
    except ValueError:
        mensagem.config(text="Digite uma idade valida")
        return
    mensagem.config(text=f"{nome} | {turma} | {idade} anos")

janela=tk.Tk()
janela.title("Cadastro de estudante")
janela.geometry("360x280")

tk.Label(janela,text="Nome:").pack()
entrada1=tk.Entry(janela)
entrada1.pack()

tk.Label(janela,text="Turma:").pack()
entrada2=tk.Entry(janela)
entrada2.pack()

tk.Label(janela,text="Idade:").pack()
entrada3=tk.Entry(janela)
entrada3.pack()

tk.Button(janela,text="Verificar cadastro", command=cadastrar).pack(pady=12)
mensagem=tk.Label(janela, text="Resultado:")
mensagem.pack()

janela.mainloop()