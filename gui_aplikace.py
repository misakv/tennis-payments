"""Module pro vykreslení GUI"""

import tkinter as tk
import functions

root = tk.Tk()

IS_CLICKED_NEW_PAYMENT = False
IS_CLICKED_BILANCE = False

home_frame = tk.Frame(root)
home_frame.grid(row=0, column=0, sticky="news")


def back():
    """I would like to this function to clean everything."""
    lbl.pack_forget()


def raise_frame(frame):
    """Funkce pro raise okna frame."""
    frame.tkraise()


def raise_new_payment():
    """Funkce pro zadání nové platby za tenis."""
    global IS_CLICKED_NEW_PAYMENT
    if not IS_CLICKED_NEW_PAYMENT:
        tk.Entry().grid()
        IS_CLICKED_NEW_PAYMENT = True
    else:
        pass


def raise_bilance():
    """Funkce vypíše stav bilance k aktuálnímu dni."""
    global IS_CLICKED_BILANCE
    if not IS_CLICKED_BILANCE:
        text_label = (
            f"Stav bilance k {functions.current_date()} \n"
            + "Marek dluží Vojtovi $1.000.000"
        )

        lbl.config(text=text_label)
        lbl.pack()
        IS_CLICKED_BILANCE = True
    else:
        pass


bilance = tk.Button(
    home_frame, text="Zjistí stav tenisové bilance", command=lambda: raise_bilance()
)
bilance.pack(pady=10)

platba = tk.Button(
    home_frame,
    text="Zadej novou platbu",
    command=lambda: raise_new_payment(),
)
platba.pack(pady=10)

zpet = tk.Button(
    home_frame,
    text="Zpět",
    command=back,
)
zpet.pack(pady=10)


raise_frame(home_frame)

lbl = tk.Label(home_frame)


root.mainloop()