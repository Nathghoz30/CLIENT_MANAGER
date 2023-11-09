from tkinter import *
from PIL import Image, ImageTk

# Création fenetre
accueil = Tk()
accueil.title("NanoBank")
accueil.geometry("1080x720")
accueil.minsize(700, 480)
# accueil.iconbitmap("banque.ico")
accueil.config(background='#3D74C9')


# Ajout d'un titre
label_title = Label(accueil, text="Bienvenue chez NanoBank.",
                    font=("Impact, 30"), bg=('#3D74C9'), fg='#D02C1C')
label_title.place(x=30, y=25)

# Ajout sous titre
label_subtitle = Label(accueil, text="Pour accéder à votre espace, merci de vous identifier ", font=(
    "Arial, 22"), bg=('#3D74C9'), fg='white')
label_subtitle.place(x=30, y=80)