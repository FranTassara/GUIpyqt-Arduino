import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000  # Hz (frecuencia de muestreo)
t = np.arange(0, 15, 1/fs)  # X segundos

# ECG sintético base
ecg = 0.5 * np.sin(2 * np.pi * 1.3 * t) + 0.02 * np.random.randn(len(t))
for i in range(1, len(t), int(fs/1.2)):
    if i + 3 < len(ecg):
        ecg[i:i+3] += [1.0, 0.3, -0.5]

# 💡 Agregar ruido de línea (cambiá a 60 si querés)
line_freq = 50  # Hz
line_noise = 0.1 * np.sin(2 * np.pi * line_freq * t)
ecg_noisy = ecg + line_noise

# Guardar como CSV (tiempo, señal)
data = np.column_stack((t, ecg_noisy))
np.savetxt("ecg_with_line_noise.csv", data, delimiter=',', header="time,signal", comments='')

# Mostrar para verificar
plt.figure(figsize=(10,4))
plt.plot(t, ecg_noisy, label='ECG con ruido de línea')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [a.u.]")
plt.title(f"ECG sintético con ruido de línea de {line_freq} Hz")
plt.legend()
plt.show()

print(f"✅ Archivo generado: ecg_with_line_noise.csv con ruido de línea de {line_freq} Hz")