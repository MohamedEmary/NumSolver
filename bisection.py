import math
import sympy
from tabulate import tabulate
from art import tprint
import pandas as pd


def main():
    tprint("\nBisection Method")
    x = sympy.Symbol('x')

    print('To enter the function you should know the following:')
    print('1. Use \'x\' as the variable')
    print('2. Use * for multiplication')
    print('3. Use ** for exponent')
    choice = input("Now enter the function: ")

    try:
        f = sympy.lambdify(x, sympy.sympify(choice))
    except:
        print("Invalid function")
    else:
        a = float(input("Enter the lower bound of the interval: "))
        b = float(input("Enter the upper bound of the interval: "))

        tol = float(input("Enter the tolerance for the error: "))

        def bisection(a, b, tol):
            # Check if a and b have opposite signs
            if f(a) * f(b) > 0:
                print("No root in the interval")
                return None
            # Check if a or b is a root
            if f(a) == 0:
                return a
            if f(b) == 0:
                return b

            # Initialize x as the midpoint of a and b
            x = (a + b) / 2
            table = [[0, a, x, b, f(a), f(x), f(b)]]
            i = 1

            # Repeat until the interval is smaller than the tolerance
            while abs(b - a) > tol:
                # If x is a root, return it
                if f(x) == 0:
                    return x, table
                # If f(a) and f(x) have opposite signs, set b = x
                elif f(a) * f(x) < 0:
                    b = x
                else:
                    a = x

                x = (a + b) / 2
                table.append([i, a, x, b, f(a), f(x), f(b)])
                i += 1
            return x, table

        # Calculate the number of iterations by the formula n = log_2(b-a/tolerance)
        n = math.ceil((math.log2((b - a) / tol)))
        print(f"\nThe number of iterations is: {n}\n")
        root, table = bisection(a, b, tol)
        print(tabulate(table, headers=["i", "a", "x",
                                       "b", "f(a)", "f(x)", "f(b)"], floatfmt=".9f", tablefmt="simple_grid", numalign="center", stralign="center"))
        print(
            f"\nThe root of {sympy.simplify(choice)} is approximately {round(root, 5)}")

    df = pd.DataFrame(
        table, columns=["i", "a", "x", "b", "f(a)", "f(x)", "f(b)"])

    df.to_csv("bisection_table.csv", index=False)
