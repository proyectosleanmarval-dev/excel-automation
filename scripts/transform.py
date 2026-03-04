import pandas as pd
from pathlib import Path

# ==============================
# Definición de rutas
# ==============================

input_path = Path("data/original/estadoObra.xlsx")
output_excel = Path("data/transformed/estadoObra_filtrado.xlsx")
output_csv = Path("data/transformed/estadoObra_filtrado.csv")

# ==============================
# Lectura del archivo
# ==============================

df = pd.read_excel(input_path)

# ==============================
# Normalizar nombres de columnas
# ==============================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.lower()
)

# ==============================
# Validación
# ==============================

if "sucursal" not in df.columns:
    raise ValueError(f"Columnas encontradas: {list(df.columns)}")

# ==============================
# Transformación
# ==============================

df_filtrado = df[
    df["sucursal"]
    .astype(str)
    .str.strip()
    .str.lower() == "bogota"
]

# ==============================
# Guardar resultados
# ==============================

output_excel.parent.mkdir(parents=True, exist_ok=True)

# Excel
df_filtrado.to_excel(output_excel, index=False)

# CSV
df_filtrado.to_csv(output_csv, index=False, encoding="utf-8")

print("Transformación completada correctamente.")
