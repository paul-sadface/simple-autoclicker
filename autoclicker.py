import pyautogui
from pynput.keyboard import *
from tkinter import *
from tkinter import ttk

class autoclicker():
    def __init__(self):
        self.create_window()

    def create_window(self):
        root = Tk()
        root.title("Autoclicker Program")
        frame = ttk.Frame(root, padding=20)
        frame.grid(column=0, row=0)
        root.geometry("500x300")

        ui_label = ttk.Label(frame, text="Autoclicker Program", font=15, background="#AFE1AF")
        ui_label.grid(column=0, row=0)
        ui_entry = ttk.Entry(frame, textvariable="abc")
        ui_entry.grid(column=0, row=1, pady=50)
        ui_closebutton = ttk.Button(frame, text="Close", command=root.destroy)
        ui_closebutton.grid(column=0, row=3, pady=20)
        root.columnconfigure(0, weight=1)
        root.mainloop()



def main():
    main_autoclicker = autoclicker()


if __name__ == "__main__":
    main()


