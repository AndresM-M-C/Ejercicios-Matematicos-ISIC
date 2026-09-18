import math
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81

# --- Menú para selección de modo ---
print("--- SIMULACIÓN DE LANZAMIENTO DE PROYECTIL ---")
print("1. Ingresar datos manualmente")
print("2. Generar datos aleatorios")
opcion = input("Selecciona una opción (1 o 2): ").strip()

if opcion == "1":
    v0 = float(input("Ingresa la velocidad inicial v0 (m/s): "))
    angulo_deg = float(input("Ingresa el ángulo de lanzamiento (grados): "))
else:
    v0 = round(random.uniform(5.0, 50.0), 2)
    angulo_deg = round(random.uniform(10.0, 80.0), 2)
    print(f"\n[Valores aleatorios generados] -> v0: {v0} m/s | Ángulo: {angulo_deg}°")

theta = math.radians(angulo_deg)

v0x = v0 * math.cos(theta)
v0y = v0 * math.sin(theta)

t_vuelo = 2 * v0y / g
x_max = v0x * t_vuelo
y_max = (v0y**2) / (2 * g)

t = 0.0
dt = 0.01 
x_data, y_data = [], []

while True:
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    
    if y < 0 and t > 0:
        x_data.append(x_max)
        y_data.append(0)
        break
        
    x_data.append(x)
    y_data.append(y)
    t += dt

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, max(x_max * 1.1, 1.0))
ax.set_ylim(0, max(y_max * 1.2, 1.0))
ax.set_xlabel('Distancia X (m)')
ax.set_ylabel('Altura Y (m)')
ax.set_title(f'Trayectoria de Proyectil (v0 = {v0} m/s, θ = {angulo_deg}°)')
ax.grid(True, linestyle='--', alpha=0.6)

linea, = ax.plot([], [], 'b--', label='Trayectoria')
proyectil, = ax.plot([], [], 'ro', markersize=8, label='Proyectil')
ax.legend()

def init():
    linea.set_data([], [])
    proyectil.set_data([], [])
    return linea, proyectil

def update(frame):
    linea.set_data(x_data[:frame], y_data[:frame])
    proyectil.set_data([x_data[frame]], [y_data[frame]])
    return linea, proyectil

ani = FuncAnimation(
    fig, 
    update, 
    frames=len(x_data), 
    init_func=init, 
    interval=50,  
    blit=True, 
    repeat=False
)

plt.show()