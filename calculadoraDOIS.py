import tkinter as tk
import math as math
import fractions as fractions

from janela2 import calcular

def adicao(numero1, numero2):                                                               #adição
    return numero1 + numero2

def subtracao(numero1, numero2):                                                            #subtração
    return numero1 - numero2

def multiplicacao(numero1, numero2):                                                        #multiplicação
    return numero1 * numero2

def divisão (numero1, numero2):                                                             #divisão
    if numero2 == 0:
        raise ValueError("Não é possível dividir por zero.")
    return numero1 / numero2

def exponenciacao(numero1, numero2):                                                        #exponenciação
    if numero1 == 0 and numero2 < 0:
        raise ValueError("Não é possível elevar zero a um número negativo.")
    return fractions.Fraction(numero1) ** numero2

def fatorial(numero1):                                                                      #fatorial
    return math.factorial(numero1)

def porcentagem (numero1, numero2):                                                         #porcentagem
    return numero1 / 100 * numero2

def logaritmo(numero1, numero2):                                                               #logaritmo
    return math.log(numero1, numero2)

def raiz(numero1, numero2):                                                                 #raiz
    return numero1**(1/numero2)

def somatorio(numero1, numero2, funcao):                                                   #somatorio
    return sum(eval(funcao) for i in range(numero1, numero2 + 1))

def jurossimples(capital, taxa, tempo):                                                    #juros simples
    return capital * (taxa/100) * tempo

def juroscompostos(capital, taxa, tempo):                                                  #juros compostos
    return capital * (1 + taxa) ** tempo

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x640")


#inicio = True
#continuar = True
#while inicio: 
#    while continuar:
titulo = tk.Label(janela, text="Calculadora", font=("Arial", 20))
titulo.pack(pady=20)

tk.Label(janela, text="Selecione que operação deseja efetuar:").pack()

botao_adicao = tk.Button(janela,text="Adição",command=adicao)
botao_adicao.pack(pady=10)

botao_subtracao = tk.Button(janela,text="Subtração",command=subtracao)
botao_subtracao.pack(pady=10)

botao_multiplicação = tk.Button(janela,text="Multiplicação",command=multiplicacao)
botao_multiplicação.pack(pady=10)

botao_divisão = tk.Button(janela,text="Divisão",command=divisão)
botao_divisão.pack(pady=10)

botao_exponenciação = tk.Button(janela,text="Exponenciação", command=exponenciacao)
botao_exponenciação.pack(pady=10)

botao_fatorial = tk.Button(janela,text="Fatorial",command=fatorial)
botao_fatorial.pack(pady=10)

botao_porcentagem = tk.Button(janela,text="Porcentagem",command=porcentagem)
botao_porcentagem.pack(pady=10)

botao_logaritmo = tk.Button(janela,text="Logaritmo",command=logaritmo)
botao_logaritmo.pack(pady=10)

botao_raiz = tk.Button(janela,text="Raiz",command=raiz)
botao_raiz.pack(pady=10)

botao_somatorio = tk.Button(janela,text="Somatório",command=somatorio)
botao_somatorio.pack(pady=10)

botao_jurossimples = tk.Button(janela,text="Juros Simples",command=jurossimples)
botao_jurossimples.pack(pady=10)

botao_juroscompostos = tk.Button(janela,text="Juros Compostos",command=juroscompostos)
botao_juroscompostos.pack(pady=10)

#        break
#    break

janela.mainloop()