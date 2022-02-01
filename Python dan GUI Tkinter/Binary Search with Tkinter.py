import sys
import tkinter as tk


class Utama():
    def __init__(self):
        count = 0
        high = 1000
        low = 0
        guess = 500

        self.win = tk.Tk()
        self.win.geometry("500x300")
        self.win.title("Ekspertiment Tkinter")
        self.win.eval("tk::PlaceWindow . center")

        while low <= high:
            mid = (low+high)//2
            count += 1

            self.lbl_low = tk.Label(text="Low: ", width="15", height=3)
            self.lbl_low.grid(column=0, row=0)
            self.lbl_low1 = tk.Label(text=low, width="15")
            self.lbl_low1.grid(column=1, row=0)

            self.lbl_high = tk.Label(text="High: ", width="15")
            self.lbl_high.grid(column=2, row=0)
            self.lbl_high1 = tk.Label(text=high, width="15")
            self.lbl_high1.grid(column=3, row=0)

            self.lbl_count = tk.Label(text="Percobaan Ke: ")
            self.lbl_count.grid(column=0, row=count+1)
            self.lbl_count1 = tk.Label(text=count)
            self.lbl_count1.grid(column=1, row=count+1)

            self.lbl_mid = tk.Label(text="Hasil: ")
            self.lbl_mid.grid(column=2, row=count+1)
            self.lbl_mid1 = tk.Label(text=mid)
            self.lbl_mid1.grid(column=3, row=count+1)
            print("Percobaan Ke: ", count, "Hasil: ", mid)
            if mid == guess:
                self.lbl_benar = tk.Label(text="Tebakan Benar: ", height=3)
                self.lbl_benar.grid(column=0, row=count+2)
                self.lbl_benar1 = tk.Label(text=mid)
                self.lbl_benar1.grid(column=1, row=count+2)
                print("Tebakan Benar: ", mid)
                break
            if mid > guess:
                high = mid - 1
                print("Guess: ", guess)
            else:
                low = mid + 1
        self.Null = tk.Label(text="Proses Selesai")
        self.Null.grid(column=3, row=count+2)
        # print("Jawaban Ga Ada")

        self.win.mainloop()


if __name__ == "__main__":
    Utama()
    sys.exit()
