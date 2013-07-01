Week 29 Review: Iterating in Python
===================================

This week I'll cover some of the built-in functions that make writing loops in Python as easy as 3.14

Sorting
-------

Let's start with a simple one: what if my list is not sorted but I want to print it alphabetical order?
I could certainly call the `.sort()` method on my list and then print it, but that method works in place.
This means that my list will actually get sorted, and perhaps I don't want  it. In fact, perhaps I don't even want to store a new list which I'm not going to need anymore as soon as I `print`ed it.
Also: what if I don't have a list at all? What if I have a set?
The Python way is to use [`sorted()`](http://docs.python.org/2/library/functions.html#sorted). It works with any iterable object, not just lists.

    a = {"a", "b", 1} # A set, not a list!
    print a
    try:
        a.sort()
    except:
        # Sets don't have a sort method!!!
        print sorted(a)
    for stuff in sorted(a, reverse=True):
    print stuff

Reversing
---------

See what I did there? By specifying the named parameter `reverse` you can also get reverse order.
But what if my list (let's get back to lists) is already ordered. It would be a waste to call `sorted` just to reverse it, right?
Enter, [`reversed`](http://docs.python.org/2/library/functions.html#reversed):

    a_to_z = ["a", "to", "z"]
    for s in reversed(a_to_z):
        print s

Once again, after I printed the list in reversed order, the new reversed list is gone, unless I store it in a variable.

Zipping
-------

Now, let's say that I have two lists of strings, names and verbs, and I want to print them in random couples just for fun.
Since the for loop only allows me to iterate over one iterable object, I would write something like:

    from random import shuffle
    
    verbs = ["kill", "kiss", "marry"]
    nouns = ["Joe", "Jane", "Guido"]
    shuffle(nouns)
    
    for index in range(len(verbs)): # <- not zen!
        print str(num+1)+".", verbs[index], nouns[index]
        
I would be wrong: always bet on Python when you need to write better and/or less code!
It's indeed true that I can't loop over two or more iterables at the same time. But I can loop over a list of tuples.
All I need is a way to build a list of tuples like:

    # Your list will be different because of shuffle
    [("kill", "Joe"), ("kiss", "Jane"), ("marry", "Guido")]
    
which is exactly what the [`zip()`](http://docs.python.org/2/library/functions.html#zip) function does!

    from random import shuffle
    
    verbs = ["kill", "kiss", "marry"]
    nouns = ["Joe", "Jane", "Guido"]
    shuffle(nouns)
    
    for verb, noun in zip(verbs, nouns):
        print verb, noun

Enumerating
-----------

Yes but... My "non zen" code printed a nice ordered list. How do I get that with zip? Well, you don't.
But that doesn't mean that you're back at iterating with `range`! What you need is [`enumerate`](http://docs.python.org/2/library/functions.html#enumerate):

    # Let's start with verbs only
    verbs = ["kill", "kiss", "marry"]
    
    for index, verb in enumerate(verbs, start=1):
        print str(index)+".", verb
        
As you can see, enumerate return a tuple like zip, but the first value is the index of the current element, or better: a counter. As you can see, with the named parameter `start` we were able to start counting at `1` even though all elements in list have been printed. (That is, enumerate didn't start at index 1: it just started counting at 1.)
