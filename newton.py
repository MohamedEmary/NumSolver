from sympy import symbols, sympify, diff
from tabulate import tabulate
from art import tprint
import pandas as pd


def main():
    tprint("\nNewton Raphson")
    x = symbols('x')
    print('\nTo enter the function you should know the following:')
    print('1. Use \'x\' as the variable')
    print('2. Use * for multiplication')
    print('3. Use ** for exponent')
    f = input('Now enter the function: ')
    f = sympify(f)
    print(f"\nf(x) = {f}")
    f_prime = diff(f, x)  # f'
    print(f"f'(x) = {f_prime}")
    start_point = float(input("\nEnter first point to start with: "))
    print(f"f'({start_point}) = {f_prime.subs(x, start_point)}")
    tolerance = float(
        input("\nEnter tolerance (for example if it 10^-7 just enter 7): "))
    decimal_places = int(input(
        "\nEnter number of decimal places you want the output to be printed with: "))
    X = []
    f_of_x = []
    segmet = []
    X.append(start_point)
    condition = True
    i = 0
    error = 0  # division by zero
    table = []  # table to store iteration data
    while condition:
        if (f_prime.subs(x, X[i]) == 0):
            print("Division by zero is not possible")
            error = 1
            break
        else:
            if i == 0:
                next_point = X[i]-(f.subs(x, X[i])/f_prime.subs(x, X[i]))
                X.append(next_point)
                f_of_x.append(f.subs(x, X[i]))
                table.append([i, X[i], f_of_x[i], "-"])
            else:
                next_point = X[i]-(f.subs(x, X[i])/f_prime.subs(x, X[i]))
                X.append(next_point)
                f_of_x.append(f.subs(x, X[i]))
                segmet.append(X[i]-X[i-1])
                if (f_of_x[-1] == 0 or segmet[-1] == 0 or X[-1] == X[-2] or abs(segmet[-1]) < 10**(-tolerance)):
                    condition = False
                table.append(
                    [i, X[i], f_of_x[i], round(segmet[-1], decimal_places)])
            i = i+1

    if (error == 0):
        print()
        print(tabulate(table, headers=[
            "i", "x", "f(x)", "ε"], floatfmt=f".{decimal_places}f", tablefmt="simple_grid", numalign="center", stralign="center"))
        print("\nSolution is:", round(X[-1], decimal_places))

    df = pd.DataFrame(table, columns=["i", "x", "f(x)", "ε"])
    df.to_csv("newton_table.csv", index=False)
