from .file_system_component import FileSystemComponent
from .directory import Directory

class FileSystemIterator:
    """
    Esta clase implementa un iterador para recorrer la estructura del sistema de archivos.
    Utiliza un enfoque de recorrido en profundidad (DFS) para visitar cada componente.
    """
    def __init__(self, root: FileSystemComponent):
        self.stack = [root]

    # Esta función inicializa el iterador.
    def __iter__(self):
        return self

    # Esta función devuelve el siguiente elemento en el recorrido.
    # Si no hay más elementos, lanza una excepción StopIteration.
    def __next__(self) -> FileSystemComponent:
        if not self.stack:
            raise StopIteration

        current = self.stack.pop()
        if isinstance(current, Directory):
            # Añadir los hijos en orden inverso
            self.stack.extend(reversed(current.children))
        return current