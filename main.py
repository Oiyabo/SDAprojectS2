import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class TtkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project SDA")
        self.center_window(960, 360)

        self.is_fullscreen = True
        self.root.attributes("-fullscreen", self.is_fullscreen) 
        self.root.bind("<F11>", self.toggle_fullscreen)

        self.mainMenu()

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
        self.clear_frame()

        bg_image = Image.open("background.jpg")
        if bg_image.height > bg_image.width:
            bg_image = bg_image.rotate(-90, expand=True)

        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        start_button = tk.Button(self.root, text="Mulai", font=("Helvetica", 14, 'bold'), width=20, height=2, bg='#C0C0C0', fg='black', command=self.pages)
        start_button.place(relx=0.5, rely=0.68, anchor='center')

        exit_button = tk.Button(self.root, text="Keluar", font=("Helvetica", 10), bg='#C0C0C0', fg='black', command=self.root.destroy)
        exit_button.place(relx=0.5, rely=0.75, anchor='center')

    def pages(self):
        self.clear_frame()

        bg_image2 = Image.open("background2.jpg")
        if bg_image2.height > bg_image2.width:
            bg_image2 = bg_image2.rotate(-90, expand=True)

        bg_image2 = bg_image2.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image2)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        start_button = tk.Button(self.root, text="Mulai", font=("Helvetica", 25, 'bold'), width=20, height=1, bg="#00aeae", fg='#000000', command=self.pagesDua)
        start_button.place(relx=0.5, rely=0.8, anchor='center')  

        back_button = tk.Button(self.root, text="Kembali", font=("Helvetica", 13), bg='#C0C0C0', fg='black', command=self.mainMenu)
        back_button.place(relx=0.5, rely=0.88, anchor='center')

        exit_button = tk.Button(self.root, text="Keluar", font=("Helvetica", 13), bg='#C0C0C0', fg='black', command=self.root.destroy)
        exit_button.place(relx=0.5, rely=0.93, anchor='center') 

        about_button = tk.Button(self.root, text="Tentang Kami", font=("Helvetica", 12), bg='#C0C0C0', fg='black', command=self.intro)
        about_button.place(relx=0.95, rely=0.05, anchor='center')

        panduan_button = tk.Button(self.root, text="Panduan", font=("Helvetica", 12), bg='#C0C0C0', fg='black', command=self.panduan)
        panduan_button.place(relx=0.88, rely=0.05, anchor='center')

    def intro(self):
        self.clear_frame()

        image = Image.open("foto4.jpg")
        if image.height > image.width:
            image = image.rotate(-90, expand=True)

        image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.animated_text_label = tk.Label(self.root, text="", font=("Helvetica", 16), fg='white', bg='black', justify='center')
        self.animated_text_label.place(relx=0.5, rely=0.7, anchor='center')

        self.full_intro_text = (
            "Halo!\n"
            "Selamat datang di aplikasi kami, Kelompok 10.\n"
            "Anggota kami adalah:\n"
            "M. Faris Adithya, Maulana Ramadhan, Keisha Aurel Ratu Assyifa, Palwa Abiyyu Jaya."
        )
        self.text_index = 0
        self.animate_text()

        back_button = tk.Button(self.root, text="Kembali", font=("Helvetica", 12), bg='#C0C0C0', fg='black', command=self.pages)
        back_button.place(relx=0.5, rely=0.88, anchor='center')

    def animate_text(self):
        if self.text_index < len(self.full_intro_text):
            current_text = self.full_intro_text[:self.text_index + 1]
            self.animated_text_label.config(text=current_text)
            self.text_index += 1
            self.root.after(40, self.animate_text)

    def panduan(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg='#000000')
        frame.pack(expand=True)

    def pagesDua(self):
        self.clear_frame()
        frame = tk.Frame(self.root, bg='#000000')
        frame.pack(expand=True)

        btn_intro = tk.Button(frame, text="Pengenalan", command=self.intro, font=("Helvetica", 15), width=15, height=2, fg='#000000', bg='#D3D3D3')
        btn_intro.place(relx=0.5, rely=0.4, anchor='center')
            
        btn_sb = tk.Button(frame, text="Score Board", command=None, font=("Helvetica", 15), width=15, height=2, fg='#000000', bg='#D3D3D3')
        btn_sb.place(relx=0.5, rely=0.5, anchor='center')
        
        btn_back = tk.Button(frame, text="Kembali", command=self.mainMenu, font=("Helvetica", 12), width=10, fg='#FFFFFF', bg='#8B0000')
        btn_back.place(relx=0.5, rely=0.6, anchor='center')


if __name__ == "__main__":
    root = tk.Tk()
    app = TtkinterApp(root)
    root.mainloop()
