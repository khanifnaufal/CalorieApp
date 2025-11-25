# gui_app.py (Menggunakan CustomTkinter untuk tampilan modern)
import customtkinter as ctk
from tkinter import messagebox
from calculator import calculate_bmr, calculate_tdee

# Daftar level aktivitas
ACTIVITY_LEVELS = [
    "Sedentari (Jarang/Tidak Olahraga)", 
    "Ringan (1-3 hari/minggu)", 
    "Sedang (3-5 hari/minggu)", 
    "Berat (6-7 hari/minggu)", 
    "Sangat Berat (Harian, Intens)"
]

# Set default appearance mode dan tema (opsional)
ctk.set_appearance_mode("System") # Menggunakan mode sistem (terang/gelap)
ctk.set_default_color_theme("blue")

class CalorieApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Hitung Kalori Harian (Modern)")
        master.geometry("400x550") # Tetapkan ukuran jendela

        # Variabel CustomTkinter untuk Input
        self.gender = ctk.StringVar(master, value='pria')
        self.activity = ctk.StringVar(master, value=ACTIVITY_LEVELS[0])
        self.entries = {}
        
        # --- Bagian 1: Input Form (Gunakan CTkFrame) ---
        input_frame = ctk.CTkFrame(master)
        input_frame.pack(padx=20, pady=20, fill="x")

        # Judul Besar
        ctk.CTkLabel(input_frame, text="KALKULATOR TDEE", 
                     font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, columnspan=3, pady=(10, 15))

        # Baris Input (Usia, Berat, Tinggi)
        self._create_label_entry(input_frame, "Usia (tahun):", "age", 1)
        self._create_label_entry(input_frame, "Berat Badan (kg):", "weight", 2)
        self._create_label_entry(input_frame, "Tinggi Badan (cm):", "height", 3)
        
        # Input Radiobutton Jenis Kelamin
        ctk.CTkLabel(input_frame, text="Jenis Kelamin:").grid(row=4, column=0, sticky="w", padx=10, pady=10)
        ctk.CTkRadioButton(input_frame, text="Pria", variable=self.gender, value="pria").grid(row=4, column=1, sticky="w")
        ctk.CTkRadioButton(input_frame, text="Wanita", variable=self.gender, value="wanita").grid(row=4, column=2, sticky="w")
        
        # Input Dropdown Aktivitas
        ctk.CTkLabel(input_frame, text="Level Aktivitas:").grid(row=5, column=0, sticky="w", padx=10, pady=10)
        # CTkOptionMenu membutuhkan nilai yang tidak dimodifikasi untuk *values*
        activity_menu = ctk.CTkOptionMenu(input_frame, variable=self.activity, values=ACTIVITY_LEVELS)
        activity_menu.grid(row=5, column=1, columnspan=2, sticky="ew", padx=10)

        # Tombol Hitung
        ctk.CTkButton(master, text="HITUNG KALORI", command=self.calculate_and_display, 
                      font=ctk.CTkFont(size=14, weight="bold"), height=40, corner_radius=10).pack(pady=(0, 20), fill="x", padx=20)

        # --- Bagian 2: Output Hasil (Gunakan CTkFrame) ---
        output_frame = ctk.CTkFrame(master)
        output_frame.pack(padx=20, pady=10, fill="x")
        
        ctk.CTkLabel(output_frame, text="HASIL:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 5))
        
        self.bmr_label = ctk.CTkLabel(output_frame, text="BMR (Kalori Minimum): -", anchor="w", font=ctk.CTkFont(size=12))
        self.bmr_label.pack(fill="x", padx=15, pady=5)
        
        self.tdee_label = ctk.CTkLabel(output_frame, text="TDEE (Kebutuhan Harian): -", anchor="w", 
                                       font=ctk.CTkFont(size=14, weight="bold"), text_color="#2ECC71") # Warna hijau menenangkan
        self.tdee_label.pack(fill="x", padx=15, pady=10)

    def _create_label_entry(self, parent, label_text, key, row):
        """Fungsi helper untuk membuat Label dan Entry CustomTkinter."""
        ctk.CTkLabel(parent, text=label_text).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        entry = ctk.CTkEntry(parent, width=15)
        entry.grid(row=row, column=1, columnspan=2, sticky="ew", padx=10)
        self.entries[key] = entry
        
    def calculate_and_display(self):
        """Mengambil data input, menghitung, dan menampilkan hasil."""
        try:
            # Mengambil dan memvalidasi input
            age = int(self.entries['age'].get())
            weight = float(self.entries['weight'].get())
            height = float(self.entries['height'].get())
            gender = self.gender.get()
            
            if age <= 0 or weight <= 0 or height <= 0:
                messagebox.showerror("Input Error", "Semua input (Usia, Berat, Tinggi) harus berupa angka positif.")
                return

            # Mengambil level aktivitas yang disederhanakan (kata pertama)
            activity_key = self.activity.get().split(' ')[0].lower()
            
            # 1. Hitung BMR
            bmr_result = calculate_bmr(gender, age, weight, height)
            
            # 2. Hitung TDEE
            tdee_result = calculate_tdee(bmr_result, activity_key)
            
            # 3. Tampilkan Hasil
            self.bmr_label.configure(text=f"BMR (Kalori Minimum): {bmr_result:.0f} Kalori/hari")
            self.tdee_label.configure(text=f"TDEE (Kebutuhan Harian): {tdee_result:.0f} Kalori/hari")

        except ValueError:
            messagebox.showerror("Input Error", "Mohon pastikan Usia, Berat, dan Tinggi diisi dengan angka yang benar.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan tak terduga: {e}")

if __name__ == '__main__':
    root = ctk.CTk()
    app = CalorieApp(root)
    root.mainloop()