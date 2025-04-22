from .file_system_component import FileSystemComponent

class File(FileSystemComponent):
    """
    Esta clase representa un archivo en el sistema de archivos.
    Hereda de FileSystemComponent y representa un archivo individual.
    """
    
    def display(self, indent: int = 0, last: bool = True, prefix: str = ""):
        symbol = "└── " if last else "├── "
        print(prefix + symbol + f"{self.name}")