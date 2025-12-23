#!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkFont
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application
)

def calculate():
    expr = entry.get()
    try:
        result = parse_expr(expr, transformations=standard_transformations)
        result_label.config(text=f"Result: {result}") #immediately replaces the default Result: this through.config. Meaning it replaces the result_label text
        entry.delete(0, tk.END) # removes the input from the entry box after calculating
    except Exception:
        result_label.config(text="Invalid Expression")

root = tk.Tk() #required at the start for gui
root.title("Meowculator")  #title of the app
root.geometry("500x200")
root.configure(bg="#1e1e1e") #bg of the app
root.attributes("-topmost", True)  # Always on top of other apps
root.attributes("-alpha", 0.95)    # Slight transparency

# Fonts
entry_font = tkFont.Font(family="Helvetica", size=38)  #entry font for the size of the box
label_font = tkFont.Font(family="Helvetica", size=20) #size of the result

# Entry Box
entry = tk.Entry(root, font=entry_font, justify="center", bg="#2e2e2e", fg="#ffffff", insertbackground="white", relief="solid", bd=2)
entry.pack(padx=20, pady=20, ipady=10)
entry.focus()
entry.bind("<Return>", lambda event: calculate()) #sends the input to function

result_label = tk.Label(root, text="Result: ", font=label_font, bg="#1e1e1e", fg="#CCABA9")
result_label.pack(pady=10)

root.mainloop() #w/o this the gui wont show