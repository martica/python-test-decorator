import sys
import traceback
from inspect import isclass

def test(inputs, expected):
    def decorate(f):
        if __name__ != "__main__": # If we are running as an import, don't run the tests
            return f

        input_string = ', '.join([repr(x) for x in inputs])
        functionString = "{}({})".format(f.__name__, input_string)
        try:
            test = expected.__name__
        except:
            test = str(expected)

        try:
            actual = f(*inputs)
        except Exception as actual:
            exceptionType, exceptionValue, exceptionTraceback = sys.exc_info()
            exceptionString = ''.join( traceback.format_exception_only( exceptionType, exceptionValue ) ).rstrip("\n")
            if expected == exceptionType:
                print( "√ Called {}, Caught expected exception. {}".format( functionString,  exceptionString ) )
            else:
                print( "X Called {}, expected {}, Caught unexpected exception. {}".format( functionString,  test, exceptionString ) )
        else:
            if isclass(expected) and issubclass( expected, Exception ):
                print( "X Called {}, expected {}, Got {} instead.". format( functionString, test, actual ) )
            elif actual == expected:
                print( "√ {} == {}".format( functionString, expected ) )
            else:
                print( "X {} != {}. Got {} instead.".format( functionString, expected, actual ) )

        return f

    return decorate
