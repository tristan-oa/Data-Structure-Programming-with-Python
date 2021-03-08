# importing the module 'random' to be able to generate random numbers
import random


# A function which validates the input entered by the user such that the user is informed
# and requested to re-enter a value if characters or a number less than 4 is inputted.
# This function has no parameters passed to it but returns an integer value
def user_input():

    # A while loop which runs indefinitely
    while True:

        # Section of code which handles exceptions
        try:

            # Converts to the integer data type and stores the value entered by the user
            x = int(input("\nEnter the max amount of integers in the list: "))

            # Checks if the value entered fits in a particular range before proceeding
            assert(x >= 4)

            # If all checks are successful, the value entered is returned
            return x

        # Informs the user if anything other than an integer is inputted
        except ValueError:
            print("Invalid input!")

        # Informs the user that a particular range of numbers is valid only
        except AssertionError:
            print("Number must be greater than or equal to 4")


# A function which simply populates an array based on the 2 parameters passed.
# The first parameter is the size of the array entered by the user and the second
# is the actual array to be populated. Nothing is returned back
def populate_array(x, arr):

    # A for loop which loops through each individual empty element in the array
    # and populates it
    for i in range(x):

        # Generates a random number from 1-1024 each time and stores it in the array
        arr.append(random.randint(1, 1024))


# A function which determines all possible 2-pairs of integers having the same product
# The first parameter is the size of the array entered by the user and the second
# is the actual array to be populated. Nothing is returned back
def pairs(x, arr):

    # A counter variable which is initialised to 0
    h = 0

    # 4 for loops which loop through all the numbers in the list for 4 times, each time
    # searching for all possible 2-pair configurations
    # Any configurations found are printed out and the counter variable 'h' is incremented
    for i in range(x):
        for j in range(x):
            for k in range(x):
                for l in range(x):

                    # An if statement which checks for all possible 2-pairs of integers having the same
                    # product while ensuring that in the pairs found, arr[i] ≠ arr[j] ≠ arr[k] ≠ arr[l]
                    if ((arr[i] * arr[j] == arr[k] * arr[l]) and (arr[i] != arr[j]) and (arr[i] != arr[k]) and
                            (arr[i] != arr[l]) and (arr[j] != arr[k]) and (arr[j] != arr[l]) and (arr[k] != arr[l])):
                        print(arr[i], "X", arr[j], "=", arr[k], "X", arr[l])
                        h += 1

    # The user is informed of the amount of 2-pairs found
    print("\nA total of", h, "2-pairs of integers were found.")


# An array is initialised as empty
numbers = []

# Placeholder 'a' stores the value entered by the user after validation
a = user_input()

# The size entered by the user and stored in placeholder 'a' together
# with the newly created array are passed as parameters to the function
# populate_array() which then fills the list with random integers
populate_array(a, numbers)

# The list is then printed out
print("Generated List:\n", numbers)

# The function pairs() is then called with the appropriate parameters passed
pairs(a, numbers)
