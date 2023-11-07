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
        ttk.Label(frame, text="Autoclicker Program",).grid(column=0, row=0)
        ttk.Entry()
        ttk.Button(frame, text="Close", command=root.destroy).grid(column=0, row=1)
        root.mainloop()



def main():
    main_autoclicker = autoclicker()


if __name__ == "__main__":
    main()


