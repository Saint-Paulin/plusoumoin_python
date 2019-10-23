#!/bin/python3.6
import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Plus ou moins")
root.geometry("360x150+500-400")

alea = int(random.randint(0, 10))
nbrc = 0
var = tk.StringVar()
nombre = 0
# nbrc = tk.StringVar()
# nbrc.set(0)
# var.set(nbrc)
# var = ["Nombre : ", nbrc]
print(alea)
# print(var[0],var[1])
# incrnb = tk.StringVar()
# var = 0

def macmd():
    global nbrc
    global var
    #nombre = int(inputuser.get())
    #print(nombre)
    nbrc += 1
    nbrcoup.config(text=nbrc)
    inputuser.config(textvariable=var)
    var = tk.StringVar()
    try:
        nombre = int(inputuser.get())
        if nombre < alea:
            Monlabel.config(text="Perdu est plus petit que le chiffre mystère")
        elif nombre > alea:
            Monlabel.config(text="Perdu est plus grand que le chiffre mystère")
        elif nombre == alea:
            Monlabel.config(text="Gagné")
            print("ok")
            print(nombre)
    except:
        messagebox.askquestion("Warning", "Faudrait mettre un nombre abruti")

### L'espace vert :

# canvas = tk.Canvas(root, height=500, width=500, bg="green")
# canvas.pack()

### Fenêtre blanche du milieu :

# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

### Bouton :

Monbouton = tk.Button(root, text="Tester ?", padx=10, pady=5, fg="white", bg="red", command=macmd)
Monbouton.pack()
Monbouton.place(relx=0.1, rely=0.5)

### Labelframe

inputuser = tk.Entry(root, fg="black", bg="white", relief="raised")
inputuser.pack()
inputuser.place(relx=0.1, rely=0.1)

### Label

Monlabel = tk.Label(root, text="Donner un nombre", padx=10, pady=5)
Monlabel.pack()
Monlabel.place(relx=0.1, rely=0.3)

nbrcoup = tk.Label(root, text="Nombre de coup : ", padx=10, pady=5)
#nbrcoup.config(textvariable=nbrc)
nbrcoup.pack()
nbrcoup.place(relx=0.1, rely=0.8)

# "Nombre de Coup : "

### Lancement de l'application :

root.mainloop()
