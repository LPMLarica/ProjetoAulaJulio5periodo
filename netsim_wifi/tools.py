import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except:
        return "Erro ao executar o comando."

def show_tools():
    root = tk.Toplevel()
    root.title("Ferramentas de Rede")

    def executar_ping():
        host = simpledialog.askstring("Ping", "Digite o host:")
        output = run_command(f"ping -n 4 {host}")
        messagebox.showinfo("Ping", output)

    def executar_tracert():
        host = simpledialog.askstring("Tracert", "Digite o host:")
        output = run_command(f"tracert {host}")
        messagebox.showinfo("Tracert", output)

    def executar_netstat():
        output = run_command("netstat -an")
        messagebox.showinfo("Netstat", output)

    tk.Button(root, text="Ping", command=executar_ping).pack(pady=5)
    tk.Button(root, text="Tracert", command=executar_tracert).pack(pady=5)
    tk.Button(root, text="Netstat", command=executar_netstat).pack(pady=5)
