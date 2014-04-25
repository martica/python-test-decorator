Mockup of an example from a tweet. https://twitter.com/raymondh/statuses/459495133075877888

Using python decorators to define tests for a function.

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

Output:

    > python3 main.py
    √ cube(3) == 27
    √ Called cube(2, 3), Caught expected exception. TypeError: cube() takes 1 positional argument but 2 were given
    X Called cube(10), expected TypeError, Got 1000 instead.
    X Called cube([]), expected ZeroDivisionError, Caught unexpected exception. TypeError: can't multiply sequence by non-int of type 'list'
    X Called cube('a'), expected 1000, Caught unexpected exception. TypeError: can't multiply sequence by non-int of type 'str'
    X cube(2) != 0.125. Got 8 instead.
    1000
    

