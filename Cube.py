import TestDecorator

@test(inputs=(2,), expected=0.125)             # Failure: get wrong value
@test(inputs=("a",), expected=1000)            # Failure: expect value, get exception
@test(inputs=([],), expected=ZeroDivisionError) # Failure: expect different exception
@test(inputs=(10,), expected=TypeError)        # Failure: expect exception get value
@test(inputs=(2,3), expected=TypeError)        # Pass: expect exception
@test(inputs=(3,), expected=27)                # Pass: get expected value
def cube( n ):
    return n*n*n
