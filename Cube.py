from testdecorator import test


# Failure: get wrong value
@test(inputs=(2,), expected=0.125)
# Failure: expect value, get exception
@test(inputs=("a",), expected=1000)
# Failure: expect different exception
@test(inputs=([],), expected=ZeroDivisionError)
# Failure: expect exception get value
@test(inputs=(10,), expected=TypeError)
# Pass: expect exception
@test(inputs=(2, 3), expected=TypeError)
# Pass: get expected value
@test(inputs=(3,), expected=27)
def cube(n):
    return n * n * n
