lista_B = [3, 2, 4, 3.6]
lista_Q = [12, 20, 13, 30]

for i in range(len(lista_B)):
    b = lista_B[i]
    q_buscada = lista_Q[i]
    
    h = b / 2
    
    print("--- Calculando para B =", b, "y Q =", q_buscada, "---")
    
    for vuelta in range(1, 11):
        q_actual = 3.33 * (b - 0.2 * h) * (h**3)**0.5
        
        pendiente = 3.33 * (1.5 * b * (h**0.5) - 0.5 * (h**1.5))
        
        error = q_actual - q_buscada
        h = h - (error / pendiente)
        
        print("Iteracion", vuelta, ": H =", h)

    print("RESULTADO FINAL: H =", h)
    print("---------------------------------------")