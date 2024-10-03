import tkinter as tk
windows = tk.Tk()
contador = 0
w= tk.Message(
    text="Juego",
    fg="black",
    anchor="center",
    width=70,
    cursor=""
)

menu=tk.Button(
    text="Opcion 1",
    fg="black",
    bg="white",
    width=20,
    height=5
)
menu2=tk.Button(
    text="Opcion 2",
    fg="black",
    bg="white",
    width=20,
    height=5
)
menu3=tk.Button(
    text="Opcion 3",
    fg="black",
    bg="white",
    width=20,
    height=5
)
menu4=tk.Button(
    text="Opcion 4",
    fg="black",
    bg="white",
    width=20,
    height=5
)
texto=tk.Menubutton(
    text="OPCION 1 o OPCION 2 o OPCION 3 o OPCION 4.",
    fg="black",
    width=70,
    height=12
)
w.pack()
texto.pack(anchor="center")
menu4.pack(side="right")
menu3.pack(side="right")
menu2.pack(side="right")
menu.pack()
windows.mainloop()

