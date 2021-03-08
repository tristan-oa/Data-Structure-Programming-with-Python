# importing the module 'random' to be able to generate random numbers
import random


# A function which validates the input entered by the user such that the user is informed
# and requested to re-enter a value if characters are inputted instead of numbers.
# This function has no parameters passed to it but returns 3 integer values
def user_input():

    # A counter variable is initialised to 1
    i = 1

    # A while loop which runs indefinitely
    while True:

        # Section of code which handles exceptions
        try:

            # This section of code runs again each time until correct input is entered by the
            # user and accepted by the program thus increasing the value of i to 2
            if i is 1:
                x = int(input("\nEnter the max amount of integers in the list: "))
                i += 1
                continue

            # This section of code runs again each time until correct input is entered by the
            # user and accepted by the program thus increasing the value of i to 3
            elif i is 2:
                y = int(input("\nEnter the min value an integer present in the list can have: "))
                i += 1
                continue

            # This section of code runs again each time until correct input is entered by the
            # user and accepted by the program thus increasing the value of i to 4
            elif i is 3:
                z = int(input("\nEnter the max value an integer present in the list can have: "))
                i += 1
                continue

            # The user is informed in this part that all inputs were correct and these
            # values are then returned back
            elif i is 4:
                print("All inputs were successfully stored and the list is shown below:\n")
                return x, y, z

        # Informs the user if anything other than an integer is inputted
        except ValueError:
            print("Invalid input!")


# A function which based on the 3 parameters passed (size of list, min value in list and
# max value in list) which were previously entered by the user, generates a list of randoms
# These numbers are then stored in an array which is passed as the final parameter and
# returned back at the end of the function
def generate_list(x, y, z, numbers):

    # A for loop which loops through each individual empty element in the array
    # and populates it
    for i in range(x):

        # Generates a random number from y-z each time and stores it in the array
        numbers.append(random.randint(y, z))

    # The generated list is returned
    return numbers


# The main function for a quick sort which also calls the 'partition()' function.
# This is a recursive function taking 3 parameters which are the array to be sorted,
# the starting position and ending position for the sorting procedure.
# This function does not return anything.
def quick_sort(array, start, end):

    # Statement runs if the end of the list is not yet reached
    if start < end:

        # The value returned from the sub-function being called is stored in
        # the placeholder split
        split = partition(array, start, end)

        # The recursive part of the function which proceeds to sorting 2 smaller
        # sections of the list separated by the split variable
        quick_sort(array, start, split-1)
        quick_sort(array, split+1, end)


# The sub-function of the quick sort which switches different numbers in the
# list to be sorted based on the pin. This takes 3 parameters:
# the array to be sorted, the starting and ending point.
# This function returns the value stored in i which determines the split
# for the next iteration
def partition(array, start, end):

    # Sets the pin to be the one approximately in the middle of the list
    pinPosition = (start + end) // 2
    pinValue = array[pinPosition]

    # Swaps the pin with the last element in the list
    array[pinPosition], array[end] = array[end], array[pinPosition]

    # Sets the counter i to 1 less than the first position of the list
    i = start - 1

    # Loops through the list from start to end excluding the pin
    for j in range(start, end):

        # If the pin is greater than an element being compared, the
        # counter variable i is incremented and the values stored in
        # positions i and j are swapped
        if array[j] <= pinValue:
            i += 1
            array[j], array[i] = array[i], array[j]

    # i is incremented
    i += 1

    # The pin is now swapped back in it's appropriate position in the list
    array[i], array[end] = array[end], array[i]

    # The counter value i is returned
    return i


# A function which takes a sorted list (1st parameter passed) and determines the
# repeated integers. These are then added to a new list which is then displayed
# The second parameter simply defines the size of the array being passed
# Nothing is returned back
def repeat(numbers, x):

    # The array used to store the repeated numbers
    repeated = ["REPEATED NUMBERS: "]

    # The block of code which determines the repeated numbers and stores them
    # in the new list entitled 'repeated' if and only if they haven't been
    # stored there already
    for i in range(x-1):

        if (numbers[i] == numbers[i+1]) and (numbers[i] != repeated[-1]):
            repeated.append(numbers[i])

    # The list is the displayed to the user
    print("\n", repeated)


print("Welcome to this program which selects repeated numbers from a list of randomly generated integers")

# The input entered by the user for the size, min and max values of the list
# are validated in the user_input() function. These are then
# returned and stored in the variables a, b & c respectively
a, b, c = user_input()

# An empty array is initialised with dimensions as specified by the user
arr = []

# The function generate_list() is then called and the placeholders a, b, c are
# passed as parameters to this function together with the array to be filled
print("Generated List: ", generate_list(a, b, c, arr))

# The quick_sort() function is called which sorts the list
quick_sort(arr, 0, a-1)
print("\nSorted List: ", arr)

# Finally the repeat() function is called to determine the repeated integers
repeat(arr, a)
