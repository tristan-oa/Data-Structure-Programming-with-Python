# The previous task_1 python file used for task 1 is now imported
# Any functions previously defined in the task_1 python file can now be
# accessed from this file
# Also, any previous operations performed like declaration of arrays and
# the actual sorting of these arrays will still be done in this file
# giving the illusion that such operations where actually coded in this file
import task_1


# The function used to merge array_a and array_b into a newly created array_c
# This function takes 4 parameters with the first 2 being the 2 arrays to be
# merged and the last 2 being their respective sizes
# Nothing is returned back as a result of calling this function
def merge(array1, array2, size1, size2):

    # The new array C is created with the sizes of both arrays A and B
    # together and each entry of the array is initialised to 0
    array_c = [None] * (size1 + size2)

    # Counter variables for arrays A, B & C respectively are set to 0
    a = 0
    b = 0
    c = 0

    # A while loop which runs until the end of both lists A & B is reached
    while a < size1 and b < size2:

        # If the an element stored in A is less than that stored in B,
        # this is stored in C and both counters for a and c are incremented
        if array1[a] < array2[b]:
            array_c[c] = array1[a]
            c += 1
            a += 1

        # else, the element at B is stored in C and both counters for
        # b and c are incremented
        else:
            array_c[c] = array2[b]
            c += 1
            b += 1

    # Any remaining elements of A are stored in C
    while a < size1:
        array_c[c] = array1[a]
        c += 1
        a += 1

    # Any remaining elements of B are stored in C
    while b < size2:
        array_c[c] = array2[b]
        c += 1
        b += 1

    # The merged array C is then printed
    print("\n\nMerged Array C: \t", array_c)


# The merge() function is called with the 4 appropriate parameters passed
# Each parameter contains a "task_1." prefix which causes the program
# to refer to the 'task_1' python file and obtain the arrays and lengths
# required from that file
merge(task_1.array_a, task_1.array_b, task_1.length1, task_1.length2)
