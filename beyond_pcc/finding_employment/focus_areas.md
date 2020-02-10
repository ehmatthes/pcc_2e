---
layout: default
nav_exclude: true
---

# What can you do as a professional programmer?
{: .no_toc }

One of the reasons it's hard to give a quick answer to the question, "What should I learn if I want to be a professional programmer?" is there are so many different things you can do as a programmer. If you want clear advice, you need to know the kinds of things you can do, and know what kinds of work you're most interested in.

* 
{:toc}

[Previous: Finding Employment as a (New) Programmer](../../finding_employment/)

[Next: How long will it take?](../../finding_employment/how_long/)

---

## General Programming

While there are many who might consider themselves to be generalist programmers, there aren't many jobs for generalists. People get hired for more specific roles, such as web development or data science work. So by all means continue to improve your overall programming skills and knowledge, but consider a more specific area to focus on when looking for work.

[top](#top)

## Web Development

Web developers focus on building and maintaining interactive web sites. Web sites have been interactive for a long time now, but they are constantly evolving. As a web developer you can work on simple sites that allow users to upload specific kinds of data, or you can work on projects that are basically full desktop applications delivered through a browser.

Web developemnt is often broken into front end work and backend work. Front-end developers focus ont he interface that users see in the browser. They try to make sites look appealing on the full range of devices available today, and try to make sites respond quickly and smoothly to user input. Back end developers focus on data management and server-side processing. This usualy involves a strong understanding of working with databases and APIs. Full-stack developers work on the front end and the back end, and can build full working prototypes of web sites independently.

You can find work building new sites, or maintaining any of the millions of existing interactive sites. You can work on small development teams, or you can be part of a large corporation responsible for some of the largest and most popular sites on the internet.

[top](#top)

## Data Science

Data science is a broad field. Data scientists collect, clean, analyze, and visualize data. They can work with small data sets that can be processed in RAM on a single laptop, or they can be enormous data sets that require careful planning to process efficiently. They can be largely static data sets, or they can be real-time feeds with large amounts of data coming in quickly, all the time.

A good data scientist also helps make meaningful decisions based on the data that's been collected.

[top](#top)

## Business Software Development

Business software development covers a broad range of work. Almost every business in operation these days has some need for software development. It's safe to say that every business has some inefficiencies in some of their workflows. These inefficiencies are opportunities to automate processes. People often assume the main benefit of automating processes is the time that's saved. But often there's even more benefit from developing consistent processes - processes that are less error-prone, and give more confidence that results are accurate.

If you want to focus on business software development, you can work within a single company, focusing solely on that company's needs. Or, you can work in an agency that does contract work for other companies.

This kind of work is a great way for people already working in a field to transition to software development. If you are already employed in a non-programming job, there's a fair chance you know some of that company's inefficiencies. You may be able to write code that addresses these inefficiencies; this is how many people start to write code that's used in a professional context. Be careful though, because software that's not fully thought out and tested can cause major disruptions to a compny if it does something wrong. And these issues can be hard to spot, because everybody assumes that since the process is automated, it's being done correctly. A small error can cause big, costly issues, and you don't want to be responsible for that as your first professional programming experience.

[top](#top)

## App Development

App development is closely related to web development. Many app developers started out as web developers, and many web developers spend some of their time building apps. App development usually breaks down into iOS and Android development, although plenty of people still spend time building desktop applications.

If you want to build iOS apps, you'll be using Swift and XCode. If you want to build Android apps, you'll be using Java or related lanagues like Kotlin. You're not wasting your time learning Python, though. For one thing, Python is a much friendlier first language than Swift. The fundamentals of programming you learn through Python will serve you well when you start digging into other languages like Swift or Java or Kotlin.

Another major reason it's good to know Python as an app developer is that many apps talk to a server on the backend. You can store some data on the user's device, but often times there's data that needs to be stored externally. For example, any interactions between users need to be processed through an external server. Also, any off-device backups need to be saved to an external server. When you hear that an app's data is "backed up to the cloud", it really means that data is stored on an external server. To write your server code, you can build a Django project that handles all of the external server interactions. For example, the Learning Log project in Chapters 18-20 could serve as the backend for an iOS app and an Android app. You'd need to build an API for the project, and then the apps would each talk to the Learning Log API to read and write the user's data. When people want to access their learning logs, they could then choose to go to the web site, or use an iOS app, or use an Android app.

[top](#top)

## Game Development

Game development is one of the more popular anticipated careers, but it's also one of the least understood areas. A lot of game development work is not nearly as appealing or lucrative as people tend to think it is.

Many people thing being a game tester means getting set up with your own high-end gaming rig, and getting to play the newest games before they're released. It actually means writing code to test certain aspects of the game (see Chapter 11), and playing through very specific parts of a game repeatedly to test for glitchy behavior. This can get really boring, compared to actually playing a finished game.

Many game development companies also have a reputation for pushing their developers really hard - demanding they work many more hours in a week than is healthy, for weeks and months at a time. and in the end, these developers usually don't get the financial reward that comes from building a massively popular game. Some game dev shops are even proud of how hard they drive their developers, and use that in their advertising.

Another source of frustation in the game dev world is that people go into the field thinking they're going to do creative work building fun, amazing games, only to find their day to day work comes down to trying to make users click on in-app purchases. Not many people go into game dev wanting to implement dark patters, but that's what a lot of people (unhappily) end up doing.

That said, if you are interested in game development, do some research. There are good games being produced, and if you can find a shop that treats you well, it can be really satisfying work.

Another area of game development that's really appealing is being an independent developer. This is appealing because you're in full control and you will reap the rewards of building a successful game. However, it takes a lot of work to build a well-polished, well-designed game, and it means you need to take care of things like artwork and marketing yourself. The app stores are flooded with games now, and it can be really hard to stand out even if your game is really good and built really well.

[top](#top)

## SaaS

SaaS stands for "Software as a Service". This is what takes place of desktop apps these days. Instead of building a piece of software that users install on their computers, you build the functionality on a server, and you provide a way for users to intereact with that software - either through a browser, or through an app. You are running the software on a server, and you're offering this as a service to end users.

There are many advantages of this model over the older desktop application model. It means you don't need to deal with distribution; users might need to download an app once, but they don't need to download the full application. If you have a bug in your server software, and you fix it, you know that you've fixed that bug for all of your users.

SaaS projects can be really simple, like photo-sharing apps and to-do apps, or they can be really complex like office suites. You could turn the Learning Log project (Chapters 18-20) into a SaaS project, if you could build it out in a way that people would want to pay for it.

There are a number of common business models for building SaaS proejcts. You can offer users a free trial period, and then require them to pay in order to continue using the service. You can offer your service free up to a certain amount of usage, and then charge users who go beyond that level of usage. You can have a limited free version of the service, and charge users who want access to the full set of features. You can offer the entire service for free, and hope it gets popular fast enough to attract funding which will let you build out the platform. This is the VC (venture capital) model.

Running your own SaaS project is appealing to many people. If you have a good idea for a service you think people might pay for, you can build a working prototype and then see if people are interested. It's important to put your prototype in front of other people early; it's easy to fall into the trap of building your project for years, only to find that no one is interested in your service enough to pay for it. You can also join a team for a SaaS that's already being built.

A common way to come up with an idea for a SaaS project is to watch how people in a certain field use spreadsheets. Many individuals and businesses use spreadsheets to manage their organizational data. This works, but it's often a more inefficient and fragile workflow than many people realize. Many of these workflows involving spreadsheets can be turned into SaaS projects, which can then be sold to users in similar companies.

[top](#top)

## Freelance Work

Many people who are new to programming dream about working as a freelancer. It's an appealing vision - you get to be your own boss, set your own hours, choose the projects you want to work on, and get paid well. But the reality is often quite different, and isn't really an option for people looking for their first programming job.

Freelancers do a lot more than write code. they have to find work, handle all communications related to a project, handle their own accounting (or pay someone else to do it), pay self-employment taxes, and deal with difficult clients without the backing of a company that you work for. Plus, you have to be able to handle the entire life cycle of a project - finding clients, speccing the work, developing a meaningful contract, handling changes to what was originally asked of you, responding to critical feedback, and making a plan to maintain the project. This is something most people need experience with before they can do it on their own.

If you are interested in freelance work, you might look at joining a freelancing agency. This is an umbrella company that finds clients, specs projects, and signs contracts, and then subcontracts with freelancers to implement projects. The company handles a lot of the logistics involved in freelancing, and you focus on building out the project. These agencies often prefer people with some professional experience, but if you're interested in this kind of work it won't hurt to talk to some of them early on in your career.

[top](#top)

## blah

