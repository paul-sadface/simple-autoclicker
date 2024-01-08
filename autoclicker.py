from pynput import keyboard, mouse
from tkinter import *
from tkinter import ttk
import time


class autoclicker():
    def __init__(self):
        self.is_running = True
        self.is_paused = True
        self.root = None
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.mouse_controller = mouse.Controller()
        

    def get_frequency(self):
        self.frequency = self.frequency_string.get()
        self.ui_feedback_label.configure(text="success")

    def create_window(self):
        self.root = Tk()
        self.root.title("Autoclicker Program")
        frame = ttk.Frame(self.root, padding=20)
        frame.grid(column=0, row=0)
        self.root.geometry("500x300")
        self.frequency_string = StringVar(self.root)

        self.ui_label = ttk.Label(frame, text="Autoclicker Program", font=15)
        self.ui_label.grid(column=0, row=0)
        self.ui_entry = ttk.Entry(frame, textvariable=self.frequency_string)
        self.ui_entry.grid(column=0, row=1, pady=30)
        self.ui_runbutton = ttk.Button(frame, text="Run", command=self.get_frequency)
        self.ui_runbutton.grid(column=0, row=2, pady=20)
        self.ui_feedback_label = ttk.Label(frame, text="", font=15)
        self.ui_feedback_label.grid(column=0, row=3, pady = 20)
        self.root.columnconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.stop_autoclicker)

        self.root.mainloop()

    def stop_autoclicker(self):
        self.root.destroy()
        self.listener.stop()
    
    def on_press(self, key):
        if key == keyboard.Key.f1:
            print("pressed f1")
            self.mouse_controller.click(mouse.Button.left, 1)
            

def main():
    main_autoclicker = autoclicker()
    main_autoclicker.listener.start()
    main_autoclicker.create_window()



if __name__ == "__main__":
    main()


