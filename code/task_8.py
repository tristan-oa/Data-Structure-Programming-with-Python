# A function which validates the input entered by the user such that the user is informed
# and requested to re-enter a value if characters or numbers less than 0 are inputted.
# This function has no parameters passed to it but returns 2 float and 1 int values
def user_input():

    # A while loop which runs indefinitely
    while True:

        # Section of code which handles exceptions
        try:

            # Converts to the float data type and stores the value entered by the user
            a = float(input("\nEnter a value to approximate its square root: "))

            # Checks if the value entered fits in a particular range before proceeding
            assert (a >= 0)

            # Converts to the float data type and stores the value entered by the user
            b = float(input("\nEnter an approximate answer you think is correct: "))

            # Converts to the integer data type and stores the value entered by the user
            c = int(input("\nEnter the number of approximations required: "))

            # If all checks are successful, the values entered are returned
            return a, b, c

        # Informs the user if anything other than a number is inputted
        except ValueError:
            print("Invalid input!")

        # Informs the user that a particular range of numbers is valid only
        except AssertionError:
            print("Number must be greater than or equal to 0")


# A function taking only 1 parameter which substitutes the values of 'a' and 'n'
# based on what the user entered and returns a float value back
def function(a):
    f1 = (a ** 2) - n
    return f1


# A function which is simply the derivative of the above function
# It takes the same parameter as the previous one and also returns a float
def derivative(a):
    f2 = 2 * a
    return f2


# The function which actually computes a Newton Raphson Approximation
# based on values returned from the 'function()' and 'derivative()' methods
# This also has the parameter 'a' passed in and returns a float value
def next_approx(a):
    a = a - (function(a) / derivative(a))
    return a


print("This program will find the approximation to the square root of a given number 'n'.")

# The inputs entered by the user are validated in the user_input() function
# These are then returned and stored in the variables a, b & c respectively
n, x, m = user_input()

# The Newton-Raphson Method is iterated for 'm' times and
# the user is informed on the updated value each time
for i in range(m):
    x = next_approx(x)
    print("\nAfter approximation #", i+1, "the answer is:", x)
