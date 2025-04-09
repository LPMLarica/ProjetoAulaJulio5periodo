import tkinter as tk
from tkinter import messagebox

def show_protocol():
    msg = """
Cliente envia:
GET /index.html HTTP/1.1
Host: www.exemplo.com

Servidor responde:
HTTP/1.1 200 OK
Content-Type: text/html

<html><body>Olá, mundo!</body></html>
    """
    messagebox.showinfo("Simulação HTTP", msg)
