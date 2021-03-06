"""Module pro vykreslení GUI"""
import tkinter as tk

import api
import functions

root = tk.Tk()

IS_CLICKED_NEW_PAYMENT = False
IS_CLICKED_BILANCE = False

home_frame = tk.Frame(root)
home_frame.grid(row=0, column=0, sticky="news")


def back():
    """Funkce smaže label a entry."""
    lbl.pack_forget()
    ent.pack_forget()

    global IS_CLICKED_NEW_PAYMENT
    global IS_CLICKED_BILANCE

    IS_CLICKED_NEW_PAYMENT = False
    IS_CLICKED_BILANCE = False


def raise_frame(frame):
    """Funkce pro raise okna frame."""
    frame.tkraise()


def raise_new_payment():
    """Funkce pro zadání nové platby za tenis."""
    global IS_CLICKED_NEW_PAYMENT
    if not IS_CLICKED_NEW_PAYMENT:
        ent.config()
        ent.pack()
        IS_CLICKED_NEW_PAYMENT = True
    else:
        pass


def raise_bilance():
    """Funkce vypíše stav bilance k aktuálnímu dni."""
    global IS_CLICKED_BILANCE
    if not IS_CLICKED_BILANCE:

        dluh, dluznik, veritel = api.get_player(api.df)

        if dluh == 0:
            text_label = (
                f"Stav bilance k {functions.current_date()} \n"
                + "Nikdo nikomu nic nedluží!."
            )
        else:
            text_label = (
                f"Stav bilance k {functions.current_date()} \n"
                + f"{dluznik} dluží {veritel} {dluh} CZK."
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
ent = tk.Entry(home_frame)

root.mainloop()