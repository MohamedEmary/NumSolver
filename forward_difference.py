import math
from sympy import *
from art import tprint


def ucal(u, p):
    temp = u
    for i in range(1, p):
        temp = (temp) * (u - i)
    return temp


def main():
    tprint("\nForward Difference")
    degree = int(input("Enter the degree of the polynomial you want to get: "))

    print(
        f"You will have to enter {degree+1} points on the graph 2 point to x and {degree+1} to y.")

    y, x = [], []

    for i in range(degree+1):
        print(f"Point {i+1}: ")
        if (i < 2):
            x.append(float(input("Enter x: ")))
        y.append(float(input("Enter y: ")))
    first_value = []
    temp = []
    first_value.append(y[0])
    for i in range(degree):
        print(f"the {i+1} column : {y}")
        for j in range(len(y)-1):
            temp.append(y[j+1]-y[j])
        first_value.append(temp[0])
        y.clear()
        y = temp.copy()
        temp.clear()
    print(f"the {degree+1} column : {y}")
    print("first element in all column")
    print(first_value)
    H = x[1]-x[0]
    X_of_zero = symbols('x')
    S_to_test = (X_of_zero - x[0])/H
    equation = []
    for i in range(1, degree+1):
        equation.append(((ucal(S_to_test, i))/math.factorial(i)))
    print("The 1 term in the equation :  ", first_value[0])
    for i in range(1, degree+1):
        print(
            f"The {i+1} term in the equation :  {first_value[i]} * ({equation[i-1]})")
    summ = first_value[0]
    X = float(input("Enter interpolate at X = "))
    S = (X-x[0])/H
    for i in range(1, degree+1):
        summ += first_value[i]*(ucal(S, i))/math.factorial(i)
    print(f"the value at {X} is {summ}")
