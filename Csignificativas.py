def cifras(n):
    return len(n.replace(".", "").lstrip("0"))

n1 = input("Número 1: ")
n2 = input("Número 2: ")

a = float(n1)
b = float(n2)

op = input("Operación (+ - * /): ")

cs = min(cifras(n1), cifras(n2))

if op == "+":
    r = round(a + b, min(len(n1.split(".")[-1]), len(n2.split(".")[-1])))
elif op == "-":
    r = round(a - b, min(len(n1.split(".")[-1]), len(n2.split(".")[-1])))
elif op == "*":
    r = round(a * b, cs - 1)
elif op == "/":
    r = round(a / b, cs - 1)
else:
    print("Operación no válida")
    exit()

print("Resultado:", r)
print("Cifras significativas:", cs)