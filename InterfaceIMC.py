#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Criar uma interface que calcule o IMC

import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    altura = float(altura_entry.get())
    peso = float(peso_entry.get())
    imc = peso / (altura * altura)
    resultado_label.config(text=f"{nome_entry.get()}, seu IMC é: {imc:.2f}")

def reiniciar():
    nome_entry.delete(0, tk.END)
    altura_entry.delete(0, tk.END)
    peso_entry.delete(0, tk.END)
    resultado_label.config(text="")

def sair():
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        janela.destroy()

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Criar e posicionar os widgets
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Endereço:").grid(row=1, column=0, padx=10, pady=10)
endereco_entry = tk.Entry(janela)
endereco_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(janela, text="Altura (m):").grid(row=2, column=0, padx=10, pady=10)
altura_entry = tk.Entry(janela)
altura_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(janela, text="Peso (kg):").grid(row=3, column=0, padx=10, pady=10)
peso_entry = tk.Entry(janela)
peso_entry.grid(row=3, column=1, padx=10, pady=10)

calcular_button = tk.Button(janela, text="Calcular", command=calcular_imc)
calcular_button.grid(row=5, column=0, pady=10)

reiniciar_button = tk.Button(janela, text="Reiniciar", command=reiniciar)
reiniciar_button.grid(row=5, column=1, pady=10)

sair_button = tk.Button(janela, text="Sair", command=sair)
sair_button.grid(row=5, column=2, pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=4, column=0, columnspan=3, pady=10)

# Iniciar o loop principal
janela.mainloop()