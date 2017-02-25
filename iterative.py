from decimal import *

# fxs are functions for the unknowns (e.g. x1 = x2 + x3)
def iterative(method, precision, epsilon, *fxs):
    getcontext().prec = precision
    getcontext().rounding = ROUND_HALF_UP

    unknowns = len(fxs)

    xs = [Decimal(0) for i in range(unknowns)]
    xs_old = [Decimal(0) for i in range(unknowns)]

    initial = True

    while (initial or not isAllConverging(xs, xs_old, epsilon)):
        initial = False
        xs_old = xs.copy()

        for i in range(unknowns):
            if (method == "j"): # Jacobi's method
                x = (fxs[i])(xs_old)
            elif (method == "g"): # Gauss-Seidel method
                x = (fxs[i])(xs)
            else:
                raise ValueError("Unknown iterative method.")

            xs[i] = x
            print("x" + str(i+1) + " = " + str(x) + ", ", end='')

        print()

    print("======================================================")

def isConverging(a, b, epsilon):
    return abs(a - b) <= Decimal(epsilon)

def isAllConverging(xs, xs_old, epsilon):
    assert(len(xs) == len(xs_old))

    for i in range(len(xs)):
        if (not isConverging(xs[i], xs_old[i], epsilon)):
            return False

    return True


if __name__ == "__main__":
    print("**Jacobi:")
    iterative("j", 4, 0.001,
              lambda xs: (-xs[1] + xs[2] + Decimal(17)) / Decimal(20),
              lambda xs: (xs[0] + xs[2] - Decimal(13)) / Decimal(10),
              lambda xs: (xs[0] - xs[1] + Decimal(18)) / Decimal(10))
    print("**Jacobi:")
    iterative("j", 4, 0.001,
              lambda xs: (xs[1] + Decimal(1)) / Decimal(3),
              lambda xs: (xs[0] + xs[2]) / Decimal(3),
              lambda xs: (xs[1] + xs[3] + Decimal(1)) / Decimal(3),
              lambda xs: (xs[2] + Decimal(1)) / Decimal(3))

    print("**Gauss-Seidel:")
    iterative("g", 4, 0.001,
              lambda xs: (-xs[1] + xs[2] + Decimal(17)) / Decimal(20),
              lambda xs: (xs[0] + xs[2] - Decimal(13)) / Decimal(10),
              lambda xs: (xs[0] - xs[1] + Decimal(18)) / Decimal(10))
    print("**Gauss-Seidel:")
    iterative("g", 4, 0.001,
              lambda xs: (xs[1] + Decimal(1)) / Decimal(3),
              lambda xs: (xs[0] + xs[2]) / Decimal(3),
              lambda xs: (xs[1] + xs[3] + Decimal(1)) / Decimal(3),
              lambda xs: (xs[2] + Decimal(1)) / Decimal(3))
