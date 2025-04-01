from abc import ABC, abstractmethod

class Reporte(ABC):
    """
    Clase abstracta que define el método plantilla para generar reportes.
    """

    def generar_reporte(self, datos, output_label):
        """
        Método plantilla que define el flujo general de generación de reportes.
        """
        self.obtener_datos(datos)
        self.procesar_datos()
        self.formatear_reporte()
        self.exportar_reporte(output_label)

    def obtener_datos(self, datos):
        """Guarda los datos recibidos en la instancia."""
        self.datos = datos

    @abstractmethod
    def procesar_datos(self):
        """Método abstracto que cada subclase debe implementar."""
        pass

    @abstractmethod
    def formatear_reporte(self):
        """Método abstracto que define el formato del reporte."""
        pass

    @abstractmethod
    def exportar_reporte(self, output_label):
        """Método abstracto que define la exportación del reporte."""
        pass