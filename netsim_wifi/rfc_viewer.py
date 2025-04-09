import tkinter as tk
from tkinter import messagebox

def show_rfc():
    rfc = """
RFC 7230 - HTTP/1.1: Message Syntax and Routing

Exemplo de Header HTTP:
GET / HTTP/1.1
Host: www.exemplo.com
User-Agent: Mozilla/5.0
Accept: text/html
    """
    messagebox.showinfo("RFC e Header HTTP", rfc)
