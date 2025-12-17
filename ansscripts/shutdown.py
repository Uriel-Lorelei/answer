import tkinter as tk
import tkinter.font as tkFont
import subprocess

def shutdown_now(event):
    subprocess.run(["shutdown", "now"])

def check_ans(event=None):
    ans = entry.get()
    if ans == "5":
        label.config(text="Wow. Congrats.")
        root.after(1000, lambda: label.config(text="Bye")) #waits 1 sec
        subprocess.run(["shutdown", "now"])
    else:
        label.config(text="Not Correct.")

root = tk.Tk()
root.title("Shutdown?")
root.geometry("500x250")
root.configure(bg="#1e1e1e")
root.attributes("-topmost", True)

label_font = tkFont.Font(family="Helvetica", size=23)
# button_font = tkFont.Font(family="Helvetica", size=18)
entry_font = tkFont.Font(family="Helvetica", size=23)

label = tk.Label(root, text="Do you wish to shutdown the PC?", font=label_font, bg="#1e1e1e", fg="#DAD9CA")
label.pack(pady=20)

canvas = tk.Canvas(root, width=390, height=83, bg="#1e1e1e")
canvas.pack()
canvas.create_text(200, 25, text="Solve this equation first: ", font=("Helvetica", 18), fill="#DAD9CA")
canvas.create_text(200, 56, text="3x + 7 = 22", font=("Helvetica", 18), fill="#DAD9CA")

entry = tk.Entry(root, font=entry_font, justify="center", bg="#2e2e2e", fg="#ffffff", insertbackground="white", relief="solid", bd=2)
entry.pack(padx=20, pady=20, ipady=10)
entry.focus()
entry.bind("<Return>", check_ans)

# button = tk.Button(root, text="YES", font=button_font, bg="#5B8D72", fg="#DAD9CA")
# button.pack(padx=10, pady=8)

root.bind("y", shutdown_now)

root.mainloop()