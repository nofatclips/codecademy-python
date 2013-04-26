Week 21 Review: Exceptions
============

Errors happen all the time in writing software. Even when we are sure that our code is bug free, problems may occur
due to user misbehavior, OS/Hardware failure or other unpredictable circumstances.

Consider the simple example of a division program:

http://pythonfiddle.com/python-week-review-exceptions/

While the logic seems flawless, there are many things that can go wrong: the user may insert non numeric values,
or try to divide a number by zero. This is the kind of error than can and should be anticipated and therefore avoided
using `if`s and library functions:

http://pythonfiddle.com/python-week-review-exceptions-avoidance

But let's see a different way to deal with exceptional circumstances, a way that will be useful when detection can't
be done in advance: handling exceptions. Which begs the question: what is an exception?

You're used to your function `return`ing a value when everything ends well, right? Well, when things goes awry,
functions stop executing and throw `Exception`s at you. When not handled, `Exception`s will make your program crash and
exit with an error message: just try dividing by zero in the first program.

In order to handle exceptions, first we wrap the part of our code that can raise problems in a `try` block:

http://pythonfiddle.com/python-week-review-exceptions-passing

The `try` block is followed by an `except` block (in fact one or more `except` block. More about this later)
which is where we handle the errors. In our example, I just did
nothing and `pass`ed: errors are muted. Notice that now, trying to divide by zero doesn't crash the program.
This is not good as it seems: we're sweeping the problems under the rug. We don't even know if something went bad!

Let's print a friendly error message like we did in the Error Avoidance version. Problem: how do we tell between
"user entered a string" and "divide by zero" errors? That's simple: `except` accept the error type as a parameter.
We can have as many `except` block as type of errors we want to handle.

But first, we need to know what these error types are. Let's run the original program and enter a string. We get:

    ValueError: invalid literal for int() with base 10: 'YOLO!'
    
while if we try to divide by zero, we get:

    ZeroDivisionError: integer division or modulo by zero
    
and now we know we need to handle `ValueError` and `ZeroDivisionError`. The rest is straightforward:

http://pythonfiddle.com/python-week-review-exceptions-handling/
