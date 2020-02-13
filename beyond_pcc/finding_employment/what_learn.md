---
layout: default
nav_exclude: true
---

# What do you need to learn in order to find a job?
{: .no_toc }

How much you need to learn to land your first programming job depends a lot on what you already know, and what kind of job you're hoping to find. Here's some perspective on how to think about this question for your own situation.

* 
{:toc}

---

[Back to Finding Employment as a (New) Programmer](../../finding_employment/)

[Previous: How long will it take to find a job?](../how_long/)

[Next: blah]

---

## What everyone should know

There are a few things everyone needs to know, regardless of what kind of job you're looking for:

### Fundamentals of programming

This includes everything in the first half of the book - variables, lists, dictionaries, conditional statements, loops, functions, classes, working with files, handling errors, and testing your code. These are the fundamentals you'll use all your life as a programmer, in any language you choose to work with.

### Programming tools and workflows

- Version Control
    
    Almost all professional projects use some form of version control today, and those that don't really should. Version control allows you to identify working states of your project, so you can always go back to a version that worked. Along with testing, this leaves you free to refactor existing code and develop new features without worrying that you'll break your existing code. If you do break your code, you roll back to the last working version and pick up from there. Distributed version control systems allow teams of just about any size to work collaboratively, in real time, on a single codebase.
    
    Most organizations use Git for version control. If you want to learn more about Git and version control, work through Appendix D in the book. It's a brief overview that will get you started using version control in your projects today.

- Editors and IDEs
    
    It doesn't matter which editor or IDE you use on your own, but it is important that you start to learn your editor well. You should be able to efficiently move around your code files and project directly, and you should be able to refactor your code efficiently as well.
    
    Some organizations require everyone to use the same editor, while others let each developer use whatever they're most comfortable with. If you're required to use an editor or IDE that you're unfamiliar with, a decent familiarity with any other editor will help you pick up the required one quickly, because you'll already know what kind of functionality to look for in the new editor.

- Debugging
    
    First of all, you should be able to describe the way you think about debugging. There are a number of techniques for debugging, but there's also a mindset that everyone needs to develop when debugging. What questions do you ask yourself when you start debugging? What do you do if your first efforts don't work?
    
    Make sure you are starting to develop a specific approach to debugging. This can start out as print debugging, where you insert print statements in your code to check if your variables represent the values you think they do at certain points in your program's execution. As you work with more complex codebases, however, you'll want to learn about using Python's built-in debugging tools, and your editor or IDE's more advanced debugging features. Some frameworks also have their own debugging toosls, such as the `django-debug-toolbar` package.

### How to work well with others

When an individual or organization hires you, they're expecting you to work with others on a team to build a product or service. You'll be expected to work professionally with others, and to communicate clearly and respectfully. This includes sharing and accepting critical feedback in a respectful way. Hopefully you already have these kinds of communication habits, but if you don't it's good to think about these things and start practicing them before you start applying.

[top](#top)

## What everyone can benefit from knowing

You can go a long way with just the basics. But there are a number of intermediate programming concepts that will help you write more efficient code, and make it easier to address a wider variety of real world problems through code. These skills and concepts will also help you make better sense of existing codebases that you might have to work with. Here are a few examples:

- Generators

  When you define a list, the computer grabs enough memory to store the entire list, and keeps using that memory as long as the program might need that data. This can be a problem with large collections of data. A generator represents a large collection, but it takes up as little memory as possible, while still being able to generate the values you need, when you need them.

- Asynchronous Code, Multithreaded Code, and Parallel Processing

  Synchronous code runs in sequence; each operation in a program must be completed before the next operation begins. Asynchronous code allows some operations to start before the previous operation has completed. For example, instead of making 10 API calls in sequence, these 10 calls can all happen at once. Asynchronous code can be much faster than synchronous code, but it's also more complex and more difficult to reason about correctly.

- Recursion

  A recursive function calls itself. Recursion isn't needed all that often, but when it is it's a really important concept to be aware of. Recursion is a shortcut for repeatedly calling the same function from inside a loop.

- Regular Expressions

  Regular expressions have a reputation for being difficult, but you shouldn't be intimidated by them. A regular expression defines a pattern; we use regular expressions to find examples of a pattern. For example there are regular expressions that will find any telephone number in a body of text, or any email address. You don't need to write your own regular expressions; many times you look up a well-tested expression and use it in your code.

[top](#top)

## Requirements for specific jobs

For some kinds of jobs, you can start to apply as soon as you have a solid grasp of basic programming skills and concepts. There are some fields, however, where you'll need more specific knowledge to get an entry-level job.

- Web Development

  As a web developer, you'll be expected to have some familiarity with how a modern web application runs. You should know what a server is, and how a server responds to requests from a browser. You should have some understanding of at least one way that code can be pushed from your computer to a server. You'll be expected to know the overall structure of an HTML document. You should know something about the DNS system; how does a request for my_site.com get from a browser to your server, and back to the browser? You should know what JavaScript is, and why it's still so important for web applications. You should know what databases are, and have some idea how they work. Gaining familiarity with SQL would be really beneficial as well.

- Data Science

  If you're interested in data science, you should know how to use at least one visualization library well, and be able to learn other libraries efficiently. You should have a reasonable understanding of statistics. People with a deeper understanding of math will be able to analyze larger and more complex datasets, and find ways to do so efficiently.

  Having some familiarity with Jupyter notebooks will be really helpful as well. Notebooks are made up of cells; each cell can be a text cell or a code cell. Text cells can include formatting and images as well. Rather than just having comments in a .py file, you can write descriptive, explanatory text in between your code blocks. Jupyter notebooks are used extensively in many data science workflows.

[top](#top)

