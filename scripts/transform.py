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
)

# =====================================
# Validación de columna requerida
# =====================================

if "descSucursal" not in df.columns:
    raise ValueError(
        f"La columna 'descSucursal' no existe. "
        f"Columnas encontradas: {list(df.columns)}"
    )

# =====================================
# Transformación
# Filtro EXACTO por "BOGOTA "
# =====================================

df_filtrado = df[
    df["descSucursal"]
    .astype(str)
    .str.upper() == "BOGOTA "
]

# =====================================
# Crear carpeta destino si no existe
# =====================================

output_excel.parent.mkdir(parents=True, exist_ok=True)

# =====================================
# Guardar resultados
# =====================================

df_filtrado.to_excel(output_excel, index=False)
df_filtrado.to_csv(output_csv, index=False, encoding="utf-8")

# =====================================
# Logs informativos
# =====================================

print("Transformación completada correctamente.")
print(f"Registros originales: {len(df)}")
print(f"Registros filtrados: {len(df_filtrado)}")
