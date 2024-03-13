import tkinter as tk
from tkinter import ttk
from pynput.mouse import Controller, Button
from threading import Thread, Lock
import time

class AutoRobloxGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Roblox Automation Tool")
        self.root.geometry("600x400")  # Landscape orientation window
        
        # Ensure the application window captures key presses
        self.root.focus_set()
        self.root.bind('<f>', self.toggle_auto_clicker)
        
        self.mouse = Controller()
        self.auto_clicker_status = False
        self.auto_egg_opener_status = False
        self.toggle_lock = Lock()
        self.last_toggle_time = time.time()
        self.toggle_delay = 0.5  # 0.5 second delay to prevent instant toggle off

        # Tab and widget setup...

    def auto_clicker_function(self):
        while self.auto_clicker_status:
            self.mouse.click(Button.left, 1)
            time.sleep(1.0 / self.cps_var.get())

    def toggle_auto_clicker(self, event=None):
        current_time = time.time()
        if current_time - self.last_toggle_time < self.toggle_delay:
            return  # Ignore toggle if within the cooldown period
        
        with self.toggle_lock:  # Ensure thread-safe toggling
            self.auto_clicker_status = not self.auto_clicker_status
            self.last_toggle_time = current_time

        if self.auto_clicker_status:
            self.auto_clicker_btn.configure(bg=self.toggle_on_color)
            Thread(target=self.auto_clicker_function, daemon=True).start()  # Daemon thread will close with the app
        else:
            self.auto_clicker_btn.configure(bg=self.toggle_off_color)

    # Additional methods...

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoRobloxGUI(root)
    root.mainloop()
