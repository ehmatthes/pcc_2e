---
layout: default
title: What's new?
nav_order: 20
has_children: false
---

# What's new in the second edition?

Python is a mature language, but like any programming language it continues to evolve. The second edition includes some new features that have been added since the first edition came out, and uses the latest versions of third-party libraries in the projects section.

## Overall changes

Here is a summary of the changes that have been made to the book overall:

- The second edition was written using Python 3.7; the first edition was written using Python 3.5.
- Python 2 support has been dropped, as Python 2 is nearing end-of-life.
- The book uses f-strings instead of concatenation, which makes much of the syntax throughout the book simpler and less verbose.
- Many Python packages have become easier to install, so setup and installation instructions are easier.

## Specific changes

- **Chapter 1**
  - The instructions for installing Python have been simplified for users of all major operating systems.
- **Chapter 2**
  - Includes a more accurate description of how variables are implemented in Python. (Variables are described as *labels* for values, instead of *boxes* that hold values.) This leads to a better conceptual understanding of how variables behave in Python.
  - Introduces f-strings, a simpler way to use variable values in strings.
  - Introduces the use of underscores to represent large numbers. For example, writing 1_000_000 is now the same thing as writing 1000000, but is much easier to read.
  - Multiple assignment of variables is introduced here, instead of in a project.
  - Introduces a clear convention for representing constant values.
- **Chapter 6**
  - Introduces the `get()` method for retrieving values from a dictionary, which can return a default value if a key does not exist.
- **Alien Invasion (Chapters 12-14)**
  - Pygame can now be installed in one line on all systems.
  - The Alien Invasion game is now entirely class-based. The game itself is a class, rather than a series of functions. This greatly simplifies the overall structure of the game, and should make it easier for readers to further customize the game and make their own games after completing this project.
  - Readers are given the option of running the game in fullscreen mode, or in a windowed mode.
- **Data Visualization**
  - **Chapter 15**
    - The installation instructions for Matplotlib are simpler for all operating systems.
    - The visualizations featuring Matplotlib use the `subplots()` function, which will be easier to build upon as you learn to create more complex visualizations.
    - The Rolling Dice project in Chapter 15 now uses [Plotly](https://plot.ly/python/), a well-maintained visualization library that features a clean syntax and fully customizable output. The first edition used Pygal.
  - **Chapter 16**
    - The weather project is based on data from NOAA, which should be more stable over the next few years than the site used in the first edition.
    - The mapping project focuses on global earthquake activity. You'll end up with a visualization showing Earth's tectonic plate boundaries through a focus on the locations of all earthquakes over a given time period. This project will help you learn to plot any location-based data set, rather than just country-specific data.
  - **Chapter 17**
    - The visualization of Python-related activity on GitHub now uses Plotly instead of Pygal.
- **Learning Log (Web Applications, Chapters 18-20)**
  - The Learning Log project is built using the latest version of Django, and styled using the latest version of Bootstrap.
  - The process of deploying the project to Heroku has been simplified, and uses environment variables as well as modifications to *settings.py*. This approach is more consistent with how professional programmers deploy modern Django projects.
  - The project will be updated with each new version of Django that is released. Each time the book goes through a new print run, the Learning Log project will be updated to use the latest Django release available at the time of printing.
- **Appendices**
  - **Appendix A** has been fully updated to recommend current best practices in installing Python, which are simpler than they've been in the past.
  - **Appendix B** includes detailed instructions for setting up Sublime Text, and brief descriptions of most of the major text editors and IDEs in current use.
  - **Appendix C** directs readers to newer more popular online resources for getting help.
  - **Appendix D** continues to offer a mini crash course on using Git for version control.
- **Index**
  - The index has been thoroughly updated to allow you to use *Python Crash Course* as a reference for all of your future Python projects.























