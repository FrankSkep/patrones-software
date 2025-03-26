import os
import pytest
from adapters import PdfToDocxAdapter, DocxToTxtAdapter, TxtToDocxAdapter, PdfToTxtAdapter, TxtToPdfAdapter, DocxToPdfAdapter

@pytest.fixture
def setup_files():
    # Archivos temporales para pruebas
    files = {
        "pdf_file": "test.pdf",
        "docx_file": "test.docx",
        "txt_file": "test.txt",
        "output_file": "output"
    }

    # Crear un archivo de texto de prueba
    with open(files["txt_file"], "w", encoding="utf-8") as f:
        f.write("Este es un archivo de prueba.\nSegunda línea de texto.")

    yield files

    # Limpiar archivos generados
    for file in files.values():
        if os.path.exists(file):
            os.remove(file)
    for ext in [".pdf", ".docx", ".txt"]:
        output_file = f"{files['output_file']}{ext}"
        if os.path.exists(output_file):
            os.remove(output_file)

def test_txt_to_docx(setup_files):
    adapter = TxtToDocxAdapter()
    adapter.convertir(setup_files["txt_file"], f"{setup_files['output_file']}.docx")
    assert os.path.exists(f"{setup_files['output_file']}.docx")

def test_docx_to_txt(setup_files):
    adapter = TxtToDocxAdapter()
    adapter.convertir(setup_files["txt_file"], setup_files["docx_file"])

    adapter = DocxToTxtAdapter()
    adapter.convertir(setup_files["docx_file"], f"{setup_files['output_file']}.txt")
    assert os.path.exists(f"{setup_files['output_file']}.txt")

def test_pdf_to_txt(setup_files):
    # Crear un archivo PDF vacío para pruebas
    with open(setup_files["pdf_file"], "wb") as f:
        f.write(b"%PDF-1.4\n%Test PDF\n")

    adapter = PdfToTxtAdapter()
    adapter.convertir(setup_files["pdf_file"], f"{setup_files['output_file']}.txt")
    assert os.path.exists(f"{setup_files['output_file']}.txt")

def test_txt_to_pdf(setup_files):
    adapter = TxtToPdfAdapter()
    adapter.convertir(setup_files["txt_file"], f"{setup_files['output_file']}.pdf")
    assert os.path.exists(f"{setup_files['output_file']}.pdf")

def test_docx_to_pdf(setup_files):
    adapter = TxtToDocxAdapter()
    adapter.convertir(setup_files["txt_file"], setup_files["docx_file"])

    adapter = DocxToPdfAdapter()
    adapter.convertir(setup_files["docx_file"], f"{setup_files['output_file']}.pdf")
    assert os.path.exists(f"{setup_files['output_file']}.pdf")