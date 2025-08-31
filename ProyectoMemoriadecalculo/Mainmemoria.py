import pandas as pd
from docx import Document
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Ocultar la ventana principal de Tkinter
Tk().withdraw()

# Seleccionar archivo Excel
archivo_excel = askopenfilename(
    title="Selecciona el archivo Excel",
    filetypes=[("Archivos Excel", "*.xlsx *.xls")]
)

# Seleccionar archivo Word (plantilla)
archivo_word = askopenfilename(
    title="Selecciona la plantilla Word",
    filetypes=[("Archivos Word", "*.docx")]
)

if archivo_excel and archivo_word:
    # Leer datos de Excel
    df = pd.read_excel(archivo_excel)

    # Recorrer filas del Excel y generar documentos
    for index, row in df.iterrows():
        doc = Document(archivo_word)  # Abrir plantilla

        # Reemplazar marcadores de posición
        for p in doc.paragraphs:
            p.text = p.text.replace("{{NOMBRE}}", str(row["Nombre"]))
            p.text = p.text.replace("{{VOLTAGE}}", str(row["Voltaje"]))
            p.text = p.text.replace("{{CORRIENTE}}", str(row["Corriente"]))

        # Guardar documento generado
        doc.save(f"memoria_{index+1}.docx")

    print("Documentos generados correctamente.")
else:
    print("No se seleccionó alguno de los archivos.")