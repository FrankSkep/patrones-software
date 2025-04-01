import customtkinter as ctk
from concrete_reports import ReportePDF, ReporteCSV, ReporteHTML

class Aplicacion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.HEIGHT=450
        self.WIDTH=500
        
        self.title("Generador de Reportes")
        self.geometry(F"{self.WIDTH}x{self.HEIGHT}")

        self.principal= ctk.CTkFrame(self, width=self.WIDTH, height=self.HEIGHT)
        self.principal.pack(padx=5, pady=5, fill="both", expand=True)        
        # Entrada de datos
        self.label = ctk.CTkLabel(self.principal, text="Ingrese datos:")
        self.label.pack(pady=10)

        self.entradaDatos = ctk.CTkFrame(self.principal)
        self.entradaDatos.pack(pady=10)
        
        self.entrada = ctk.CTkTextbox(self.entradaDatos, width=400, height=90)
        self.entrada.pack(pady=5, padx=5)

        # Botones de generación de reporte
        self.boton_pdf = ctk.CTkButton(self.principal, text="Generar Reporte PDF", command=self.generar_pdf)
        self.boton_pdf.pack(pady=5)

        self.boton_csv = ctk.CTkButton(self.principal, text="Generar Reporte CSV", command=self.generar_csv)
        self.boton_csv.pack(pady=5)

        self.boton_html = ctk.CTkButton(self.principal, text="Generar Reporte HTML", command=self.generar_html)
        self.boton_html.pack(pady=5)

        # Label de salida
        self.output_label = ctk.CTkLabel(self, text="", fg_color="transparent")
        self.output_label.pack(pady=10)

    def generar_pdf(self):
        datos = self.entrada.get("1.0","end").strip().split("\n")
        reporte = ReportePDF()
        reporte.generar_reporte(datos, self.output_label)

    def generar_csv(self):
        datos = self.entrada.get("1.0","end").strip().split("\n")
        reporte = ReporteCSV()
        reporte.generar_reporte(datos, self.output_label)

    def generar_html(self):
        datos = self.entrada.get("1.0","end").strip().split("\n")
        reporte = ReporteHTML()
        reporte.generar_reporte(datos, self.output_label)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
