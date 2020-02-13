---
layout: default
nav_exclude: true
---

# Building a portfolio
{: .no_toc }

When you're applyihng for your first programming job, employers want to know that you can use code to solve real-world problems. Most won't be satisfied that you've simply learned the syntax of a language. One of the clearest ways to demonstrate that you've moved beyond learning syntax is to build a portfolio that shows your skills, knowledge, and experience. Even if an employer doesn't look at your portfolio, you will have benefited from the process of putting it together.

* 
{:toc}

---

[Back to Finding Employment as a (New) Programmer](../../finding_employment/)

[Previous: How much do you need to know in order to find a job?](../what_learn/)

[Next: blah]

---

## What is a portfolio?

A portfolio is a body of work that demonstrates your skills and knowledge. A portfolio can be a single project, or it can be a collection of projects. It's much more important to have high quality work in your portfolio thatn to have a large number of projects.

[top](#top)

## Why is building a portfolio important?

A portfolio demonstrates not just the ability to write code; it also demonstrates that you understand how code fits into a larger project. Many portfolios are stored on GitHub, but you can use any online code repository such as Gitlab or Bitbucket. If you have a well developed project on GitHub, employers will see a number of things about you:

- You know how to use a version control system, such as Git.
- You know how to manage a remote repository, not just a repository on your local system.
- You know how issue trackers work, and you have a clear system for tracking issues over the course of a larger project.
- You know how to submit, review, and accept pull requests.

[top](#top)

## How should you build a portfolio?

A portfolio should not be a collection of homework problems from a class, or solutions to exercises from a book. All that really shows is that you've learned the syntax and basic concepts of a language. It's also really hard to tell whether someone wrote their own solutions to a common set of exercises, or looked them up online.

Instead, you should build a meaningful project. Ideally this is an original project, that uses what you've learned from other sources. It can, and probably will, be modeled after a project you learned from a book or tutorial. But your project should go beyond what you were directed to do in the tutorial in a significant way.

There are ways to make your projects interesting. If you're interested in web development, for example, you might build an interactive site for your portfolio. If you don't have users, you can write code that generates hundreds or thousands of fake users, and even fake interactions between users. This shows what your project might look like when it's being used by actual people.

Your portfolio project should demonstrate familiarity with as many aspects of a professional workflow as you can, without spreading yourself too thin. Here are a few things to consider:

### Use GitHub (or any online repository) as if you were part of a team

  Build a small piece of your project on your local system, and then set up a GitHub repository for the project. Push this first piece of your project, and from then on use GitHub to manage your project.

### Keep track of your project using GitHub's issue tracker

  You may want to keep some working notes offline. But each time you start working on a new feature, open an issue describing the new feature, and keep track of your progress on that feature in that issue thread. As you complete new features, you will start to have a set of closed issues that represent your progress on the project.

### Submit pull requests to yourself

  Since you're the maintainer of this project, you could just commit and push your code every time you make progress. But you won't often be able to do that on a team. Instead, submit a pull request to your own project. Then use GitHub's online tools to review the PR, and merge it into the project. You can write a brief comment about this overall phase of the project.

### Use feature branches

  Branching is a powerful tool for feature development and deployment workflows. When you start working on a new feature, make a new branch and then merge that branch when you're finished implementing the new feature. This allows you to make incremental commits as you're working on the feature, and then merge the entire set of commits into the main branch once the feature is complete. If you decide to abandon this particular feature, your main branch won't be polluted with the incremental commits you made while starting to build out this feature.

  Feature branches also work well with the process of submitting pull requests to your own project.

### Write an informative readme

  Your readme file is an overview of your project. It should tell peoplpe what the project does, and how to run your project locally. Writing a good readme shows potential employers how well you can document your own development work, and how you might communicate with co-workers, customers, and the general public.

  If your project is deployed somewhere, make sure you provide a link to the deployed version of your projects.

### Include meaningful tests

  You don't have to have full test coverage, but you should have some tests. Pick one core aspect of your project's functionality, and make sure that functionality is well-tested. Run your tests every time you make a pull request, or merge a feature branch.

[top](#top)

## What's better, depth or breadth?

A single project that shows depth of understanding, and an awareness of the complete lifecycle of a real-world project, is better than a bunch of smaller projects or exercises. It's perfectly reasonable to have several smaller projects that show specific skills in your portfolio. For example if you have a fully functioning web app, but you also want to demonstrate an understanding of web scraping, you might have a repository containing a small project that scrapes local marketplace listings.

[top](#top)