contador_pares = 0

for i in range(2, 101):
    if i % 2 == 0:
        print(f"{i:2d}", end=" ")
        contador_pares += 1
        if i % 20 == 0:  
            print()

print(f"\nCantidad de números pares: {contador_pares}")