# A function which implements the Fibonacci Sequence using a non-recursive method
# The nth integer of the sequence to be printed out is passed as a parameter and
# the values coming out of this list are returned one after the other
def fibonacci(num):

    # These 2 variables are initialised
    n1 = 0
    n2 = 1

    # A for loop to determine the next integer in the sequence
    for i in range(num):
        n1, n2 = n2, n1 + n2

    # The next integer in the sequence found is returned
    return n1


print("This program will display the Fibonacci Sequence.")

# User input is entered, converted to an int variable and stored in n
n = int(input("Please enter the position of the last integer of the sequence to be printed out: "))


print("\n\n\tThe Fibonacci Sequence up till the integer in position", n)
print("-------------------------------------------------------------------------------")

# A for loop which iterates through the sequence whilst calling the fibonacci() function each time
for count in range(1, n + 1):
    print(fibonacci(count))

