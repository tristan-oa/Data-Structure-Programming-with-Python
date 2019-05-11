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
# These numbers are then stored to the 'arr' array passed as the 4th parameter
def generate_list(x, y, z, arr):

    # A for loop which loops through each individual empty element in the array
    # and populates it
    for i in range(x):

        # Generates a random number from y-z each time and stores it in the array
        arr.append(random.randint(y, z))


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


# A function which finds the extreme points in an array
# It has 2 parameters passed to it (the array whose extreme points are to be found
# and the size of the array passed) but returns nothing back
def extreme(arr, x):

    # An empty list to store the extreme points is created
    points = []

    # The statement which loops through all the possible extreme points
    # (from the second to the element before the last) and adds any extreme
    # points found to the newly created array
    for i in range(1, x-1):
        if (arr[i-1] < arr[i] > arr[i+1]) or (arr[i-1] > arr[i] < arr[i+1]):
            points.append(arr[i])

    # This statement checks if any extreme points have been found
    # If none are found, the user is informed that the list is sorted
    # If not, the extreme points found are printed out to the user
    if len(points) == 0:
        print("\nSORTED")
        print("This array had no extreme points")
    else:
        print("\nThe extreme points are: ")
        print(points)


# An empty array to be randomly populated is created
arrayA = []

print("This program will print the extreme points of a given array.")

# The input entered by the user for the size, min and max values of the list
# are validated in the user_input() function. These are then
# returned and stored in the variables a, b & c respectively
a, b, c = user_input()

# The function generate_list() is then called and the placeholders a, b, c are
# passed as parameters to this function
generate_list(a, b, c, arrayA)

# The generated list is displayed to the user
print("ARRAY:", arrayA)

# The extreme() function is called with the 'arrayA' list passed as the first
# parameter and its size as the second parameter
extreme(arrayA, a)

# The quick_sort() function is called which sorts the list to show that a
# sorted list has no extreme points
# This has the 'arrayA' list passed as the 1st parameter, 0 as the 2nd and
# the length of the array - 1 as the 3rd
quick_sort(arrayA, 0, a-1)
print("\nSorted Array: ", arrayA)

# The extreme() method is called once again to prove that a sorted list
# contains no extreme points
extreme(arrayA, a)
