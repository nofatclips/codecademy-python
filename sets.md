Week 18 Review: The Set
====================

Today we're going to talk about `set`s, a data structure that I mistakenly covered in
[Week 14 review](http://www.codecademy.com/groups/python-fro-beginners/discussions/513db1703a03bbfc0b0006f2)
being under the impression that it was the topic of one the lessons in the Python track.
In fact it isn't, but it should since it's a nicely useful object.

A Python set is very close to the mathematical set: it can store many objects, but they must all be unique and they're
not in any particular order or sequence. So,
while you are used to store the same value multiple times in a list (es. fibonacci = [1,1,2,3,5]) this is
not possible with sets: you can only have one copy. Let's try and define a set in the Python console:

    > fibo = {1, 1, 2, 3, 5}
    > print fibo
    => set([1, 2, 3, 5])
    
The `{}` is the literal notation for sets. As you might remember from last week, it's also the notation for
dictionaries, but Python is smart enough to distinguish between the two.

We tried to store the first 5 elements in the fibonacci sequence, but we only got four: we only got one instance
of the number `1`. But let's go by the manual.

The [manual](http://docs.python.org/2/library/stdtypes.html#set) says that a **set** is an
_unordered_ _collection_ of _distinct_ _hashable_ objects. Let's break this down.

What is a collection? We already saw other examples:
the [list](http://www.codecademy.com/groups/python-fro-beginners/discussions/50bcc8cde3a02329b9000003) and
the [dictionary](http://www.codecademy.com/groups/python-fro-beginners/discussions/5159a72318e52a0dd9001a6a). What
these structures have in common is the fact that they store multiple values.

One difference between lists and dictionaries is that lists have a defined order, while dictionaries don't. As
you might have guessed, sets are also unordered


P.S. Some technicalities. What I described refers to Python 2.7.x as well as Python 3.x.x

The set was first introduced in Python 2.3 as a library (you had to `import sets`, plural, in order
to be able to use it in your programs). In Python 2.6 `sets` was replaced by `set` , a built-in type, that is
part of the Python language (while the old library has been deprecated). Only with Python 2.7 the `{}` notation
has been introduced (so, you won't be able to use it in some online IDEs that are still stuck to older versions of
Python, and you may even have to `import sets` if the version is <2.6).

For Python 3 users, same as Python 2.7 except that obviously `sets` has been removed.
