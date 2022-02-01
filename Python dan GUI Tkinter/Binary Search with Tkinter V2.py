import sys
import tkinter as tk
from tkinter import ttk


class Utama():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Binary Search GUI")
        # self.win.geometry("500x500")
        # self.win.resizable(False, False)
        self.win.eval("tk::PlaceWindow . center")
        # Lable
        self.lbl_judul = tk.Label(text="Binary Search UI Tkinter")
        self.lbl_judul.grid(column=1, row=0)
        # self.lbl_judul.pack()

        self.lbl_min = tk.Label(text="Min: ")
        self.lbl_min.grid(column=0, row=1)
        self.en_min = tk.Entry(validate='key')
        self.en_min.grid(column=1, row=1)
        self.btn_ran_min = tk.Button(text="Random Min")
        self.btn_ran_min.grid(column=2, row=1)
        self.en_min.bind("<KeyRelease>", self.cek_num)
        self.btn_ran_min.bind("<Button-1>", self.btn_min)

        self.lbl_max = tk.Label(text="Max: ")
        self.lbl_max.grid(column=0, row=2)
        self.en_max = tk.Entry()
        self.en_max.grid(column=1, row=2)
        self.btn_ran_max = tk.Button(text="Random Max")
        self.btn_ran_max.grid(column=2, row=2)
        self.en_max.bind("<KeyRelease>", self.cek_num)
        self.btn_ran_max.bind("<Button-1>", self.btn_max)

        self.lbl_guess = tk.Label(text="guess: ")
        self.lbl_guess.grid(column=0, row=3)
        self.en_guess = tk.Entry()
        self.en_guess.grid(column=1, row=3)
        self.btn_ran_guess = tk.Button(text=" Random ")
        self.btn_ran_guess.grid(column=2, row=3)
        self.en_guess.bind("<KeyRelease>", self.cek_num)
        self.btn_ran_guess.bind("<Button-1>", self.btn_ran)

        self.btn_run = tk.Button(text="Jalankan!")
        self.btn_run.grid(column=0, row=4, columnspan=3)

        # self.img = tk.Canvas(width=100, height=100)
        # self.img.create_rectangle(0, 0, 200, 100)
        # self.img.grid(column=0, row=5, columnspan=3)

        self.win.mainloop()

    def cek_num(self, event):
        pass
        # if event.keycode < 48 and event.keycode > 59:
        #     self.en_min.delete(0, tk.END)

    def btn_min(self, event):
        pass

    def btn_max(self, event):
        pass

    def btn_ran(self, event):
        pass


if __name__ == "__main__":
    Utama()
    sys.exit()
