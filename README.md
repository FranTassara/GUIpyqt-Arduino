# 🖥️ GUIpyqt-Arduino

Este repo contiene todo el material para aprender a armar interfaces gráficas en Python usando **PyQt/PySide**, y conectar una **señal analógica de Arduino** para visualizarla en tiempo real o plotear una imagen y aplicarle filtros.

Ideal para proyectos de bioingeniería, procesamiento de señales o imágenes y prototipos biomédicos.

---

## ¿Qué vas a aprender?

- Crear interfaces gráficas simples en Python (PyQt/PySide).
- Conectarte con un Arduino vía Serial (puerto COM).
- Leer y graficar una señal analógica en vivo.
- Pltear una imagen y aplicarle filtros

---

## 01_primer_gui

Pequeña interfaz gráfica que muestra una ventana con un botón.  
La idea es entender la estructura básica de una gui en PyQt/PySide.

Se aprende a:
- Crear una ventana.
- Agregar widgets básicos (botones).
- Manejar eventos de click.

---

## 02_plotear_imagen_filtrar

Carga una imagen (ej: una RMN), la muestra en la interfaz y permite aplicarle filtros básicos.

Se aprende a:
- Cargar y mostrar imágenes.
- Usar `pyqtgraph` o `matplotlib` embebido.
- Aplicar un filtro (ejemplo: media, gaussiano o sobel).

---

## 03_arduino_plot_en_vivo

Conecta el Arduino vía puerto serie, lee una señal analógica en tiempo real y la plotea en la interfaz.

Se aprende:
- Comunicación serial (PySerial).
- Adquisición de datos en tiempo real.
- Ploteo dinámico de señales tipo ECG o EMG.

---

---

## Cómo empezar

[![Abrir presentación](https://img.shields.io/badge/Ver_Presentación-PDF-blue)](/Steps.pdf)

1. Instalar las librerías necesarias.
2. Cargar el código Arduino (`lectura_senal.ino`) en tu placa.
3. Correr los ejemplos de Python siguiendo el orden recomendado.

---

> Este proyecto te va a ayudar a mezclar hardware y software para visualizar señales de una forma simple y potente.
