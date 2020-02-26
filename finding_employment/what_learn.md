---
layout: default
title: How much do you need to know?
parent: Finding Employment
nav_order: 40
---

# How much do you need to know in order to find a job?
{: .no_toc }

How much you need to learn to land your first programming job depends on what you already know, and what kind of job you're hoping to find. Here's some perspective on how to think about this question for your own situation.

* 
{:toc}

| [<< How long will it take?](../how_long/) | [Finding Employment](../../finding_employment/) | [Building a portfolio >>](../../finding_employment/building_portfolio/) |

---

## What everyone should know

There are a few things everyone needs to know, regardless of what kind of job you're looking for:

### Fundamentals of programming

This includes everything in the first half of the book - variables, lists, dictionaries, conditional statements, loops, functions, classes, working with files, handling errors, and testing your code. These are the fundamentals you'll use all your life as a programmer, in any language you choose to work with.

### Programming tools and workflows

- Version Control
    
    Almost all professional projects use some form of version control, and those that don't really should. Version control allows you to identify working states of your project, so you can always go back to a version that worked. Along with testing, this leaves you free to refactor existing code and develop new features without worrying that you'll break your existing code. If you do break your code, you can roll back to the last working version and pick up from there. Distributed version control systems allow teams of just about any size to work collaboratively, in real time, on a single codebase.
    
    Most organizations use Git for version control. If you want to learn more about Git and version control, work through Appendix D in the book. It's a brief overview that will get you started using version control in your projects today.

- Editors and IDEs
    
    It doesn't matter which editor or IDE you use on your own, but it's important that you start to learn your editor well. You should be able to efficiently move around your code files and project directory, and you should be able to refactor your code efficiently as well.
    
    Some organizations require everyone to use the same editor, while others let each developer use whatever they're most comfortable with. If you're required to use an editor or IDE that you're unfamiliar with, a decent familiarity with any other editor will help you pick up the required one quickly, because you'll already know what kind of functionality to look for in the new editor.

- Debugging
    
    First of all, you should be able to describe the way you think about debugging. There are a number of techniques for debugging, but there's also a mindset that everyone needs to develop when debugging. What questions do you ask yourself when you start debugging? What do you do if your initial debugging efforts don't work?
    
    Make sure you're starting to develop a specific approach to debugging. This can start out as print debugging, where you insert print statements in your code to check if your variables represent the values you think they do at certain points in your program's execution. As you work with more complex codebases, however, you'll want to learn about using Python's built-in debugging tools, and your editor or IDE's more advanced debugging features. Some frameworks also have their own debugging tools, such as the `django-debug-toolbar` [package](https://github.com/jazzband/django-debug-toolbar) for Django projects.

### How to work well with others

When an individual or organization hires you, they're expecting you to work with others on a team to build a product or service. You'll be expected to work professionally with others, and to communicate clearly and respectfully. This includes sharing and accepting critical feedback in a respectful way. Hopefully you already have these kinds of communication habits, but if you don't it's good to think about these things and start practicing them before you start applying for jobs.

[top](#top)

## What everyone can benefit from knowing

You can go a long way with just the basics. But there are a number of intermediate programming concepts that will help you write more efficient code, and make it easier to address a wider variety of real-world problems through code. These skills and concepts will also help you make better sense of existing codebases that you might have to work with. Here are a few examples:

- Generators

  When you define a list, the computer grabs enough memory to store the entire list, and keeps using that memory as long as the program might need that data. This can be a problem with large collections of data. A *generator* represents a large sequence, but it takes up as little memory as possible. Instead of storing all the items in the sequence, it just contains rules for how to generate or retrieve the values you'll need, when you need them.

- Asynchronous Code, Multithreaded Code, and Parallel Processing

  *Synchronous* code runs in sequence; each operation in a program must be completed before the next operation begins. *Asynchronous* code allows some operations to start before the previous operations have completed. For example, instead of making 10 API calls in sequence, these 10 calls can all happen at once. Asynchronous code can be much faster than synchronous code, but it's also more complex and more difficult to reason about correctly.

- Recursion

  A *recursive* function calls itself. Recursion isn't needed all that often, but when it is it's a really important concept to be aware of. Recursion is a shortcut for repeatedly calling the same function from inside a loop.

- Regular Expressions

  Regular expressions have a reputation for being difficult, but you shouldn't be intimidated by them. A *regular expression* defines a pattern; we use regular expressions to find examples of a pattern. For example there are regular expressions that will find any telephone number in a body of text, or any email address. You don't always need to write your own regular expressions; many times you'll look up a well-tested expression and use it in your code.

- Packaging and managing environments

  As you transition into professional programming work, you'll find yourself working on more than one project at a time, or multiple versions of the same project. For example you'll need to fix bugs in the latest version of a project, but also in older but still maintained versions of a project. These projects can require different libraries, different versions of the same library, and different versions of Python itself. At some point you'll need to learn how to isolate projects on your system, so the libraries you install for one project won't affect the libraries you're using for another project. The Learning Log project uses the `venv` module to do this.

- Type systems

  Python is a dynamically-typed language, which means you don't have to declare what kind of information you're going to assign to a variable ahead of time. Python looks at the values you're using, and takes care of types automatically. However, you can choose to assign types to your variables if you want. This makes for more verbose code, but it also helps prevent certain kinds of errors.

- Reading documentation

  It's really important to become familiar with the [official Python documentation](https://docs.python.org/3/), and the documentation of the libraries you use regularly. Familiarity with documentation will help you solve your own problems more efficiently, and keep you from leaning too heavily on others in your learning and in your work. You should absolutely ask questions of the people around you and in online communities, but you should also show that you've done your own research as you're asking others for help. You'll also have to write documentation for your own code, or your team's code at some point. Knowing how [good documentation is organized](https://www.divio.com/blog/documentation/) is really helpful.

  Don't worry if it takes a while to make sense of the documentation for large projects such as the overall Python language, a visualization library such as [Matplotlib](https://matplotlib.org), or a web framework like [Django](https://docs.djangoproject.com/en/3.0/). These large projects aim for thorough coverage in their documentation, so the documentation itself gets large and can take a while to understand. Instead of trying to understand the documentation of the entire Python language, just spend some time on one element such as [dictionaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries), and see [how much you can learn](https://docs.python.org/3/library/stdtypes.html#typesmapping) about that one element from studying the documentation. Also, it might be helpful to start by diving into the documentation for a smaller library that you use, such as [Requests](https://requests.readthedocs.io/en/master/). 

- Algorithms and data structures

  Algorithms and data structures are the bread and butter of a programmer's work. *Algorithms* are well-established approaches to common problems in programming, such as how to sort a collection of elements into a specific order. *Data structures* refer to the model you'll use to store data for a specific problem you're trying to solve.

  Python takes care of a lot of the basic algorithms you'll need, such as sorting a list. If you need to sort a list, you should use the built-in sorting methods. They're well tested and optimized, and you're unlikely to write better sorting code than what a large team of language developers have come up with over a period of decades. But at some point you might want to learn about the internals of these methods, and you may be asked about them in interviews. Employers won't want you to write your own sorting code. However, if you know many of the common CS algorithms they can be more confident that you'll be able to write higher-quality code that's easier to optimize over time.

  You're probably already using a number of data structures - lists, tuples, dictionaries, and classes. These can go a long way, but there are a number of others you should be aware of at some point. These include arrays, stacks, queues, linked lists, structs, graphs, trees, and a few others.

  Some interviewers use algorithms and data structures as a gatekeeping tool. Everyone who goes through a formal CS education has to learn about algorithms and data structures, and these are seen as evidence of a thorough background in CS concepts. Go ahead and learn them, because the concepts you learn will help you write better code, and understand the code you're working with better. But don't let the gatekeeper folks get you down about being self-taught, if it's clear they're more interested in showing how much they know than finding out how much you know.

[top](#top)

## Requirements for specific jobs

For some kinds of jobs, you can start to apply as soon as you have a solid grasp of basic programming skills and concepts. There are some fields, however, where you'll probably need more specific knowledge to get an entry-level job.

- Web Development

  As a web developer, you'll be expected to have some familiarity with how a modern web application runs. You should know what a server is, and how a server responds to requests from a browser. You should have some understanding of at least one way that code can be pushed from your computer to a server. You'll be expected to know the overall structure of an HTML document. You should know something about the DNS system; how does a request for my_site.com get from a browser to a server, and back to the browser? You should know what JavaScript is, and why it's still important for many web applications. You should know what databases are, and have some idea how they work. Gaining familiarity with SQL would be really beneficial as well.

- Data Science

  If you're interested in data science, you should know how to use at least one visualization library well, and be able to learn other libraries efficiently. You should have a reasonable understanding of statistics. People with a deeper understanding of math will be able to analyze larger and more complex datasets, and find ways to do so efficiently.

  Having some familiarity with [Jupyter notebooks](https://jupyter.org) will be really helpful as well. *Notebooks* are made up of cells; each cell can be a text cell or a code cell. Text cells can include formatting and images as well. Rather than just writing comments in a .py file, you can write descriptive, explanatory text in between your code blocks. Jupyter notebooks are used extensively in many data science workflows.

[top](#top)

