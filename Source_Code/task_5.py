# This module is imported to be able to make use of specific
# operator functions listed in the operators dictionary below
import operator


# A class which defines basic stack operations including an
# additional __str__() function to be able to print out the stack
class Stack:

    # A constructor function which defines the stack being used
    def __init__(self):
        self.items = []

    # A function which allows items to be pushed onto the stack
    def push(self, info):
        self.items.append(info)

    # A function which allows items to be popped off the stack
    def pop(self):
        return self.items.pop()

    # A function which returns the string representation of the
    # object created
    def __str__(self):
        return str(self.items)


# An 'operators' dictionary which associates actual operators to
# binary operator functions imported from the operator module
operators = {"+":  operator.add,
             "-":  operator.sub,
             "*":  operator.mul,
             "/":  operator.truediv}


# The function which does the evaluation of the RPN arithmetic
# It takes in a formula as the only argument and returns back a
# popped variable. This is a recursive function
def rpn(formula):

    # An instance 'storage' of the 'Stack()' class is created
    # to be able to make use of 'Stack()' functions
    storage = Stack()

    # The formula to be evaluated is split up
    elements = formula.split()

    # A for loop which loops through the split up elements
    for element in elements:

        # The arithmetic operator going to affect any values on the stack
        print("\nCurrent element:\t\t", element)

        # The stack contents are displayed before the operation
        print("Stack contents BEFORE:", storage)

        # If an element present is found in the operators dictionary,
        # '+'/'-'/'*'/'/' is performed on the last 2 elements pushed
        # onto the stack. These are then popped off the stack, evaluated
        # and the result is then popped back onto the stack
        if element in operators:

            # The last 2 elements present in the stack are popped
            # and stored in variables
            num2 = storage.pop()
            num1 = storage.pop()

            # The result is then computed
            result = operators[element](num1, num2)

            # the result is then pushed back onto the stack
            storage.push(result)
        else:

            # else, the element found is an integer and not an operator,
            # so it is pushed onto the stack
            storage.push(int(element))

        # The stack contents are displayed after the operation
        print("Stack contents AFTER: ", storage)

    # The last value on the stack is popped off at the end
    return storage.pop()


# Driver code which tests the rpn calculator
print("\n\n\nThe final answer is :", rpn("15 6 8 * 2 + +"))
