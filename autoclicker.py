import pyautogui
from pynput.keyboard import *
from tkinter import *
from tkinter import ttk
import time


class autoclicker():
    def __init__(self):
        self.create_window()

    def get_frequency(self):

        print(self.frequency_string.get())

    def create_window(self):
        root = Tk()
        root.title("Autoclicker Program")
        frame = ttk.Frame(root, padding=20)
        frame.grid(column=0, row=0)
        root.geometry("500x300")
        self.frequency_string = StringVar(root)

        self.ui_label = ttk.Label(frame, text="Autoclicker Program", font=15, background="#AFE1AF")
        self.ui_label.grid(column=0, row=0)
        self.ui_entry = ttk.Entry(frame, textvariable=self.frequency_string)
        self.ui_entry.grid(column=0, row=1, pady=50)
        self.ui_runbutton = ttk.Button(frame, text="Run", command=self.get_frequency)
        self.ui_runbutton.grid(column=0, row=3, pady=20)
        root.columnconfigure(0, weight=1)

        root.mainloop()


    
def main():
    main_autoclicker = autoclicker()




if __name__ == "__main__":
    main()


