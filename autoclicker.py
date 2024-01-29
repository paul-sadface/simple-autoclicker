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
        self.delay = None
        

    def get_delay(self):
        try:
            self.delay = self.delay_string.get()
            self.ui_feedback_label.configure(text="success")
        except ValueError:
            self.ui_feedback_label.configure(text="invalid input")

    def toggle_autoclicker(self):
        self.is_paused = not self.is_paused
        if self.is_paused == True:
            self.ui_paused.configure(text="paused")
        else:
            self.ui_paused.configure(text="running")

        while self.is_paused == False:
            self.autoclick()
            time.sleep(int(self.delay))

    def autoclick(self):
        if self.is_paused == False:
            self.mouse_controller.click(mouse.Button.left, count=1)


    def create_window(self):
        self.root = Tk()
        self.root.title("Autoclicker Program")
        frame = ttk.Frame(self.root, padding=20)
        frame.grid(column=0, row=0)
        self.root.geometry("500x300")
        self.delay_string = StringVar(self.root)

        self.ui_label = ttk.Label(frame, text="Autoclicker Program", font=15)
        self.ui_label.grid(column=0, row=0)
        self.ui_entry = ttk.Entry(frame, textvariable=self.delay_string)
        self.ui_entry.grid(column=0, row=1, pady=30)
        self.ui_runbutton = ttk.Button(frame, text="Set Delay", command=self.get_delay)
        self.ui_runbutton.grid(column=0, row=2, pady=20)
        self.ui_feedback_label = ttk.Label(frame, text="", font=15)
        self.ui_feedback_label.grid(column=0, row=3, pady = 10)
        self.ui_paused = ttk.Label(frame, text="paused", font=15)
        self.ui_paused.grid(column=0, row=4)
        self.root.columnconfigure(0, weight=1)
        self.root.protocol("WM_DELETE_WINDOW", self.stop_autoclicker)

        self.root.mainloop()

    def stop_autoclicker(self):
        self.root.destroy()
        self.listener.stop()
    
    def on_press(self, key):
        if key == keyboard.Key.f9:
            self.toggle_autoclicker()
            

def main():
    main_autoclicker = autoclicker()
    main_autoclicker.listener.start()
    main_autoclicker.create_window()



if __name__ == "__main__":
    main()


