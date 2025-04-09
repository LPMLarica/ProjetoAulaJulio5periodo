import tkinter as tk
from tkinter import messagebox

def show_architecture():
    arch_text = """
Arquitetura da rede 802.11ac:
[Usuário] <-Wi-Fi-> [Roteador AC] <-Ethernet-> [Switch] <-Fibra-> [Backbone ISP]
    """
    messagebox.showinfo("Arquitetura de Rede", arch_text)
