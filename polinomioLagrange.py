import sympy as sp
from tabulate import tabulate


def lagrange_directo():
    sp.init_printing(use_unicode=True)
    x = sp.Symbol("x")

    grado = int(input("Introduce el grado del polinomio (n): "))
    num_puntos = grado + 1

    X, Y = [], []
    for i in range(num_puntos):
        x_val = float(input(f"x_{i}: "))
        y_val = float(input(f"y_{i}: "))
        X.append(int(x_val) if x_val.is_integer() else x_val)
        Y.append(int(y_val) if y_val.is_integer() else y_val)

    print("\nTABLA DE VALORES:")
    print(
        tabulate(
            [[i, X[i], Y[i]] for i in range(num_puntos)],
            headers=["i", "X_i", "Y_i"],
            tablefmt="grid",
        )
    )

    L = []
    print("\nTÉRMINOS L_i(x):")
    for i in range(num_puntos):
        num_factores = [x - X[j] for j in range(num_puntos) if i != j]

        denominador = 1
        for j in range(num_puntos):
            if i != j:
                denominador *= X[i] - X[j]

        numerador_expresion = sp.Mul(*num_factores)
        L_i = numerador_expresion / denominador
        L.append(L_i)

        print(f"\nL_{i}(x) =")
        sp.pprint(sp.simplify(L_i), use_unicode=True)

    P_x = sum(Y[i] * L[i] for i in range(num_puntos))
    polinomio_final = sp.poly(P_x, x).as_expr()

    print("\n" + "=" * 40)
    print("POLINOMIO FINAL P(x):")
    print("=" * 40)
    sp.pprint(polinomio_final, use_unicode=True)
    print("=" * 40)

if __name__ == "__main__":
    lagrange_directo()