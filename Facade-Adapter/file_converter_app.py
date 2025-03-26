import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from file_converter_facade import FileConverterFacade

# ==================== INTERFAZ GRAFICA CON CTK ==================== #
class FileConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Archivos")
        self.geometry("600x400")
        ctk.set_appearance_mode("dark")

        self.fachada = FileConverterFacade()
        self.origen = ""

        # Marco principal
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Etiqueta de título
        self.label = ctk.CTkLabel(self.main_frame, text="Conversor de Archivos", font=("Arial", 20, "bold"))
        self.label.pack(pady=10)

        # Marco para selección de archivo
        self.file_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.file_frame.pack(pady=10, padx=10, fill="x")

        self.file_label = ctk.CTkLabel(self.file_frame, text="Archivo seleccionado: Ninguno", anchor="w")
        self.file_label.pack(side="left", padx=10, pady=10, fill="x", expand=True)

        self.select_button = ctk.CTkButton(self.file_frame, text="Seleccionar Archivo", command=self.seleccionar_archivo)
        self.select_button.pack(side="right", padx=10, pady=10)

        # Menú desplegable de conversión
        self.format_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.format_frame.pack(pady=10, padx=10, fill="x")

        self.format_label = ctk.CTkLabel(self.format_frame, text="Formato de destino:", anchor="w")
        self.format_label.pack(side="left", padx=10, pady=10)

        self.formato_destino = ctk.CTkComboBox(self.format_frame, values=["PDF", "DOCX", "TXT"])
        self.formato_destino.pack(side="right", padx=10, pady=10)

        # Botón de conversión
        self.convert_button = ctk.CTkButton(self.main_frame, text="Convertir Archivo", command=self.convertir_archivo)
        self.convert_button.pack(pady=10)

        # Barra de progreso
        self.progress = ctk.CTkProgressBar(self.main_frame, mode="determinate")
        self.progress.pack(pady=10)
        self.progress.set(0)

        # Área de mensajes
        self.message_area = ctk.CTkTextbox(self.main_frame, height=100, state="disabled")
        self.message_area.pack(pady=10, padx=10, fill="both", expand=True)

    def seleccionar_archivo(self):
        self.origen = filedialog.askopenfilename(filetypes=[("Archivos", "*.pdf;*.docx;*.txt")])
        if self.origen:
            self.file_label.configure(text=f"Archivo seleccionado: {self.origen.split('/')[-1]}")

    def convertir_archivo(self):
        if not self.origen:
            messagebox.showwarning("Error", "Por favor, selecciona un archivo")
            return

        formato_origen = self.origen.split(".")[-1].lower()
        formato_destino = self.formato_destino.get().lower()
        destino = self.origen.replace(f".{formato_origen}", f".{formato_destino}")

        if formato_origen == formato_destino:
            messagebox.showwarning("Error", "El formato de origen y destino son iguales")
            return

        self.progress.set(0.5)  # Simula progreso intermedio
        self.update()

        if self.fachada.convertir_archivo(self.origen, destino, formato_origen, formato_destino):
            self.progress.set(1)
            self._append_message(f"Éxito: Conversión completada: {destino}")
            messagebox.showinfo("Éxito", f"Conversión completada: {destino}")
        else:
            self.progress.set(0)
            self._append_message(f"Error: Conversión de {formato_origen} a {formato_destino} no soportada.")
            messagebox.showerror("Error", f"Conversión de {formato_origen} a {formato_destino} no soportada.")

    def _append_message(self, message):
        self.message_area.configure(state="normal")
        self.message_area.insert("end", message + "\n")
        self.message_area.configure(state="disabled")

# ======================== EJECUCIÓN ======================== #
if __name__ == "__main__":
    app = FileConverterApp()
    app.mainloop()
