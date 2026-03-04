import pandas as pd
from pathlib import Path

# ==============================
# Definición de rutas
# ==============================

input_path = Path("data/original/estadoObra.xlsx")
output_path = Path("data/transformed/estadoObra_filtrado.xlsx")

# ==============================
# Lectura del archivo
# ==============================

df = pd.read_excel(input_path)

# ==============================
# Validación de existencia de columna
# ==============================

if "Sucursal" not in df.columns:
    raise ValueError("La columna 'Sucursal' no existe en el archivo.")

# ==============================
# Transformación (robusta)
# ==============================

df_filtrado = df[
    df["Sucursal"]
    .astype(str)
    .str.strip()
    .str.lower() == "bogota"
]

# ==============================
# Guardar resultado
# ==============================

output_path.parent.mkdir(parents=True, exist_ok=True)
df_filtrado.to_excel(output_path, index=False)

print("Transformación completada correctamente.")
