#!/bin/python3.6
import tkinter as tk
import random

root = tk.Tk()
root.title("Plus ou moins")
root.geometry("360x150+500-400")

alea = random.randint(0, 10)
nbrc = 0
var = tk.StringVar()
# nbrc = tk.StringVar()
# nbrc.set(0)
# var.set(nbrc)
# var = ["Nombre : ", nbrc]
print(alea)
# print(var[0],var[1])
# incrnb = tk.StringVar()
#var = 0

def macmd():
    global nbrc
    global var
    nombre = int(inputuser.get())
    print(nombre)
    Monlabel.config(text="Tester")
    nbrc += 1
    nbrcoup.config(text=nbrc)
    # inputuser.delete(first)
    inputuser.config(textvariable=var)
    var = tk.StringVar()
    # inputuser.config(bg="black", fg="white") # ça fonctionne mais impossible de supprimer le chiffre avec text=""
    if nombre < alea:
        Monlabel.config(text="Perdu est plus petit que le chiffre mystère")
    elif nombre > alea:
        Monlabel.config(text="Perdu est plus grand que le chiffre mystère")
    elif nombre == alea:
        Monlabel.config(text="Gagné")
        print("ok")
        print(nombre)
    elif nombre == "":
        Monlabel.config(text="Rien")
		#tk_messageBox -message "Vous n'avez rien mis !" -icon error -type ok -title "Erreur !"
    # else:
    #     print("ko")
    #     Monlabel.config(text="Perdu")

### L'espace vert :

# canvas = tk.Canvas(root, height=500, width=500, bg="green")
# canvas.pack()

### Fenêtre blanche du milieu :

# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

### Bouton :

Monbouton = tk.Button(root, text="Tester ?", padx=10, pady=5, fg="white", bg="red", command=macmd)
Monbouton.pack()
Monbouton.place(x=30, y=95)

### Labelframe

inputuser = tk.Entry(root, fg="black", bg="white")
inputuser.pack()
Monbouton.place(x=15, y=15)

### Label

Monlabel = tk.Label(root, text="Tester", padx=10, pady=5)
Monlabel.pack()
Monbouton.place(x=210, y=11)

nbrcoup = tk.Label(root, text="Nombre de coup : ", padx=10, pady=5)
#nbrcoup.config(textvariable=nbrc)
nbrcoup.pack()
Monbouton.place(x=15, y=120)

# "Nombre de Coup : "

### Lancement de l'application :

root.mainloop()
