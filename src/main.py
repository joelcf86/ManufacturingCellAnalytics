import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ==================================================
# CREAR DIRECTORIO DE FIGURAS
# ==================================================

os.makedirs("reports/figures", exist_ok=True)

# ==================================================
# CARGAR DATOS
# ==================================================

archivo = "data/raw/celda_manufactura.csv"

df = pd.read_csv(archivo)

print("\nPrimeras filas:")
print(df.head())

# ==================================================
# VARIABLES DE ENTRADA
# ==================================================

X = df[
    [
        "velocidad",
        "carga",
        "vida_util",
        "humedad",
        "corriente",
        "vibracion",
        "energia"
    ]
]

# ==================================================
# VARIABLE OBJETIVO
# ==================================================

y = df["produccion"]

# ==================================================
# NORMALIZAR
# ==================================================

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# ==================================================
# TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# ==================================================
# RED NEURONAL
# ==================================================

print("\nEntrenando red neuronal...\n")

modelo = MLPRegressor(
    hidden_layer_sizes=(64, 32, 16),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=1000,
    random_state=42
)

modelo.fit(X_train, y_train)

# ==================================================
# PREDICCION
# ==================================================

predicciones = modelo.predict(X_test)

# ==================================================
# METRICAS
# ==================================================

mae = mean_absolute_error(y_test, predicciones)

r2 = r2_score(y_test, predicciones)

print("\n==============================")
print("RESULTADOS DEL MODELO")
print("==============================")

print("MAE :", round(mae, 2))
print("R²  :", round(r2, 4))

# ==================================================
# GRAFICA 1
# REAL VS PREDICHO
# ==================================================

from sklearn.linear_model import LinearRegression

plt.figure(figsize=(10,7))

plt.scatter(
    y_test,
    predicciones,
    alpha=0.7
)

# Línea ideal
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--',
    linewidth=2,
    label='Predicción Ideal'
)

# Ajuste lineal
lr = LinearRegression()

lr.fit(
    np.array(y_test).reshape(-1,1),
    predicciones
)

m = lr.coef_[0]
b = lr.intercept_

x_line = np.linspace(
    y_test.min(),
    y_test.max(),
    100
)

y_line = m*x_line + b

plt.plot(
    x_line,
    y_line,
    linewidth=2,
    label='Tendencia'
)

plt.xlabel("Producción Real")
plt.ylabel("Producción Predicha")

plt.title(
    f"Producción Real vs Predicha\nR² = {r2:.4f}"
)

plt.text(
    0.05,
    0.95,
    f"y = {m:.3f}x + {b:.3f}",
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment='top',
    bbox=dict(boxstyle="round", alpha=0.2)
)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/figures/01_real_vs_predicho.png",
    dpi=300
)

# ==================================================
# GRAFICA 2
# HISTOGRAMA PRODUCCION
# ==================================================

plt.figure(figsize=(8, 6))

plt.hist(
    df["produccion"],
    bins=20
)

plt.xlabel("Producción")
plt.ylabel("Frecuencia")

plt.title("Distribución de Producción")

plt.tight_layout()

plt.savefig(
    "reports/figures/02_hist_produccion.png",
    dpi=300
)

# ==================================================
# GRAFICA 3
# CORRELACION
# ==================================================

plt.figure(figsize=(12,8))
# Calcular matriz de correlación
corr = df.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title(
    "Matriz de Correlación"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/03_correlacion.png",
    dpi=300
)

# ==================================================
# GRAFICA 4
# PRODUCCION VS VELOCIDAD
# ==================================================

plt.figure(figsize=(10,7))

plt.scatter(
    df["velocidad"],
    df["produccion"],
    alpha=0.6
)

coef = np.polyfit(
    df["velocidad"],
    df["produccion"],
    1
)

poly = np.poly1d(coef)

x = np.linspace(
    df["velocidad"].min(),
    df["velocidad"].max(),
    100
)

plt.plot(
    x,
    poly(x),
    linewidth=3
)

r2_vel = np.corrcoef(
    df["velocidad"],
    df["produccion"]
)[0,1]**2

plt.title(
    f"Producción vs Velocidad\nR²={r2_vel:.4f}"
)

plt.xlabel("Velocidad (RPM)")
plt.ylabel("Producción")

plt.text(
    0.05,
    0.95,
    f"y = {coef[0]:.4f}x + {coef[1]:.4f}",
    transform=plt.gca().transAxes,
    fontsize=12,
    verticalalignment='top',
    bbox=dict(boxstyle="round", alpha=0.2)
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "reports/figures/04_velocidad_produccion.png",
    dpi=300
)

# ==================================================
# GRAFICA 5
# IMPORTANCIA DE VARIABLES
# ==================================================

importancias = (
    corr["produccion"]
    .abs()
    .sort_values(ascending=False)
)

importancias = importancias.drop("produccion")

plt.figure(figsize=(10,6))

importancias.plot(kind="bar")

plt.title(
    "Influencia de Variables sobre Producción"
)

plt.ylabel(
    "|Correlación|"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "reports/figures/05_importancia_variables.png",
    dpi=300
)

# ==================================================
# OPTIMIZACION
# ==================================================

print("\nBuscando mejor configuración...\n")

df["score"] = (
      df["produccion"] * 2
    - df["energia"]
    - df["vibracion"] * 5
    - df["defectos"] * 10
)

mejor = df.loc[df["score"].idxmax()]

print("\n==============================")
print("CONFIGURACION OPTIMA")
print("==============================\n")

print(mejor)

# ==================================================
# REPORTE FINAL
# ==================================================

print("\n==============================")
print("RECOMENDACION")
print("==============================\n")

print(
    f"""
Velocidad recomendada : {mejor['velocidad']:.2f}
Carga recomendada     : {mejor['carga']:.2f}
Vida útil             : {mejor['vida_util']:.2f}
Humedad               : {mejor['humedad']:.2f}
Corriente             : {mejor['corriente']:.2f}
Vibración             : {mejor['vibracion']:.2f}
Energía               : {mejor['energia']:.2f}

Producción esperada   : {mejor['produccion']}

La configuración anterior maximiza
la producción mientras minimiza:

- Defectos
- Vibración
- Consumo energético
"""
)

print("\nFiguras guardadas en:")
print("reports/figures/")