import tkinter as tk

class GUI:
    def __init__(self):
        self.fenster = tk.Tk()
        self.fenster.configure(background = "black")
        self.fenster.attributes("-fullscreen", True)
        self.fenster.mainloop()
        self.main = tk.Frame()

    def set_time(self,hour,minute):
            return
