from art import tprint
import numpy as np


def main():
    tprint("\nLeast Squares")
    N = int(input("Enter the total number of data points: "))
    X = np.zeros(N)
    Y = np.zeros(N)

    print("-------------Enter the X values----------------")
    for i in range(N):
        val = float(input("X" + str(i) + ": "))
        X[i] = val

    print("-------------Enter the Y values----------------")
    for i in range(N):
        val = float(input("Y" + str(i) + ": "))
        Y[i] = val

    X = np.array(X)
    Y = np.array(Y)

    print("-----------------------------------------------")
    print(f"X : ", X)
    print(f"Y : ", Y)
    deg = int(input("Enter the degree of the polynomial : "))
    round_to = int(input("Enter the number of decimal places to round to: "))
    # calculate X,X^2 ,X^3,..and so on that we need in the equations.
    # calculate summation of X,X^2 ,X^3,..and so on that we need in the equations.
    powerx = [X]
    sum1 = [np.sum(X)]
    for i in range(1, deg*2):
        powerx.append(powerx[i-1] * X)
        sum1.append(np.sum(powerx[i]))
    # print the array of X.
    for i in range(0, deg*2):
        print(f"X^{i + 1} :", powerx[i])
        print(f"Sum X^{i + 1} :", sum1[i])

    # calculate Y,YX , YX^2,..and so on that we need in the equations.
    # calculate summation of Y,YX , YX^2,..and so on that we need in the equations.
    poweryx = [Y]
    sum2 = [np.sum(Y)]
    for i in range(1, deg+1):
        poweryx.append(poweryx[i-1] * X)
        sum2.append(np.sum(poweryx[i]))
    print("----------------------------------------------")
    # print the array of YX.
    for i in range(0, deg+1):
        print(f"YX^{i} :", poweryx[i])
        print(f"Sum YX^{i} :", sum2[i])
    print("-------------------------------------------------")
    n = deg+1
    m = deg+1
    matrix_A = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                matrix_A[i, j] = N
            else:
                matrix_A[i, j] = sum1[i+j-1]
    print(f" matrix_A :\n {matrix_A}")

    print("---------------------------------------------------")

    # Results matrix B
    n = deg+1
    m = 1
    matrix_B = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            matrix_B[i, j] = sum2[i+j]
    print(f" matrix_B :\n {matrix_B}")

    # solve the equations by invert matrix_A and maltiply it in matrix_B.
    matrix_A = np.linalg.inv(matrix_A)
    coeff = np.dot(matrix_A, matrix_B)
    coefficients = coeff.flatten()
    for i in range(len(coefficients)):
        if abs(coefficients[i])-0 < 1e-8:
            coefficients[i] = 0
    print("--------------------------------------------------------")
    print("Coefficients are :")
    for i in range(deg+1):
        print(f"a{i} = {coefficients[i].round(round_to)}")
    print("--------------------------------------------------------")
    # Form the polynomial equation
    p = np.poly1d(coefficients[::-1].round(round_to))
    print(f"The polynomial equation is:\n {p} = 0")
    print("--------------------------------------------------------")
    # find the value of y at any point.
    D1 = int(input(
        "Do You Want To Find The Value Of Y At Any Point ? :\nEnter (1) if Yes And (0) If No: "))
    if D1 == 1:
        x = float(input("Enter the value of x: "))
        # Calculate the value of p at the given x value
        result = p(x)
        print(f"f({x}) = {result.round(round_to)}")
    print("--------------------------------------------------------")
    D2 = int(input(
        "Do You Want To Find The derivative Of the polynomail ? :\nEnter (1) if Yes And (0) If No: "))
    if D2 == 1:
        # Find the derivative of the polynomial.
        p_derivative = np.polyder(p)
        print("The Derivative Of The Polynomial Is: ")
        print(p_derivative)
    print("--------------------------------------------------------")
    D3 = int(input(
        "Do You Want To Find The integration Of the polynomail ? :\nEnter (1) if Yes And (0) If No: "))
    if D3 == 1:
        # Find the Unlimited integration of the polynomial.
        p_integration = np.polyint(p)
        print("The Integration Of The Polynomial Is:")
        print(p_integration, "+ c")
