---
layout: default
nav_exclude: true
---

# What do you need to learn in order to find a job?
{: .no_toc }

The answer to this question depends a lot on what you already know, and what kind of programming-related job you're hoping to find. Here is some guidance on how to think about this question for your own situation.

* 
{:toc}

---

[Back to Finding Employment as a (New) Programmer](../../finding_employment/)

[Previous: How long will it take to find a job?](../how_long/)

[Next: blah]

---

## What everyone needs to learn

There are just a few things everyone needs to learn, regardless of what kind of job you are looking for:

### Fundamentals of Programming

- Fundamentals of programming
  - This includes everything in the first half of the book - variables, lists, dictionaries, loops, functions, classes, working with files, handling errors, and testing your code.
- Programming tools and workflows.
  - Version Control
    - Almost all meaningful professional projects use some form of version control today, and those that don't really should. Version control allows you to mark working states of your project, so you can always go back to a version that worked. Along with testing, this leaves you free to refactor existing code and develop new features without worrying that you'll break your existing code.
    - Most organizations are using Git for version control. If you want to learn more about this, work through Appendix D in the book; it's a brief overview that will get you started using version control in your projects today.
  - Editors and IDEs
    - It doesn't matter too much which editor or IDE you use on your own, but it does matter that you start to learn your editor well. You should be comfortable moving around your code files and project directly efficiently, and you should be able to refactor your code efficiently.
    - Some organizations require everyone to use the same editor, while others let each developer use whatever they're most comfortable with. If you're required to use an editor or IDE that you're unfamiliar with, a decent familiarity with any other editor will help you pick up the new one quickly, because you already know what kind of functionality to look for in the new editor.
  - Debugging
    - First of all, you should be able to describe the way you think about debugging. There are a number of techniques for debugging, but there's also a mindset that everyone needs to develop when debugging. What questions do you ask yourself when you start debugging? What do you do if your first efforts don't work?
    - Have some specific approaches to debugging. This can start out as print debugging. As you work with more complex codebases, however, you'll want to learn about using Python's built-in debugging tools, and your editor or IDE's debugging features. Some frameworks also have their own debugging toosls, such as the `django-debug-toolbar` package.
- How to work with others
  - When someone hires you, they're expecting you to work with others on a team to build a product or service. You will be expected to work professionally with others, to communicate clearly. This includes documenting your own work, coming to agreements. It also includes sharing and accepting critical feedback in a respectful way. Hopefully you already have these habits, but if you don't it's good to think about these things and start practicing them before you start applying.

[top](#top)

## What everyone can benefit from learning

- Intermediate programming concepts
  - You can go a long way with just the basics. But there are a number of intermediate programming concepts that will help you write more efficient code, and make it easier to approach a wider variety of problems. These skills and concepts will also help you make better sense of existing codebases. Here are a few examples:
    - Generators
      - When you define a list, the computer uses enough memory to store the entire list. This can be a problem with large collections of data. A generator represents a large collection, but it takes up little memory and returns the values you need when you ask it to.
    - Asynchronous Code, Multithreaded Code, and Parallel Processing
      - Synchronous code runs in sequence; each operation must be completed before the next operation begins. Asynchronous code allows some operations to start before the previous operation has completed. For example, instead of making 10 API calls in sequence, these 10 calls can all happen at once.
    - Recursion
      - A recursive function calls itself. Recursion isn't needed all that often, but when it is it's a really important concept to be aware of. It can be a little difficult to get conceptually at first, but with a good explanation and examples it can be understood.
    - Regular Expressions
      - Regular expressions have a reputation for being difficult, but the concept is not difficult to understand. A regular expression is a pattern; we use regular expressions to find examples of a pattern. For example there are regular expressions that will find any telephone number in a body of text, or any email address. You don't need to write your own regular expressions; many times you look up a well-tested expression and use it in your code.

[top](#top)

## Field-specific requirements

There are some kinds of jobs where you can start to apply as soon as you have a solid grasp of some basic programming skills and concepts. There are some fields, however, where you'll need some more specific knowledge to get an entry-level job.

- Web Development
  - As a web developer, you'll be expected to have some familiarity with how a modern web application runs. You'll be expected to know what a server is, and how a server responds to requests from a browser. You'll be expected to know the overall structure of an HTML document. You should know something about the HTTP request-response cycle. You should know something about the DNS system; how does a request for my_site.com get from a browser to your server, and back to the browser? You should know what JavaScript is, and why it's still so important for web applications. You should know what a database is, and have some idea how they work. Gaining familiarity with SQL would be really beneficial as well. You should have some understanding of at least one way that code can be pushed from your computer to a server, so users will see the pages and data that you want them to.
- Data Science
  If you're interested in data science, you should know how to use at least one visualization library well, and be able to learn other libraries efficiently. You should have a reasonable understanding of statistics. People with a deeper understanding of math will be able to analyze larger and more complex datasets, and do so efficiently.
  - Familiarity with Jupyter notebooks will be really helpful as well. Notebooks allow you to write text cells and code cells. So rather than just having comments in a .py file, you can write descriptive, explanatory text in between your code blocks. Jupyter notebooks are used extensively in many data science workflows.

[top](#top)

