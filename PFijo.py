import math

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    """
    Método de punto fijo: x_{n+1} = g(x_n)
    """
    print(f"\n{'i':^4} | {'x_n':^12} | {'g(x_n)':^12} | {'error':^12}")
    print("-" * 50)
    
    x = x0
    for i in range(max_iter):
        x_nuevo = g(x)
        error = abs(x_nuevo - x)
        
        print(f"{i:^4} | {x:^12.8f} | {x_nuevo:^12.8f} | {error:^12.8f}")
        
        if error < tol:
            print(f"\n✅ Raíz encontrada: x = {x_nuevo:.8f}")
            print(f"   Iteraciones: {i+1}")
            return x_nuevo
        
        x = x_nuevo
    
    print("\n⚠️  No convergió en las iteraciones máximas")
    return x


# EJEMPLOS RÁPIDOS:

print("=" * 50)
print("MÉTODO DE PUNTO FIJO")
print("=" * 50)



# Ejemplo 4: Resolver x³ + 4x² - 10 = 0 (despejando x = √(10/(x+4)))
print("\n📌 Ejemplo 4: 2x² - x - 5 = 0")
g2 = lambda x: math.sqrt((x+5)/2)
punto_fijo(g2, x0=2)
