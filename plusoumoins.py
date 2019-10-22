#!/bin/python
import tkinter as tk
import random

root = tk.Tk()
mystere = random.randint(0, 10)
print(mystere)

def macmd():
    nombre = inuptuser.get()
    if mystere == nombre:
        Monlabel = tk.Label(root, text="Gagné", padx=10, pady=5)
        Monlabel.pack()
        inuptuser.set(root, text="")
        print("ok")
        print(nombre)

### L'espace vert :

# canvas = tk.Canvas(root, height=500, width=500, bg="green")
# canvas.pack()

### Fenêtre blanche du milieu :

# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

### Bouton :

Monbouton = tk.Button(root, text="Je suis un bouton", padx=10, pady=5, fg="white", bg="red", command=macmd)
Monbouton.pack()

### Labelframe

inuptuser = tk.Entry(root, fg="black", bg="white")
inuptuser.pack()

### Lancement de l'application :

root.mainloop()
