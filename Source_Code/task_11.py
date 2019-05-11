# Importing the module 'math' to be able to use mathematical functions
import math


# A function which computes the Cosine maclaurin's series expansion
# This takes the angle x as the first parameter and n as the nth term to be computed
# The answer of this expansion is then returned back
def cosine(x, n):

    # This variable is initialised to 0
    answer = 0

    # This section of code iterates through each individual term in the cosine series
    # expansion, each time adding the value obtained to the answer variable
    for i in range(n+1):

        answer += (((-1)**i)*(x**(2*i)))/math.factorial(2*i)

    # The final answer for a given expansion is returned back
    return answer


# A function which computes the Sine maclaurin's series expansion
# This takes the angle x as the first parameter and n as the nth term to be computed
# The answer of this expansion is then returned back
def sine(x, n):

    # This variable is initialised to 0
    answer = 0

    # This section of code iterates through each individual term in the sine series
    # expansion, each time adding the value obtained to the answer variable
    for i in range(n+1):

        answer += (((-1)**i)*(x**((2*i)+1)))/(math.factorial((2*i)+1))

    # The final answer for a given expansion is returned back
    return answer


# Values for the angle and the final term to be computed for the cosine expansion are entered and stored
print("This program will calculate the Maclaurin Expansion of cos(x).")
value1 = int(input("Enter a value for x in degrees: "))
upper1 = int(input("Enter the position of the last term of this expansion you want to compute: "))

# The cosine() function previously defined is called and the answer is printed on the screen
print("The answer of cos(" + str(value1) + ") from 0 to " + str(upper1) + " is:", cosine(value1, upper1))
print("\n-------------------------------------------------------\n")

# Values for the angle and the final term to be computed for the sine expansion are entered and stored
print("This program will calculate the Maclaurin Expansion of sin(x).")
value2 = int(input("Enter a value for x in degrees: "))
upper2 = int(input("Enter the position of the last term of this expansion you want to compute: "))

# The sine() function previously defined is called and the answer is printed on the screen
print("The answer of sin(" + str(value2) + ") from 0 to " + str(upper2) + " is:", sine(value2, upper2))
