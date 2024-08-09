print(my_variable)

"""
We’ll quickly get a NameError. That’s a built-in error type in Python that suggests we used a name (in this case, `my_variable`) that didn’t exist. It’s great to receive that error, because once you know what it means you can easily find the source of the problem.

It would be much worse if you just got an `Error`—it may take you hours (or days) to find a simple error in a larger application.

The name of the error is very useful. But even more useful is the *stack trace*, which tells you which files the error touched. Here’s a sample stack trace from an error I saw earlier on:

Traceback (most recent call last):
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 53, in <module>
    menu()
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 10, in menu
    show_movies()
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 36, in show_movies
    show_movie_details(movie)
  File "/Users/jslvtr/Dropbox/teclado/courses/complete-python-course/section3/milestone_1/app.py", line 40, in show_movie_details
    print(f"Name: {movies['name']}")
TypeError: list indices must be integers or slices, not str

This error is a `TypeError`, which means we used the wrong type of data for our operation (in this case, we tried to access a list as if it were a dictionary).