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

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mainMenu(self):
        pass

    def pages(self):
        self.clear_frame()
        bg_image2 = Image.open("background2.jpg")

        if bg_image2.height > bg_image2.width:
            bg_image2 = bg_image2.rotate(-90, expand=True)

        bg_image2 = bg_image2.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image2)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        start_button = tk.Button(self.root, text="Mulai", font=("Helvetica", 25, 'bold'), width=20, height=1, bg="#00aeae", fg='#000000', command=self.pages)
        start_button.place(relx=0.5, rely=0.8, anchor='center')  # Sesuaikan rely

        back_button = tk.Button(self.root,text="Kembali", font=("Helvetica", 13), bg='#C0C0C0', fg='black', command=self.main_menu)
        back_button.place(relx=0.5, rely=0.88, anchor='center')

        exit_button = tk.Button(self.root,text="Keluar", font=("Helvetica", 13), bg='#C0C0C0', fg='black', command=self.root.destroy)
        exit_button.place(relx=0.5, rely=0.93, anchor='center')  # Sesuaikan rely

        about_button = tk.Button(self.root,text="Tentang kami", font=("Helvetica", 12), bg='#C0C0C0', fg='black', command=self.intro)
        about_button.place(relx=0.95, rely=0.05, anchor='center')

        panduan_button = tk.Button(self.root,text="panduan", font=("Helvetica", 12), bg='#C0C0C0', fg='black', command=self.panduan)
        panduan_button.place(relx=0.88, rely=0.05, anchor='center')
    
    def TentangKamiPage(self):
        pass

    def panduanPage(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TtkinterApp(root)
    root.mainloop()
