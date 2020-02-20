---
layout: default
nav_exclude: true
---
      
# Building a portfolio
{: .no_toc }

When you're applying for your first programming job, employers want to know that you can use code to solve real-world problems. Most won't be satisfied that you've simply learned the syntax of a language. One of the clearest ways to show that you've moved beyond learning syntax is to build a portfolio that demonstrates your skills, knowledge, and experience. Even if an employer doesn't look at your portfolio, you will have benefited from the process of putting it together.

* 
{:toc}

| [<< How much do you need to know?](../what_learn/) | [Finding Employment](../../finding_employment/) | [Applying for jobs >>](../../finding_employment/applying_jobs/) |

---

## What is a portfolio?

A portfolio is a body of work that demonstrates your skills and knowledge. A portfolio can be a single project, or it can be a collection of projects. It's much more important to have high quality work in your portfolio than to have a large number of projects.

[top](#top)

## Why is building a portfolio important?

A portfolio demonstrates not just the ability to write code; it also demonstrates that you understand how code fits into a larger project. Many portfolios are stored on [GitHub](https://github.com), but you can use any online code repository such as [GitLab](https://about.gitlab.com) or [Bitbucket](https://bitbucket.org). If you have a well developed project on one of these sites, employers will see clear evidence of a number of important things:

- You know how to use a version control system, such as Git.
- You know how to manage a remote repository, not just a repository on your local system.
- You know how issue trackers work, and you have a clear system for tracking issues over the course of a larger project.
- You know how to submit, review, and accept pull requests.
- You know how to manage a project environment, and make it easy for others to replicate your work.

[top](#top)

## How should you build a portfolio?

A portfolio shouldn't be a collection of homework problems from a class, or solutions to exercises from a book. All that really shows is that you've learned the syntax and basic concepts of a language. It's also really hard to tell whether someone wrote their own solutions to a common set of exercises, or looked them up online.

Instead, you should build a meaningful project. Ideally this is an original project, that uses what you've learned from other sources. It can, and probably will, be modeled after a project you learned from a book or tutorial. But your project should go beyond what you were directed to do in the tutorial in a significant way.

There are ways to make your projects interesting. If you're interested in web development, for example, you might build an interactive site for your portfolio. If you don't have users, you can write code that generates hundreds or thousands of fake users, and even fake interactions between users. This shows what your project might look like when it's actually being used.

Your portfolio project should demonstrate familiarity with as many aspects of a professional workflow as possible, without spreading yourself too thin. Here are a few things to consider when building your portfolio.

### Use GitHub (or any online repository) as if you were part of a team

  Build a small piece of your project on your local system, and then set up a GitHub repository for the project. Push this first piece of your project, and from then on use GitHub to manage your project.

### Keep track of your project using GitHub's issue tracker

  You may want to keep some working notes offline. But each time you start working on a new feature, open an issue describing the new feature and keep track of your progress on that feature in that issue thread. As you complete new features, you'll start to have a set of closed issues that represent your progress on the project.

### Submit pull requests to yourself

  Since you're the maintainer of this project, you could just commit and push your code every time you make progress. But you won't often be able to do that on a team. Instead, submit a pull request to your own project. Then use GitHub's online tools to review the PR, and merge it into the project. You can write a brief comment about this overall phase of the project when you merge the PR.

### Use feature branches

  *Branching* is a powerful tool for feature development and deployment workflows. When you start working on a new feature, make a new branch and then merge that branch when you're finished implementing the new feature. This allows you to make incremental commits as you're working on the feature, and then merge the entire set of commits into the main branch once the feature is complete. If you decide to abandon this particular feature, your main branch won't be polluted with the incremental commits you made while starting to build out this feature.

  Feature branches also work well with the process of submitting pull requests to your own project.

### Write an informative readme

  The *readme file* is an overview of your project. It should tell people what the project does, and how to run your project locally. It should include a description of how to install the required libraries in an isolated environment on a developer's local system. If your project is deployed somewhere, make sure you provide a link to the deployed version of the project.

  Writing a good readme shows potential employers how well you can document your own development work, and how you might communicate with co-workers, customers, and the general public.

### Include meaningful tests

  You don't have to have full test coverage, but you should have some tests. Pick one core aspect of your project's functionality, and make sure that functionality is well-tested. Run your tests every time you review a pull request, or merge a feature branch.

[top](#top)

## What's better, depth or breadth?

A single project that shows depth of understanding, and an awareness of the complete lifecycle of a real-world project, is better than a bunch of smaller projects or exercises. That said, it's perfectly reasonable to have several smaller projects that show specific skills in your portfolio. For example if you have a fully functioning web app, but you also want to demonstrate an understanding of web scraping, you might have a repository containing a small project that scrapes local marketplace listings.

[top](#top)