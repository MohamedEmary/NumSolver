import numpy as np
from art import tprint


def interpolate_at(coef, x, x_test, round_to):
    """Interpolate at a point using Newton's divided difference coefficients.
    Args:
        coef (numpy.ndarray): Newton's divided difference coefficients.
        x (numpy.ndarray): x values.
        x_test (float): The value of x to interpolate at.
        round_to (int): The number of decimal places to round to.
    """
    f_x = coef[0]
    for i in range(1, len(coef)):
        temp = coef[i]
        for j in range(i):
            temp *= (x_test - x[j])
        f_x += temp
    print(f"\nf({x_test}) = {round(f_x, round_to)}")


def newton_divided_difference(x, y, round_to):
    """Find the coefficients of Newton's divided difference.
    Also, find Newton's polynomial.
    Args:
        x (numpy.ndarray): x values.
        y (numpy.ndarray): y values.
    Returns:
        f (numpy.ndarray): Newton's divided difference coefficients.
    """
    n = x.size
    q = np.zeros((n, n - 1))

    # Insert 'y' in the first column of the matrix 'q'
    q = np.concatenate((y[:, None], q), axis=1)

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (x[i] - x[i - j])

    # Copy the diagonal values of the matrix q to the vector f
    f = np.zeros(n)
    for i in range(0, n):
        f[i] = q[i, i]

    print("The polynomial is:")
    print(f"p(x)={f[0]:+.{round_to}f}", end="")  # :
    for i in range(1, n):
        if f[i] == 0:
            continue
        print(f"{f[i]:+.{round_to}f}", end="")
        for j in range(1, i + 1):
            print(f"(x{(x[j-1] * -1):+.{round_to}f})", end="")
    print("")
    return f.round(round_to)


def main():
    tprint("\nDivided difference")
    points_number = int(input("Enter the number of points: "))
    x, y = np.zeros(points_number), np.zeros(points_number)
    x = np.array(x)
    y = np.array(y)
    for i in range(points_number):
        print(f"Point {i + 1}: ")
        x[i] = float(input("Enter x: "))
        y[i] = float(input("Enter y: "))
    round_to = int(
        input("\nEnter the number of decimal places to round to if no just enter 99: "))
    x_test = int(
        input("\nEnter the value of x to find the value of f(x) at: "))

    print()
    print('=' * 50)
    coef = newton_divided_difference(x, y, round_to)
    interpolate_at(coef, x, x_test, round_to)
    print('=' * 50)
