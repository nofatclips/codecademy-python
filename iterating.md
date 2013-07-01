Week 29 Review: Iterating in Python
===================================

This week I'll cover some of the built-in functions that make writing loops in Python as easy as 3.14

Let's start with a simple one: what if my list is not sorted but I want to print it alphabetical order?
I could certainly call the `.sort()` method on my list and then print it, but I would have to store a new list which I won't need anymore as soon as I `print`ed it. That's a waste. Also: what if I don't have a list?
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
But what if my 
