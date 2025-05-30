import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TtkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Gambar dan Fullscreen")
        self.center_window(960, 360)

        #set otomatis layar ke fullscreen
        self.is_fullscreen = True
        self.root.attributes("-fullscreen", self.is_fullscreen) 

        # set tombol F11 untuk toggle fullscreen dan esc untuk keluar fullscreen
        self.root.bind("<F11>", self.toggle_fullscreen)

        # jalanin dan buat page mainMenu
        self.mainMenu()
    
    # set layar ke tenga monitor menyesuaikan dengan ukuran
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)

    def mainMenu(self):
        pass

    def page1(self):
        pass
    
    def TentangKamiPage(self):
        pass

    def panduanPage(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TtkinterApp(root)
    root.mainloop()