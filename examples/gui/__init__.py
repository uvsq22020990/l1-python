from tkinter import * #pourquoi pas import tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk()  #création de la fonction racine

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)  #création du tableau avec dimension 
    #pourquoi pas tk.canvas

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)  #commence aux coordonnées (100,200) finit aux coord (500,200)
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50) #dessine un oval qui a pour coordonnées (50,250) et (150, 150)
    canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

    canvas.pack() #gestionnaire de position (en fonction des coordonnées)
    root.mainloop()  # Lancement de la boucle principale

"""-----------------------------------------------------------------------------------------------------"""

from tkinter import * #pourquoi pas import tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


root = Tk()  #création de la fonction racine

canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)  #création du tableau avec dimension 
#pourquoi pas tk.canvas

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
canvas.create_line(x0, y, x1, y)  #commence aux coordonnées (100,200) finit aux coord (500,200)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50) #dessine un oval qui a pour coordonnées (50,250) et (150, 150)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
# Fin de votre code

canvas.pack() #gestionnaire de position (en fonction des coordonnées)
root.mainloop()  # Lancement de la boucle principale