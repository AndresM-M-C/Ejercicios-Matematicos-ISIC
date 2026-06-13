numero_input = input("Ingresa un número: ")

cifras_limpias = numero_input.replace('.', '').lstrip('0')
cantidad = len(cifras_limpias)

print(f"El número {numero_input} tiene {cantidad} cifras significativas.")