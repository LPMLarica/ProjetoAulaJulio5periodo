import tkinter as tk
from tkinter import ttk
from network_arch import show_architecture
from tools import show_tools
from arp_simulator import show_arp
from protocol_app import show_protocol
from rfc_viewer import show_rfc

def main():
    root = tk.Tk()
    root.title("NetSim Wi-Fi Explorer")
    root.geometry("400x400")

    label = ttk.Label(root, text="NetSim Wi-Fi Explorer", font=("Arial", 18))
    label.pack(pady=20)

    ttk.Button(root, text="Desenho da Arquitetura", command=show_architecture).pack(pady=5)
    ttk.Button(root, text="Ferramentas de Rede", command=show_tools).pack(pady=5)
    ttk.Button(root, text="Simulação Tabela ARP", command=show_arp).pack(pady=5)
    ttk.Button(root, text="Protocolo HTTP (Camada Aplicação)", command=show_protocol).pack(pady=5)
    ttk.Button(root, text="RFC + Header", command=show_rfc).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
