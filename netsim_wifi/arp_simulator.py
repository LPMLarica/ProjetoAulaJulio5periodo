import tkinter as tk
from tkinter import messagebox

def show_arp():
    table = """
Tabela ARP Simulada:
IP: 192.168.0.2 -> MAC: A0:B1:C2:D3:E4:F5
IP: 192.168.0.3 -> MAC: A1:B2:C3:D4:E5:F6
    """
    messagebox.showinfo("Tabela ARP", table)
