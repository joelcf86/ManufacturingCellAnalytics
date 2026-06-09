# Manufacturing Cell Analytics

Sistema de análisis y optimización de una celda de manufactura utilizando técnicas de Inteligencia Artificial y Machine Learning.

## 📋 Descripción

Este proyecto simula una celda de manufactura industrial y utiliza algoritmos de aprendizaje automático para analizar el comportamiento del proceso productivo, identificar variables críticas y proponer condiciones óptimas de operación.

El sistema genera datos sintéticos de operación, entrena una red neuronal para modelar el comportamiento de la producción y genera reportes gráficos que facilitan la toma de decisiones dentro de un entorno de Industria 4.0.

---

## 🎯 Objetivos

* Simular el comportamiento de una celda de manufactura.
* Generar datos de producción para análisis.
* Aplicar técnicas de Machine Learning.
* Entrenar una red neuronal para predecir la producción.
* Identificar variables con mayor impacto en el desempeño.
* Obtener recomendaciones de operación óptima.
* Generar reportes gráficos para análisis industrial.

---

## 🏭 Variables Analizadas

El sistema considera las siguientes variables de proceso:

| Variable   | Descripción                          |
| ---------- | ------------------------------------ |
| Velocidad  | Velocidad de operación de la máquina |
| Carga      | Porcentaje de carga aplicada         |
| Vida útil  | Estado estimado del equipo           |
| Humedad    | Humedad relativa del ambiente        |
| Corriente  | Consumo eléctrico                    |
| Vibración  | Nivel de vibración del sistema       |
| Defectos   | Cantidad de piezas defectuosas       |
| Producción | Piezas producidas                    |
| Energía    | Consumo energético                   |

---

## 🧠 Modelo de Inteligencia Artificial

Se implementa una red neuronal tipo:

**MLP (Multi-Layer Perceptron)**

Arquitectura utilizada:

```text
Entradas (7 variables)
        │
        ▼
Capa Oculta 1 (64 neuronas)
        │
        ▼
Capa Oculta 2 (32 neuronas)
        │
        ▼
Capa Oculta 3 (16 neuronas)
        │
        ▼
Salida (Producción)
```

El modelo es entrenado utilizando Scikit-Learn mediante el algoritmo de retropropagación (Backpropagation) y el optimizador Adam.

---

## 📁 Estructura del Proyecto

```text
ManufacturingCellAnalytics/
│
├── data/
│   └── raw/
│       └── celda_manufactura.csv
│
├── reports/
│   └── figures/
│
├── src/
│   ├── generate_data.py
│   ├── data.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Instalación

### Requisitos

Se recomienda utilizar:

* Python 3.11.x ✅
* Python 3.12.x ✅

> **Importante:** Algunas librerías de Inteligencia Artificial y Machine Learning, como TensorFlow, pueden presentar problemas de compatibilidad con versiones más recientes de Python (3.13 y superiores). Para garantizar el correcto funcionamiento del proyecto se recomienda trabajar con Python 3.11 o Python 3.12.

Verificar la versión instalada:

```bash
python --version
```

### Clonar repositorio

```bash
git clone https://github.com/joelcf86/ManufacturingCellAnalytics.git

cd ManufacturingCellAnalytics
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Actualizar pip

```bash
python -m pip install --upgrade pip
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```
---

## ⚙️ Generar Dataset

Ejecutar:

```bash
python src/generate_data.py
```

Se generará automáticamente:

```text
data/raw/celda_manufactura.csv
```

---

## 📊 Análisis y Optimización

Ejecutar:

```bash
python src/main.py
```

El sistema realizará:

* Carga del dataset.
* Normalización de variables.
* Entrenamiento de la red neuronal.
* Evaluación del modelo.
* Predicción de producción.
* Análisis de correlación.
* Búsqueda de condiciones óptimas.
* Generación de gráficas.

---

## 📈 Gráficas Generadas

El proyecto genera automáticamente:

### Producción Real vs Predicha

Permite evaluar la capacidad predictiva del modelo.

### Matriz de Correlación

Identifica relaciones entre variables de proceso.

### Producción vs Velocidad

Analiza el impacto de la velocidad sobre la producción.

### Importancia de Variables

Muestra qué variables afectan más el desempeño de la celda.

---

## 📌 Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Machine Learning
* Artificial Intelligence

---

## Resultados Esperados

El sistema permite:

* Identificar condiciones óptimas de operación.
* Reducir defectos de producción.
* Minimizar consumo energético.
* Detectar variables críticas.
* Implementar estrategias de mantenimiento predictivo.
* Mejorar la eficiencia de la celda de manufactura.

---



## 📄 Licencia

Este proyecto se distribuye con fines académicos y de investigación.
Puede ser utilizado como base para proyectos de aprendizaje relacionados con:

* Inteligencia Artificial
* Machine Learning
* Manufactura Inteligente
* Gemelos Digitales
* Industria 4.0
* Mantenimiento Predictivo
