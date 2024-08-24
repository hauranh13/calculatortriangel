import tkinter as tk
from tkinter import messagebox

class TriangleAreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Mario Triangle Area Calculator")
        
        # Mengatur ukuran jendela utama
        self.root.geometry("400x300")  # Mengatur ukuran window

        # Mengatur warna latar belakang (biru langit)
        self.canvas = tk.Canvas(root, width=400, height=300, bg='#87CEEB', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Mengatur font yang mirip dengan Super Mario
        label_font = ('Arial Black', 14, 'bold')
        entry_font = ('Arial Black', 14)
        button_font = ('Arial Black', 14, 'bold')

        # Menambahkan frame transparan untuk meletakkan widget di atas Canvas
        self.frame = tk.Frame(self.canvas, bg='#87CEEB')
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # LabelFrame untuk Alas
        self.label_alas_frame = tk.LabelFrame(self.frame, text="Masukkan Alas Segitiga:", font=label_font, fg='#FFFFFF', bg='#87CEEB', labelanchor='n', padx=10, pady=5, relief='solid', bd=2)
        self.label_alas_frame.pack(pady=10)
        
        # Entry untuk Alas
        self.entry_alas = tk.Entry(self.label_alas_frame, font=entry_font, width=15, bd=2, relief="solid", justify="center", bg='#FFD700')
        self.entry_alas.pack()

        # LabelFrame untuk Tinggi
        self.label_tinggi_frame = tk.LabelFrame(self.frame, text="Masukkan Tinggi Segitiga:", font=label_font, fg='#FFFFFF', bg='#87CEEB', labelanchor='n', padx=10, pady=5, relief='solid', bd=2)
        self.label_tinggi_frame.pack(pady=10)
        
        # Entry untuk Tinggi
        self.entry_tinggi = tk.Entry(self.label_tinggi_frame, font=entry_font, width=15, bd=2, relief="solid", justify="center", bg='#FFD700')
        self.entry_tinggi.pack()

        # Tombol untuk menghitung luas segitiga
        self.create_square_button()

    def create_square_button(self):
        # Menambahkan tombol kotak ke dalam frame
        self.calculate_button = tk.Button(self.frame, text="Hitung Luas", font=('Arial Black', 14, 'bold'), bg='#FF4500', fg='#FFFFFF', command=self.calculate_area, bd=2, relief="raised")
        self.calculate_button.pack(pady=20)

        # Menambahkan efek hover pada tombol
        self.calculate_button.bind("<Enter>", self.on_hover)
        self.calculate_button.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        event.widget.config(bg='#FF6347', fg='white')

    def on_leave(self, event):
        event.widget.config(bg='#FF4500', fg='white')

    def calculate_area(self):
        try:
            alas = float(self.entry_alas.get())
            tinggi = float(self.entry_tinggi.get())
            
            # Hitung Luas Segitiga
            luas = (alas * tinggi) / 2
            
            # Menampilkan Hasil Perhitungan
            messagebox.showinfo("Hasil", f'Luas Segitiga adalah {luas:.2f}')
        
        except ValueError:
            messagebox.showerror("Error", "Harap masukkan angka yang valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TriangleAreaCalculator(root)
    root.mainloop()
