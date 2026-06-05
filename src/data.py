import os
import csv
import random
from datetime import datetime, timedelta

# ==================================================
# CONFIGURACION
# ==================================================

OUTPUT_DIR = "data/raw"
OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "celda_manufactura.csv"
)

NUM_REGISTROS = 5000

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

# ==================================================
# GENERACION DE DATOS
# ==================================================

fecha = datetime.now()

with open(
    OUTPUT_FILE,
    mode="w",
    newline="",
    encoding="utf-8"
) as archivo:

    writer = csv.writer(archivo)

    writer.writerow([
        "timestamp",
        "velocidad",
        "carga",
        "vida_util",
        "humedad",
        "corriente",
        "vibracion",
        "defectos",
        "produccion",
        "energia"
    ])

    for _ in range(NUM_REGISTROS):

        # -------------------------
        # VARIABLES PRINCIPALES
        # -------------------------

        velocidad = random.uniform(900, 1800)

        carga = random.uniform(30, 100)

        vida_util = random.uniform(20, 100)

        humedad = random.uniform(30, 70)

        # -------------------------
        # CORRIENTE
        # DEPENDE DE VELOCIDAD Y CARGA
        # -------------------------

        corriente = (
            2
            + (carga * 0.18)
            + (velocidad / 250)
            + random.uniform(-1, 1)
        )

        # -------------------------
        # VIBRACION
        # AUMENTA SI LA VIDA UTIL BAJA
        # -------------------------

        vibracion = (
            0.5
            + ((100 - vida_util) * 0.08)
            + random.uniform(0, 1)
        )

        # -------------------------
        # DEFECTOS
        # DEPENDEN DE LA VIBRACION
        # -------------------------

        defectos = max(
            0,
            int(
                vibracion * 0.8
                + random.uniform(0, 2)
            )
        )

        # -------------------------
        # PRODUCCION
        # RELACIONADA CON VELOCIDAD
        # Y AFECTADA POR DEFECTOS
        # -------------------------

        produccion = (
            (velocidad * 0.28)
            + (carga * 1.5)
            - (defectos * 8)
            - (vibracion * 3)
            + random.uniform(-20, 20)
        )

        produccion = max(
            50,
            int(produccion)
        )

        # -------------------------
        # ENERGIA
        # DEPENDE DE CARGA Y CORRIENTE
        # -------------------------

        energia = (
            corriente * 0.6
            + carga * 0.08
            + random.uniform(-1, 1)
        )

        writer.writerow([
            fecha.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            round(velocidad, 2),
            round(carga, 2),
            round(vida_util, 2),
            round(humedad, 2),
            round(corriente, 2),
            round(vibracion, 2),
            defectos,
            produccion,
            round(energia, 2)
        ])

        fecha += timedelta(minutes=1)

print()
print("=================================")
print("ARCHIVO GENERADO CORRECTAMENTE")
print("=================================")
print(OUTPUT_FILE)
print("Registros:", NUM_REGISTROS)

