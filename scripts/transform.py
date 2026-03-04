import pandas as pd
from pathlib import Path

# =====================================
# Definición de rutas
# =====================================

input_path = Path("data/original/estadoObra.xlsx")
output_excel = Path("data/transformed/estadoObra_filtrado.xlsx")
output_csv = Path("data/transformed/estadoObra_filtrado.csv")

# =====================================
# Validación de existencia del archivo
# =====================================

if not input_path.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {input_path}")

# =====================================
# Lectura del archivo
# =====================================

df = pd.read_excel(input_path)

# =====================================
# Normalización de nombres de columnas
# =====================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.lower()
)

# =====================================
# Validación de columna requerida
# =====================================

if "sucursal" not in df.columns:
    raise ValueError(f"La columna 'Sucursal' no existe. Columnas encontradas: {list(df.columns)}")

# =====================================
# Transformación robusta
# =====================================

df_filtrado = df[
    df["sucursal"]
    .astype(str)
    .str.strip()
    .str.lower() == "bogota"
]

# =====================================
# Crear carpeta destino si no existe
# =====================================

output_excel.parent.mkdir(parents=True, exist_ok=True)

# =====================================
# Guardar resultados
# =====================================

# Excel
df_filtrado.to_excel(output_excel, index=False)

# CSV
df_filtrado.to_csv(output_csv, index=False, encoding="utf-8")

print("Transformación completada correctamente.")
print(f"Registros originales: {len(df)}")
print(f"Registros filtrados: {len(df_filtrado)}")
