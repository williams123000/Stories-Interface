import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import pyttsx3
import threading
from tkinter.font import Font
import os
from PIL import Image, ImageTk
import sys

class StoryGeneratorGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Generador de Historias Cósmicas")
        master.geometry("1200x690")
        master.configure(bg="#0B0E17")

        # Función para obtener la ruta del archivo
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)
        
        # Cargar y mostrar una imagen de fondo usando resource_path
        self.bg_image = Image.open(resource_path("background2.jpg"))
        self.bg_image = self.bg_image.resize((1200, 690), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.load_custom_font()
        self.center_window()
        self.engine = pyttsx3.init()

        # Updated color palette with softer TFrame color
        self.colors = {
            "bg_dark": "#0B0E17",
            "bg_medium": "#1d293b",
            "bg_light": "#2A3B55",  # New softer color for TFrame
            "accent": "#4A698C",
            "text_light": "#E0E7FF",
            "text_dark": "#B8C7E0",
            "button": "#5A82B4",
            "button_hover": "#6A92C4"
        }

        # Configure fonts
        title_font = Font(family="Product Sans", size=29, weight="bold")
        subtitle_font = Font(family="Product Sans", size=16)
        button_font = Font(family="Product Sans", size=14, weight="bold")
        text_font = Font(family="Product Sans", size=12)

        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Updated TFrame style with softer background color
        self.style.configure("TFrame", background=self.colors["bg_light"])
        
        self.style.configure("TButton", 
                             background=self.colors["button"],
                             foreground=self.colors["text_light"],
                             font=button_font,
                             padding=10,
                             borderwidth=0)
        self.style.map("TButton", 
                       background=[("active", self.colors["button_hover"])])
        
        self.style.configure("TCheckbutton",
                             background=self.colors["bg_light"],
                             foreground=self.colors["text_light"],
                             font=text_font)
        self.style.map("TCheckbutton",
                       background=[("active", self.colors["bg_medium"])],
                       foreground=[("active", self.colors["text_dark"])])
        
        self.style.configure("TLabel", 
                             background=self.colors["bg_light"],
                             foreground=self.colors["text_light"],
                             font=text_font)

        self.style.configure("TCombobox", 
                             fieldbackground=self.colors["bg_medium"],
                             background=self.colors["accent"],
                             foreground=self.colors["text_light"],
                             arrowcolor=self.colors["text_light"])
        self.style.map("TCombobox", 
                       fieldbackground=[("readonly", self.colors["bg_medium"])],
                       selectbackground=[("readonly", self.colors["bg_medium"])],
                       selectforeground=[("readonly", self.colors["text_light"])])

        # Main frame with transparency effect
        main_frame = tk.Frame(master, bg=self.colors["bg_light"], bd=2, relief=tk.RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        # Title with glow effect
        title = tk.Label(main_frame, 
                         text="🌌 Generador de Historias 🌌", 
                         font=title_font, 
                         bg=self.colors["bg_light"], 
                         fg=self.colors["text_light"])
        title.pack(pady=5)

        # Options frame
        options_frame = ttk.Frame(main_frame, style="TFrame")
        options_frame.pack(pady=5, padx=30, fill='x')

        ttk.Label(options_frame, text="Configura tu aventura estelar:", font=subtitle_font, style="TLabel").pack(anchor="w", pady=0)

        self.voice_var = tk.IntVar(value=0)
        voice_check = ttk.Checkbutton(options_frame, text="Activar narración por voz", variable=self.voice_var, style="TCheckbutton")
        voice_check.pack(anchor="w", pady=0)

        self.ia_var = tk.IntVar(value=0)
        ia_check = ttk.Checkbutton(options_frame, text="Potenciar con IA avanzada", variable=self.ia_var, style="TCheckbutton")
        ia_check.pack(anchor="w", pady=0)

        ttk.Label(options_frame, text="Elige el tema de tu odisea espacial:", font=subtitle_font, style="TLabel").pack(anchor="w", pady=(10,5))
        self.script_var = tk.StringVar(value="Un Secuestro")
        self.script_map = {
            "Un Secuestro": "HistoryFinal.py",
            "La Búsqueda del Tesoro": "History.py"
        }
        script_combo = ttk.Combobox(options_frame, textvariable=self.script_var, values=list(self.script_map.keys()), state="readonly", style="TCombobox")
        script_combo.pack(fill='x', pady=0)

        # Generate story button
        self.generate_button = ttk.Button(main_frame, text="Genera tu historia", command=self.generate_story, style="TButton")
        self.generate_button.pack(pady=5)

        # Text area for displaying the story
        self.story_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=80, height=12, font=text_font)
        self.story_text.pack(pady=20, padx=50, fill='both', expand=True)
        self.story_text.configure(bg=self.colors["bg_medium"], fg=self.colors["text_light"])

        # Author signature
        author_label = ttk.Label(main_frame, text="Creado por: Williams Chan | Sistemas Inteligentes", style="TLabel")
        author_label.pack(side=tk.BOTTOM, pady=10)

    def generate_story(self):
        self.generate_button.configure(state="disabled")
        self.story_text.delete('1.0', tk.END)
        self.story_text.insert(tk.END, "Preparando los motores de la narrativa cósmica...\n\n")

        selected_theme = self.script_var.get()
        selected_script = self.script_map.get(selected_theme, "History.py")

        # Usar resource_path para obtener la ruta correcta del script
        script_path = self.resource_path(selected_script)
        args = ['python', script_path, 
                f'-Voice={self.voice_var.get()}', 
                f'-IA={self.ia_var.get()}']

        def run_script():
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()
            self.master.after(0, self.update_story_text, output, error)

        threading.Thread(target=run_script, daemon=True).start()

    def update_story_text(self, output, error):
        self.story_text.delete('1.0', tk.END)
        if error:
            self.story_text.insert(tk.END, f"Error en el sistema de navegación espacial: {error}")
        else:
            self.story_text.insert(tk.END, output)
            if self.voice_var.get():
                self.master.after(500, lambda: threading.Thread(target=self.read_text_aloud, args=(output,)).start())
        self.generate_button.configure(state="normal")

    def read_text_aloud(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def load_custom_font(self):
        font_path = "/Font/ProductSans.ttf"
        if os.path.exists(font_path):
            self.master.tk.call('font', 'create', 'ProductSans', 
                                '-family', 'Product Sans', 
                                '-file', font_path)
            print("Fuente Product Sans cargada correctamente.")
        else:
            print("No se pudo encontrar el archivo de fuente. Usando fuente predeterminada.")

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        # Aumentar un poco a la y
        y -= 37
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tk.Tk()
    gui = StoryGeneratorGUI(root)
    root.mainloop()