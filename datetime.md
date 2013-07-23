The datetime Module Part 2
==========================

The datetime class
------------------

You might have noticed that the [date](http://www.codecademy.com/groups/python-fro-beginners/discussions/51dae0ab7c82ca812204d793) class doesn't have properties for hours, minutes and seconds. And the [time](http://www.codecademy.com/groups/python-fro-beginners/discussions/51e44a87631fe9442d006521) class doesn't have properties for year, month and day.

This is great: concerns are nicely separate, each class does exactly what it needs to do, I don't need to create objects that do more things than I actually need and so on. But what if I need manage a complete timestamp, years to milliseconds?

If I want to represent the exact moment of my birth, I need to store both the date and the time. Do I need to use two separate objects? If I want to know how many seconds passed from my birth up until now, do I need four objects? Do I need to write all the code to do that?

Fear not, since the [datetime module](http://docs.python.org/2/library/datetime.html) has a [datetime class](http://docs.python.org/2/library/datetime.html#datetime-objects)
