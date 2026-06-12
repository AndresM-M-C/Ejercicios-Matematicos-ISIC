import math

#=====================================================
# METODO DE BISECCION
#=====================================================

# Ecuacion 1: x^2 - 1 = 0
def biseccion_1():
    print("--- BISECCION: x^2 - 1 = 0 ---")
    
    # Datos iniciales
    a = 0.0      # Extremo izquierdo
    b = 2.0      # Extremo derecho
    tol = 0.00001  # Tolerancia
    max_iter = 100  # Máximo de iteraciones
    iter = 0     # Contador de iteraciones
    
    # Evaluar funcion en extremos
    fa = f1(a)   # f(0) = 0² - 1 = -1
    fb = f1(b)   # f(2) = 4 - 1 = 3
    
    # Verificar cambio de signo
    if fa * fb > 0:
        print(f"Error: No hay cambio de signo en [{a}, {b}]")
        return
    
    print(f"Intervalo inicial: [{a}, {b}], f(a)={fa}, f(b)={fb}")
    print("-" * 50)
    
    # Ciclo principal
    while (b - a) / 2.0 > tol and iter < max_iter:
        c = (a + b) / 2.0    # Punto medio
        fc = f1(c)            # f(c)
        
        print(f"Iter {iter}: c = {c:.6f}, f(c) = {fc:.6f}")
        
        # Verificar si encontro la raiz
        if abs(fc) < tol:
            print(f"¡Raíz encontrada! f(c) ≈ 0")
            break
        
        # Actualizar intervalo
        if fa * fc < 0:       # Si cambia signo entre a y c
            b = c              # La raíz está en [a, c]
            fb = fc
        else:                  # Si no cambia signo entre a y c
            a = c              # La raíz está en [c, b]
            fa = fc
        
        iter += 1
    
    print(f"\nRAÍZ APROXIMADA: x = {c:.6f}")
    print(f"Verificación: f({c:.6f}) = {f1(c):.6f}")
    print("=" * 50)

# Ecuacion 2: x^3 - 4x - 10 = 0
def biseccion_2():
    print("--- BISECCION: x^3 - 4x - 10 = 0 ---")
    
    # Datos iniciales
    a = 1.0      # Extremo izquierdo
    b = 3.0      # Extremo derecho
    tol = 0.00001
    max_iter = 100
    iter = 0
    
    # Evaluar funcion en extremos
    fa = f2(a)   # f(1) = 1 - 4 - 10 = -13
    fb = f2(b)   # f(3) = 27 - 12 - 10 = 5
    
    # Verificar cambio de signo
    if fa * fb > 0:
        print(f"Error: No hay cambio de signo en [{a}, {b}]")
        return
    
    print(f"Intervalo inicial: [{a}, {b}], f(a)={fa}, f(b)={fb}")
    print("-" * 50)
    
    # Ciclo principal
    while (b - a) / 2.0 > tol and iter < max_iter:
        c = (a + b) / 2.0
        fc = f2(c)
        
        print(f"Iter {iter}: c = {c:.6f}, f(c) = {fc:.6f}")
        
        if abs(fc) < tol:
            print(f"¡Raíz encontrada! f(c) ≈ 0")
            break
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iter += 1
    
    print(f"\nRAÍZ APROXIMADA: x = {c:.6f}")
    print(f"Verificación: f({c:.6f}) = {f2(c):.6f}")
    print("=" * 50)

# Ecuacion 3: cos(x) - x = 0
def biseccion_3():
    print("--- BISECCION: cos(x) - x = 0 ---")
    
    # Datos iniciales
    a = 0.0      # Extremo izquierdo
    b = 1.5      # Extremo derecho
    tol = 0.00001
    max_iter = 100
    iter = 0
    
    # Evaluar funcion en extremos
    fa = f3(a)   # f(0) = cos(0) - 0 = 1
    fb = f3(b)   # f(1.5) = cos(1.5) - 1.5 ≈ -1.429
    
    # Verificar cambio de signo
    if fa * fb > 0:
        print(f"Error: No hay cambio de signo en [{a}, {b}]")
        return
    
    print(f"Intervalo inicial: [{a}, {b}], f(a)={fa:.6f}, f(b)={fb:.6f}")
    print("-" * 50)
    
    # Ciclo principal
    while (b - a) / 2.0 > tol and iter < max_iter:
        c = (a + b) / 2.0
        fc = f3(c)
        
        print(f"Iter {iter}: c = {c:.6f}, f(c) = {fc:.6f}")
        
        if abs(fc) < tol:
            print(f"¡Raíz encontrada! f(c) ≈ 0")
            break
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iter += 1
    
    print(f"\nRAÍZ APROXIMADA: x = {c:.6f}")
    print(f"Verificación: f({c:.6f}) = {f3(c):.6f}")
    print("=" * 50)

#=====================================================
# FUNCIONES
#=====================================================

def f1(x):
    """Función: f(x) = x² - 1"""
    return x**2 - 1.0

def f2(x):
    """Función: f(x) = x³ - 4x - 10"""
    return x**3 - 4.0*x - 10.0

def f3(x):
    """Función: f(x) = cos(x) - x"""
    return math.cos(x) - x

#=====================================================
# PROGRAMA PRINCIPAL
#=====================================================

def main():
    print("=" * 60)
    print("MÉTODO DE BISECCIÓN - 3 EJERCICIOS")
    print("=" * 60)
    
    # Ejecutar los tres ejercicios
    biseccion_1()    # x² - 1 = 0
    biseccion_2()    # x³ - 4x - 10 = 0
    biseccion_3()    # cos(x) - x = 0
    
    print("\n" + "=" * 60)
    print("PROGRAMA FINALIZADO")
    print("=" * 60)

if __name__ == "__main__":
    main()