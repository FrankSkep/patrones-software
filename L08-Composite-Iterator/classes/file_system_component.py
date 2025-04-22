from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    """
    Esta clase representa un componente del sistema de archivos.
    Puede ser un archivo o un directorio.
    """
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0, last: bool = True):
        pass