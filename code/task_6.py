# Importing the module 'math' to be able to use mathematical functions
import math


# A function which checks if a number is prime and returns True or False
# The only parameter is the actual number being checked
def check_if_prime(num):

    # This section of code checks if the number is one, if not divides
    # the number each time by a set of numbers starting from 2 until a
    # the remainder from a division is found to be 0
    # If neither checks are true, then number is prime and user is informed
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True


# A function which implements the sieve of eratosthenes algorithm
# The number up till which the algorithm will check for prime numbers
# is passed as a parameter and the list of prime numbers evaluated
# from this algorithm is returned back as a list
def sieve_of_eratosthenes(num):

    # Initialisation of empty list
    table = []

    # All the numbers starting from the first prime up till the final
    # number to be checked are appended to the list
    for n in range(2, num+1):
        table.append(n)

    # The limit for the next loop is set as the square root of the
    # last integer to be evaluated
    limit = int(math.sqrt(num)) + 1

    # This section iterates through all the numbers in the table list
    # and if an integer present there is found to not be prime, it is
    # removed along with all of its factors
    for n in range(2, limit):
        if n in table:
            for m in range(n+n, num+1, n):
                if m in table:
                    table.remove(m)
        n += 1

    # The remaining numbers in the table list are returned
    return table


print("This program will check if a number is prime.")

# The number to be checked if prime is entered, converted to an int and stored
check = int(input("Please enter the number to be checked: \n"))

# The check_if_prime() function is called and a 'True' or 'False" are returned
print(check_if_prime(check))

print("\n-----------------------------------------------------\n")

print("Now, the Sieve of Eratosthenes Algorithm will be implemented.")

# The last number to be evaluated in the sieve algorithm is inputted,
# converted to an int and stored
last = int(input("Enter the last number to be checked if it is prime: "))

print("\nThe following numbers are all prime: ")

# The sieve_of_eratosthenes() function is called and a list is returned
print(sieve_of_eratosthenes(last))

