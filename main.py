from boot.boot_screen import boot_screen
from gui.gui import PythonOSGUI
import tkinter as tk

if __name__ == "__main__":
    # Boot screen first
    boot_screen()

    # Then start GUI
    root = tk.Tk()
    app = PythonOSGUI(root)
    root.mainloop()
