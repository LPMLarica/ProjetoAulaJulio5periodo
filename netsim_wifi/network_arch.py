import tkinter as tk
from tkinter import messagebox

def show_architecture():
    arch_text = """
Arquitetura da rede 802.11ac:
[Larissa] <-Wi-Fi-> [Roteador Algar] <-Ethernet-> [Switch] <-Fibra-> [Backbone ISP]
    """
    messagebox.showinfo("Arquitetura de Rede", arch_text)
