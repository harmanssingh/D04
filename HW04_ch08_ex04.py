#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """The function just returns the status of the first letter in the word. It doesn't check whether there is any occurence
    of a lowercase letter anywhere else in the word.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """c is in 'quotes'. The function treats 'c'.islower() as : check if 'c' is lowercase, which is always true.
    So the function would always return True irrespective of what the value for the entered string is.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Flag is updated with each iteration. So the return value would just indicate if the last letter of the word is lowercase.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """The if condition is satisfied and a False value is returned if not c.islower() is True. In other words, if there is even a single
    capital letter in the word, the if condition would return False.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    any_lowercase1('Hello')
    any_lowercase2('Hello')
    any_lowercase3('HellO')
    any_lowercase5('Hello')


if __name__ == '__main__':
    main()
