from classes.directory import Directory
from classes.file import File
from classes.file_iterator import FileSystemIterator

if __name__ == "__main__":
    # === 1. Crear directorios ===
    root = Directory("root")

    # Nivel 1
    bin_dir = Directory("bin")
    etc_dir = Directory("etc")
    home_dir = Directory("home")
    opt_dir = Directory("opt")

    # Nivel 2
    user_dir = Directory("user")
    idea_dir = Directory("idea")
    
    # Nivel 3
    download_dir = Directory("Downloads")
    documents_dir = Directory("Documents")

    # === 2. Construir la jerarquía de carpetas ===
    root.add(bin_dir)
    root.add(etc_dir)
    root.add(home_dir)
    root.add(opt_dir)

    home_dir.add(user_dir)
    opt_dir.add(idea_dir)

    user_dir.add(download_dir)
    user_dir.add(documents_dir)

    # === 3. Agregar archivos ===
    bin_dir.add(File("bash"))
    bin_dir.add(File("ls"))

    etc_dir.add(File("config.cfg"))

    documents_dir.add(File("document.txt"))
    download_dir.add(File("photo.jpg"))

    # === 4. Mostrar la estructura ===
    import os
    os.system("cls" if os.name == "nt" else "clear")

    print("=== ESTRUCTURA DEL SISTEMA DE ARCHIVOS ===")
    root.display()

    # === 5. Recorrido con iterador ===
    print("\n=== RECORRIDO CON ITERADOR (PROFUNDIDAD) ===")
    for component in FileSystemIterator(root):
        tipo = "(Directorio)" if isinstance(component, Directory) else "(Archivo)"
        print(f"Visitando: {component.name} {tipo}")
