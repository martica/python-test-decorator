#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback
from inspect import isclass


def exception_as_string(exception):
    exceptionType, exceptionValue, exceptionTraceback = exception
    strings = traceback.format_exception_only(exceptionType, exceptionValue)
    return ''.join(strings).rstrip('\n')


def test(inputs, expected):
    def decorate(f):
        if f.__globals__["__name__"] != "__main__":
            # If the tested function is not part of the current main
            # module, the decorators are being applied to the tested
            # function in an import context. Running tests during import
            # would generate a lot of noise.
            return f

        input_string = ', '.join([repr(x) for x in inputs])
        functionString = "{}({})".format(f.__name__, input_string)
        try:
            test = expected.__name__
        except:
            test = str(expected)

        try:
            actual = f(*inputs)
        except:
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            exceptionString = exception_as_string(sys.exc_info())
            if expected == exceptionType:
                print("√ Called {}, Caught expected exception. {}".
                      format(functionString,  exceptionString))
            else:
                print("X Called {}, expected {}, Caught unexpected exception."
                      " {}".format(functionString,  test, exceptionString))
        else:
            if isclass(expected) and issubclass(expected, Exception):
                print("X Called {}, expected {}, Got {} instead.".
                      format(functionString, test, actual))
            elif actual == expected:
                print("√ {} == {}".format(functionString, expected))
            else:
                print("X {} != {}. Got {} instead.".
                      format(functionString, expected, actual))

        return f

    return decorate
