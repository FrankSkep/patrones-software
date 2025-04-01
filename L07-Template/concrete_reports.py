from report_template import Reporte
from fpdf import FPDF
import csv
import webbrowser

class ReportePDF(Reporte):
    """Clase concreta que genera reportes en formato PDF."""

    def procesar_datos(self):
        self.reporte_texto = "\n".join(self.datos)

    def formatear_reporte(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        for linea in self.datos:
            self.pdf.cell(200, 10, txt=linea, ln=True, align='L')

    def exportar_reporte(self, output_label):
        archivo_pdf = "reporte.pdf"
        self.pdf.output(archivo_pdf)
        output_label.configure(text=f"Reporte PDF generado: {archivo_pdf}")

class ReporteCSV(Reporte):
    """Clase concreta que genera reportes en formato CSV."""

    def procesar_datos(self):
        self.reporte_texto = "\n".join(self.datos)

    def formatear_reporte(self):
        self.reporte_csv = [linea.split(",") for linea in self.datos]

    def exportar_reporte(self, output_label):
        archivo_csv = "reporte.csv"
        with open(archivo_csv, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.reporte_csv)
        output_label.configure(text=f"Reporte CSV generado: {archivo_csv}")

class ReporteHTML(Reporte):
    """Clase concreta que genera reportes en formato HTML."""

    def procesar_datos(self):
        self.reporte_html = "<html><head><title>Reporte</title></head><body>"
        self.reporte_html += "<h1>Reporte Generado</h1><ul>"
        for item in self.datos:
            self.reporte_html += f"<li>{item}</li>"
        self.reporte_html += "</ul></body></html>"

    def formatear_reporte(self):
        pass  # Ya formateamos el HTML en procesar_datos()

    def exportar_reporte(self, output_label):
        archivo_html = "reporte.html"
        with open(archivo_html, "w") as file:
            file.write(self.reporte_html)
        output_label.configure(text=f"Reporte HTML generado: {archivo_html}")
        webbrowser.open(archivo_html)  # Abre el HTML en el navegador automáticamente