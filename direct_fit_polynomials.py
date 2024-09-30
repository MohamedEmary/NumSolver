import numpy as np
from art import tprint


def get_coefficients(x: np.ndarray, y: np.ndarray, degree: int, decimal_places: int):
    '''Get the coefficients of the polynomial using direct fit method.
    Args:
        x (numpy.ndarray): The x values of the points.
        y (numpy.ndarray): The y values of the points.
        degree (int): The degree of the polynomial.
        decimal_places (int): The number of decimal places to round to.
    Returns:
        coefficients (numpy.ndarray): The coefficients of the polynomial.
    '''
    X = np.zeros((degree+1, degree+1))

    # prepare the matrix X which is a list of column vectors of
    # the form [x^0, x^1, x^2, ..., x^degree]
    X = [[x[i]**(j) for j in range(degree+1)] for i in range(degree+1)]

    # solve the system of linear equations using matrix inversion method
    # X * coefficients = y
    # coefficients = X^-1 * y
    # get the inverse of X and multiply it by y
    X = np.linalg.inv(X)
    coefficients = np.dot(X, y)
    return coefficients.round(decimal_places)


def interpolate_at(coefficients: np.ndarray, x_value: float, decimal_places: int):
    '''Interpolate at a point using Newton's divided difference coefficients.
    Args:
        coefficients (numpy.ndarray): Newton's divided difference coefficients.
        x_value (float): The value of x to interpolate at.
        decimal_places (int): The number of decimal places to round to.
    Returns:
        y_value (float): The value of y at the specified x value.
    '''
    y_value = coefficients[0]
    for i in range(1, len(coefficients)):
        y_value += coefficients[i] * x_value**i
    return y_value.round(decimal_places)


def get_input_points(degree: int):
    '''Get the x and y values of the points from the user
    Args:
        degree (int): The degree of the polynomial.
    Returns:
        x (numpy.ndarray): The x values of the points.
        y (numpy.ndarray): The y values of the points.
    '''

    y, x = [], []

    for i in range(degree+1):
        print(f"Point {i+1}: ")
        x.append(float(input("Enter x: ")))
        y.append(float(input("Enter y: ")))

    x = np.array(x)
    y = np.array(y)
    return x, y


def print_equation(coefficients: list, degree: int):
    '''Print the equation of the polynomial
    Args:
        coefficients (list(float)): The coefficients of the polynomial.
        degree (int): The degree of the polynomial.
    '''
    coefs = []
    for i in range(degree+1):
        # if the coefficient is negative enclose them in parentheses it to avoid the case
        # where the negative and positive signs come next to each other like: x^2 + -2x + 1 = 0
        if coefficients[i] < 0:
            coefs.append(f"({coefficients[i]})")
        else:
            coefs.append(f"{coefficients[i]}")
    print("The polynomial equation is: ")
    for i in range(degree, 0, -1):
        print(f"{coefs[i]}x^{i} + ", end="")
    print(f"{coefs[0]} = 0")


def main():
    tprint("\nDirect Fit Method")
    degree = int(input("Enter the degree of the polynomial you want to get: "))

    print(f"You will have to enter {degree+1} points on the graph.")

    x, y = get_input_points(degree)

    print("\nDo you want the coefficients rounded or not? ")
    print("If yes enter the number of decimal places you want the coefficients to be rounded to.")
    decimal_places = int(input("And if no just enter 99: "))
    x_interpolate = float(input("Enter the value of x to interpolate at: "))

    print("\n", "="*50, sep="")
    coefficients = get_coefficients(x, y, degree, decimal_places)
    print_equation(coefficients, degree)
    y_interpolate = interpolate_at(coefficients, x_interpolate, decimal_places)
    print(f"P{degree}({x_interpolate}) : {y_interpolate}")
    print("="*50, "\n")
