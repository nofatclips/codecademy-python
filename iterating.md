Week 29 Review: Iterating in Python
===================================

This week I'll cover some of the built-in functions that make writing loops in Python as easy as 3.14

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

See what I did there? By specifying the named parameter `reverse` you can also get reverse order.
But what if my list (let's get back to lists) is already ordered. It would be a waste to call `sorted` just to reverse it, right?
Enter, `reversed`:

    a_to_z = ["a", "to", "z"]
    for s in reversed(a_to_z):
        print s

Once again, after I printed the list in reversed order, the list is gone.
