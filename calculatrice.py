import tkinter as tk
from typing import Text

racine = tk.Tk()

racine.title("calculatrice")

police=("helvetica","25")

label1 = tk.Label(racine, text="zone d'affichage", height="4", font = ("helvetica", "20"))
bouton1 = tk.Button(racine, width=4,text="1", font=("helvetica", "25"))
bouton2 = tk.Button(racine, width=4,text="2", font=("helvetica", "25"))
bouton3 = tk.Button(racine, width=4,text="3", font =police)
bouton4 = tk.Button(racine, width=4,text="4", font =police)
bouton5 = tk.Button(racine, width=4,text="5", font =police) #création du widget
bouton6 = tk.Button(racine, width=4,text="6", font =police)
bouton7 = tk.Button(racine, width=4,text="7", font =police)
bouton8 = tk.Button(racine, width=4,text="8", font =police)
bouton9 = tk.Button(racine, width=4,text="9", font =police)
bouton0 = tk.Button(racine, width=4,text="0", font =("helvetica","25"))

boutonplus = tk.Button(racine, width=4,text="+", font =police)
boutonmoins = tk.Button(racine, width=4,text="-", font =police)
boutonfois = tk.Button(racine, width=4,text="x", font =police)
boutondivision = tk.Button(racine, width=4,text="%", font =police)
boutonpoint = tk.Button(racine, width=4,text=".", font =police)
boutondel = tk.Button(racine, width=4,text="del", font =police)


label1.grid(column=1, columnspan= 4, row=0)
bouton1.grid(column= 1, row=1)
bouton2.grid(column= 2, row=1)
bouton3.grid(column= 3, row=1)
bouton4.grid(column= 1, row=2)
bouton5.grid(column= 2, row=2)
bouton6.grid(column= 3, row=2)
bouton7.grid(column= 1, row=3)
bouton8.grid(column= 2, row=3)
bouton9.grid(column= 3, row=3)
bouton0.grid(column= 2, row=4)

boutonplus.grid(column= 4, row=1)
boutonmoins.grid(column= 4, row=2)
boutonfois.grid(column= 4, row=3)
boutondivision.grid(column= 4, row=4)
boutonpoint.grid(column= 3, row=4)
boutondel.grid(column= 1, row=4)


racine.mainloop()

def bouton1():
    x1 = 1 
    label(Text)

def bouton2():
    x2 = 2
