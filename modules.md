Week 25 Review: Importing Modules
============

Hi!
Today we're going to talk about modules. A [module](http://docs.python.org/2/tutorial/modules.html), in its essence, is no more than a script, a file containing Python code. When you're working on a big project, you might want to split your code in smaller modules to keep it manageable; additionally, using modules makes possible to reuse the same code in several projects.

The most prominent case of reuse is obviously the [Python Standard Library](http://docs.python.org/2/library/). Python comes with a set of standard modules that add a lot of useful features to those built into the language. You only need to import them into your own program and use them. How?

Importing and Using a Module
------------------

In Python, you do that with the `import` keyword, followed by the name of the module:

    import someLibrary
    
From now on, `someLibrary` works as a namespace to access the functions offered the the module. That is: in order to call some function defined in `someLibrary`, you're going to use:
    
    someLibrary.someFunction()
    


References and Additional Links
----------------

[Python Koans](https://github.com/gregmalcolm/python_koans)
