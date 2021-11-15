import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
#from Geheim import Geheim

def encrypt():
    pass


def decrypt():
    pass

fenster = tk.Tk()
fenster.title("Mein geheimes Tagebuch")

#fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

feld = tk.Canvas(fenster, width=1000, height=1000)

feld.pack(fill="both", expand=True)

purple_dreieck = feld.create_polygon(0, 0, 0, 1000, 1000, 1000, fill='darkorchid1')
royal_dreieck = feld.create_polygon(1000, 1000, 1000, 0, 0, 0, fill='royalblue1')

btn_encrypt = tk.Button(fenster, text='Encrypt', command=encrypt)
btn_decrypt = tk.Button(fenster, text='Decrypt', command=decrypt)

btn_encrypt_canvas = feld.create_window(500, 240, window=btn_encrypt)
btn_decrypt_canvas = feld.create_window(500, 300, window=btn_decrypt)


#fr_buttons.grid(row=0, column=0, sticky="ns")
text_eingabe = tk.Text(fenster)
text_eingabe.pack()#(row=0, column=1, sticky="nsew")

fenster.mainloop()
