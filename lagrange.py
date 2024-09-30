from art import tprint


def lagrange(x, y, x_test):
    n = len(x)
    res = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= (x_test - x[j])/(x[i] - x[j])
        res += p*y[i]
    return res


def main():
    tprint("\nLagrange Method")
    n = int(input("Enter the number of data points: "))
    x = []
    y = []
    for i in range(n):
        x.append(float(input(f"Enter x{i+1}: ")))
        y.append(float(input(f"Enter y{i+1}: ")))

    x_test = float(
        input("Enter the value of x for which you want to estimate y: "))
    result = lagrange(x, y, x_test)

    print(f"f({x_test}) = {result}")
