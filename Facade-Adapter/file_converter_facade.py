from adapters import PdfToDocxAdapter, DocxToTxtAdapter, TxtToDocxAdapter, PdfToTxtAdapter, TxtToPdfAdapter, DocxToPdfAdapter

# Clase que actua como fachada integrando los adaptadores
class FileConverterFacade:
    def __init__(self):
        # Diccionario de adaptadores con formato de origen y destino como clave
        # y el adaptador a utilizar como valor
        self.adapters = {
            ("pdf", "docx"): PdfToDocxAdapter(),
            ("docx", "txt"): DocxToTxtAdapter(),
            ("txt", "docx"): TxtToDocxAdapter(),
            ("pdf", "txt"): PdfToTxtAdapter(),
            ("txt", "pdf"): TxtToPdfAdapter(),
            ("docx", "pdf"): DocxToPdfAdapter(),
        }

    # método para convertir un archivo de un formato a otro
    def convertir_archivo(self, origen: str, destino: str, formato_origen: str, formato_destino: str):
        clave = (formato_origen.lower(), formato_destino.lower())
        if clave in self.adapters:
            # se llama al método convertir del adaptador correspondiente
            self.adapters[clave].convertir(origen, destino)
            return True
        else:
            return False