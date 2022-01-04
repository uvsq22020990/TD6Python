import tkinter as tk

racine = tk.Tk()

racine.title("calculatrice")

bouton1 = tk.Button(racine, text="1", font=("helvetica", "10")) #création du widget
bouton2 = tk.Button(racine, text="2", font = ("helvetica", "10"))
bouton3 = tk.Button(racine, text="3", font = ("helvetica", "10"))
bouton4 = tk.Button(racine, text="4", font = ("helvetica", "10"))
bouton5 = tk.Button(racine, text="5", font = ("helvetica", "10")) #création du widget
bouton6 = tk.Button(racine, text="6", font = ("helvetica", "10"))
bouton7 = tk.Button(racine, text="7", font = ("helvetica", "10"))
bouton8 = tk.Button(racine, text="8", font = ("helvetica", "10"))
bouton9 = tk.Button(racine, text="9", font = ("helvetica", "10"))
bouton0 = tk.Button(racine, text="0", font = ("helvetica", "10"))

boutonplus = tk.Button(racine, text="+", font = ("helvetica", "10"))
boutonmoins = tk.Button(racine, text="-", font = ("helvetica", "10"))
boutonfois = tk.Button(racine, text="x", font = ("helvetica", "10"))
boutondivision = tk.Button(racine, text="%", font = ("helvetica", "10"))
boutonpoint = tk.Button(racine, text=".", font = ("helvetica", "10"))


bouton1.grid(column= 1, row=0)
bouton2.grid(column= 2, row=0)
bouton3.grid(column= 3, row=0)
bouton4.grid(column= 1, row=1)
bouton5.grid(column= 2, row=1)
bouton6.grid(column= 3, row=1)
bouton7.grid(column= 1, row=2)
bouton8.grid(column= 2, row=2)
bouton9.grid(column= 3, row=2)
bouton0.grid(column= 2, row=3)

boutonplus.grid(column= 4, row=0)
boutonmoins.grid(column= 4, row=1)
boutonfois.grid(column= 4, row=2)
boutondivision.grid(column= 4, row=3)
boutonpoint.grid(column= 3, row=3)


racine.mainloop()
