from .file_system_component import FileSystemComponent
from typing import List

class Directory(FileSystemComponent):
    """
    Esta clase representa un directorio en el sistema de archivos.
    Puede contener otros archivos o directorios.
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    # Agregar un componente (archivo o directorio) al directorio
    def add(self, component: FileSystemComponent):
        self.children.append(component)

    # Eliminar un componente (archivo o directorio) del directorio
    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    # Mostrar la estructura del directorio
    def display(self, indent: int = 0, last: bool = True, prefix: str = ""):
        symbol = "└── " if last else "├── "
        print(prefix + symbol + f"{self.name}")
        
        # Actualizar el prefijo para los hijos
        new_prefix = prefix + ("    " if last else "│   ")
        
        # Recorrer los hijos, mostrando si es el último o no
        for index, child in enumerate(self.children):
            child.display(indent + 1, last=(index == len(self.children) - 1), prefix=new_prefix)