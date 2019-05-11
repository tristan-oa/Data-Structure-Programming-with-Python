# importing the module 'random' to be able to generate random numbers
import random


# A function which validates the input entered by the user such that the user is informed
# and requested to re-enter a value if characters or numbers less than 256 are inputted.
# This function has no parameters passed to it but returns an integer value
def user_input():

    # A while loop which runs indefinitely
    while True:

        # Section of code which handles exceptions
        try:

            # Converts to the integer data type and stores the value entered by the user
            x = int(input("\nEnter the max amount of integers in the list: "))

            # Checks if the value entered fits in a particular range before proceeding
            assert(x >= 256)

            # If all checks are successful, the value entered is returned
            return x

        # Informs the user if anything other than an integer is inputted
        except ValueError:
            print("Invalid input!")

        # Informs the user that a particular range of numbers is valid only
        except AssertionError:
            print("Number must be greater than or equal to 256")


# A function which simply populates an array based on the 2 parameters passed.
# The first parameter is the size of the array entered by the user and the second
# is the actual array to be populated. Nothing is returned back
def populate_array(x, array):

    # A for loop which loops through each individual empty element in the array
    # and populates it
    for i in range(x):

        # Generates a random number from 0-1024 each time and stores it in the array
        array.append(random.randint(0, 1024))


# The main function for a shell sort which also calls the 'split_list()' function.
# This takes 2 parameters which are the array size and the array itself and returns nothing
def shell_sort(x, array):

    # The approximate middle position of the list is determined and stored
    skip = x // 2

    # Loops as long as skip > 0
    while skip > 0:

        # Loops up to the splitting factor
        for i in range(skip):

            # Calls the split_list() function with the appropriate parameters passed
            split_list(array, i, skip, x)

        # Displays the list being sorted in stages whilst halving the skip value each time
        print(skip, "\t\t\t", array)
        skip = skip // 2


# The sub-function for the shell sort which compares and sorts the list.
# This has 4 parameters passed into it but returns nothing. The first is the array
# to be sorted, the second the starting element to be compared, the third the amount
# of integers to be skipped each time and the fourth, the length of the list
def split_list(array, start, skip, x):

    # Loops through the list to compare and sort
    for i in range(start + skip, x, skip):

        # Initialising of 2 new variables. val stores the array value at position i
        # and j stores the index of the current iteration
        val = array[i]
        j = i

        # Loops as long as the value being skipped <= j and the integer stored in val
        # is less than another integer being compared to
        while skip <= j and val < array[j-skip]:

            # Shifts the smaller number to take the larger number's place
            array[j] = array[j-skip]
            j = j-skip

        # Shifts the larger number in its new appropriate position
        array[j] = val


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

        # List-related information is printed out to the user in stages
        # as the list gets sorted
        print("\nSplitting Factor:\t\t", array[split])
        print("Smaller or equal to:  \t", array[start:split])
        print("Larger: \t\t\t\t", array[split+1:])

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


# The 2 empty lists to be populated and sorted are initialised here
array_a = []
array_b = []

print("\t\t\t\t\t\tARRAY A")
print("----------------------------------------------------------\n")

# Placeholder length1 stores the value entered by the user after validation
length1 = user_input()

# The 1st array is populated when populate_array() function is called
populate_array(length1, array_a)

# The 1st array is displayed to the user
print("Array A: ", array_a)

print("\n\t\t\t\t\t\tARRAY B")
print("----------------------------------------------------------\n")

# Placeholder length2 stores the value entered by the user after validation
length2 = user_input()

# Ensures that the 2 lists created are not of equal length
while length1 == length2:
    print("The different arrays cannot be of the same size")
    length2 = user_input()

# The 2nd array is populated when populate_array() function is called
populate_array(length2, array_b)

# The 2nd array is displayed to the user
print("Array B: ", array_b)

print("\n\t\t\t\tSorting array A using Shell Sort")
print("----------------------------------------------------------------------------------------------\n")
print("Original Array A: ", array_a)
print("\nGap Size |\t Current list")

# The shell_sort() funtion is called which sorts the list
shell_sort(length1, array_a)

print("\n\t\t\t\tSorting array B using Quick Sort")
print("----------------------------------------------------------------------------------------------\n")
print("Original Array B: ", array_b)

# The quick_sort() function is called which sorts the list
quick_sort(array_b, 0, length2-1)
print("\nSorted Array B: ", array_b)
