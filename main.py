import direct_fit_polynomials
import divided_difference
import forward_difference
import lagrange
import least_squares_approximation
import newton
import bisection

first_call = True


def main():
    global first_call
    if first_call:
        first_call = False
        print("Welcome to NumSolver!\n")
        print("Please select the algorithm you want to use:")
        print("\t1. Direct Fit Polynomials")
        print("\t2. Bisection Method")
        print("\t3. Divided Difference")
        print("\t4. Forward Difference")
        print("\t5. Lagrange")
        print("\t6. Least Squares Approximation")
        print("\t7. Newton Raphson")

    while True:
        try:
            choice = int(
                input("\nEnter the number of the algorithm you want: "))
            if (choice >= 1 and choice <= 7):
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 7.")

        except ValueError:
            print("\nInvalid input (you didn't enter a number). Please try again.")

    if choice == 1:
        direct_fit_polynomials.main()
    elif choice == 2:
        bisection.main()
    elif choice == 3:
        divided_difference.main()
    elif choice == 4:
        forward_difference.main()
    elif choice == 5:
        lagrange.main()
    elif choice == 6:
        least_squares_approximation.main()
    elif choice == 7:
        newton.main()
    else:
        print("\nInvalid choice. Please enter a number between 1 and 6.\n")
        main()


if __name__ == "__main__":
    main()
