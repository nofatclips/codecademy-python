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
be done in advance: handling exceptions.
