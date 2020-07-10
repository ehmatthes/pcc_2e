---
layout: default
title: Coding for Social Justice
parent: Challenges
nav_order: 40
---

# Coding for Social Justice
{: .no_toc }

## Overview
{: .no_toc }

As I wrote in [Coding is Political](/pcc_2e/), learning to code gives you power. But what does that power look like? How do you begin to exercise that power?

A full answer to these kinds of questions is lengthy, and I intend to write about that in the near future. One kind of power that you can focus on even if you're new to programming is the ability to collect and analyze data independently, rather than relying on the work of others. Learning to work with social justice related data means you no longer have to take politicans and others in power at their word when they tell you what "the data" says. You can find data, evalute it, analyze it, and present your own findings. This will help you decide who you can trust, and help you find a voice in speaking truth to power.

The challenges here begin at Chapter 2; you don't have to wait until you've finished the book in order to start applying what you've learned to social justice issues. You can use your interest in, and commitment to, social justice to solidifying your learning. Working through these kinds of exercises early on can also help you think about how you might use what you're learning about programming to address systemic issues at a personal, local, national, and international level.

I've written these exercises in response to the Black Lives Matter movement. Each exercise may not appear to relate directly to Black lives, but that's because Black people's lives are impacted by a wide range of systemic issues. For example, the US prison system disproportionally incarcerates Black people, even when controlled for type of crime committed. So there are exercises here that clearly relate to Black Lives Matter, but also exercises that relate to a number of social issues that dispoportionally impact Black people's lives. Additionally, the Black Lives Matter movement began in the US, but it has since led to global protests and renewed efforts to reject the legacy of colonialism. Some of the exercises below focus on issues in the US, but most are phrased in a way that they can be used to dig into relevant issues in different communities around the globe.

You don't have to do every challenge in the set. If one challenge depends on completing a previous challenge, that is usually indicated in the challenge. Challenges are grouped by chapter, so you'll know when you can start on each one.

## About the Data
{: .no_toc }

When addressing social justice issues there is rarely a nice, clean, official, trustworthy database to work from. People in power tend to want to hide or obscure data, particularly data that paints them in an unfavorable light. For that reason, people working in this area work from a variety of data sets, many of which are crowdsourced. Just because a data set is crowdsourced doesn't mean it's less reliable; a well-structured and sourced, transparent dataset can be more reliable than an officially produced dataset.

To support these exercises, I've identified a number of datasets that you can start working with. If you find this work meaningful, you'll probably want to find your own data sets to work with, especially for local work, and as new broader-scale projects emerge. When you're starting out, however, it can be helpful to not have to find your own data. There's a [separate page](../social_justice_datasets/) describing these data sets, and individual exercises below will focus on specific data sets from this small collection. Feel free to apply any of the exercises below to a data set you've identified in your own work.

---

## Exercises
{: .no_toc }

* 
{:toc}

---

## Chapter 2

### CSJ 2-1: Black Lives Matter

Think of a statement you would make about the Black Lives Matter movement. For example, if you were going to hold up a sign in a march or in a protest, what would your sign say?

Assign your message to a variable, and use a `print()` call to display your message.

[top](#top)

---

## Chapter 3

### CSJ 3-1: Know their Names

Store the names of victims of police brutality in a list. Print each person's name. Consider printing a message about each person as well.

Consider doing some research to learn the names of less well-known victims from your local area, in addition to more broadly-known victims.

### CSJ 3-2: Helping Organizations

One of the reasons police violence is so entrenched is that the police are the first group called not just for acute threatening situations, but also for situations involving addiction, domestic violence, mental health, and much more.

To help ground our thinking in what other resources we have available in our communities, make a list of several non-police organizations in your community that address any or all of these issues. Use the `print()` function to output the names of each of these organizations.

[top](#top)

---

## Chapter 4

### CSJ 4-1: Efficient Output

Take one of your Chapter 3 programs from this set of challenges, and replace your series of `print()` calls with a single loop. If you had different messages that can't be automated, consider writing a more general message that can be repeated for the entire list.

[top](#top)

---

## Chapter 6

In Chapter 6, we learn about dictionaries. With dictionaries, we can really start to dig into social justice issues because we can begin to connect pieces of information. I encourage you to try these exercises, but don't get lost in large data sets at this point, because you'll learn to automate much of this work in later chapters.

### CSJ 6-1: Annual Incidents of US Police Killings

Visit the [National Trends](https://mappingpoliceviolence.org/nationaltrends) page on [Mapping Police Violence](../social_justice_datasets#mapping_police_violence). Choose several years from the data shown, and make a dictionary where the keys are the years and the values are the number of people killed by police officers in the US for that year. Loop through your dictionary, and print a summary of how many people were killed for each year in your data set.

### CSJ 6-2: International Rates of Police Killings

To put things in perspective, it's helpful to know how the rates of police violence in the US compare to the rates of police violence in other nations. Wikipedia maintains a list of [international rates of killings by law enforcement officers](https://en.wikipedia.org/wiki/List_of_killings_by_law_enforcement_officers_by_country). Read through this list, and pick 5-10 countries to focus on.

Store your selected data in a dictionary, where the keys are the country names or abbreviations and the values are the rates of police violence in those countries. Use a loop to summarize your data about each country.

### CSJ 6-3: Incarceration Rates

Incarceration is an important part of the criminal justice system to understand. Take a look at this list of [incarceration rates by country](https://en.wikipedia.org/wiki/List_of_countries_by_incarceration_rate), and choose several countries to focus on. Store the names of these countries as the keys in a dictionary, and the incarceration rate as the values. Use a loop to print a series of statements that summarize the incarceration rates for each country.

### CSJ 6-4: Police Killings and Incarceration Rates

One of the values of bringing programming abilities to data analysis work is the ability to bring together information from different data sets. Complete CSJ 6-2 and CSJ 6-3, focusing on the same countries for each exercise.

Now, make a dictionary where the keys are the country names, and the values are a list with two items each. The first item is the rate of police killings for the country, and the second is the rate of incarceration for the country. Write a loop that summarizes the information you have stored about each country, for all countries in your dictionary.

[top](#top)

## Chapter 9

In Chapter 9, we learn about classes. With classes, you can model the data that you're interested in, which will make it easier to build, analyze, and present exactly the data you're interested in, even if that data comes from multiple sources.

### CSJ 9-1: National Data Modeling

Write a class that represents a country. Include attributes that allow you to store the following information about the country: name, population, percent of the population that identifies as Black, rate of police killings, and incarceration rate. Write a method that summarizes demographic information about the country, and another method that summarizes social justice statistics for the country.

Make objects representing several countries, and assign data for each attribute. Store these objects in a list, and write a loop that summarizes information about each country, by calling each of your methods.

[top](#top)

---

## Chapter 15

In Chapter 15, we learn how to make simple graphs with data that's generated within our program. We can use this same approach to plot data that we enter manually.

### CSJ 15-1: Simple Bar Graph

Choose one of the earlier exercises from Chapter 6, such as [CSJ 6-1](#csj-6-1-annual-incidents-of-us-police-killings) or [CSJ 6-2](#csj-6-2-international-rates-of-police-killings). Use Plotly to create a bar graph of the data you chose for these exercises.

[top](#top)

---

## Chapter 16

In Chapter 16, we learn how to make charts with data that we've downloaded. With these skills you can process entire datasets much more efficiently, rather than focusing on just a few pieces of data that you enter manually.

### CSJ 16-1: Police Killings by State (CSV)

In the PCC resources [available for download](https://github.com/ehmatthes/pcc_2e/zipball/master/), you can find a CSV file containing data about police killings by state in the US for the period 2013-2019. The file is at *challenges/social_justice_datasets/police_killings_by_state_2013-2019.csv*. This file was generated from the [Excel file](https://mappingpoliceviolence.org/s/MPVDatasetDownload.xlsx) available from Mapping Police Violence.

Copy this file to an appropriate location, and use what you've learned from Chapter 16 to pull each state's name and the number of Black people killed by police in that state from 2013-2019 into lists. Make a visualization of this data. You may also want to repeat this exercise by creating a dictionary where the keys are the state names and the values are the number of Black people killed in each state during this period.

The data is stored in alphabetical order by state. Consider sorting your 

### CSJ 16-2: CSV from Spreadsheet

Most spreadsheet applications such as Excel or LibreOffice Calc allow you to save a spreadsheet as a CSV file. You can only save one worksheet at a time, but this is often what you want anyway. [Download the spreadsheet](https://mappingpoliceviolence.org/s/MPVDatasetDownload.xlsx) from Mapping Police Violence, and click on the worksheet named *2013-2019 Killings by State*. Save this worksheet as a CSV file. Make a visualization of one of the columns of data in your CSV file.

Combined with what you've already learned in Chapter 16, this workflow will allow you to analyze data and create visualizations from JSON files, CSV files, and spreadsheet files.

### CSJ 16-3: Direct from Excel

The data for these exercises is coming from the Excel file you can download from [Mapping Police Violence](https://mappingpoliceviolence.org/). Previous exercises have worked from a CSV file that was generated from that Excel file. Rather than working from a CSV file, however, you can load data directly from an Excel file. Look at the [Extracting Data from Excel Files](../../beyond_pcc/extracting_from_excel/) resource, and repeat one of the previous exercises by pulling the data directly from the .xlsx file.

### CSJ 16-4: Multiple Columns

Analyzing data about police violence usually makes more sense when it's put into context. One simple way to do this is to plot several different kinds of data on one visualization. Using the Mapping Police Violence spreadsheet, choose two or more columns to plot together. For example, you might plot the percentage of each state's population that identifies as African American, and the percentage of people killed by police who are African American.

### CSJ 16-5: Data Modeling

The first worksheet in the Mapping Police Violence spreadsheet includes one entry for every individual killed by the police between 2013 and 2019, known to the maintainers of this dataset. Look over this spreadsheet to see what kind of information is included about each individual. Write a class representing an individual, which includes an attribute for each piece of information you'd like to focus on. Using what you've learned about [extracting data from Excel files]() and processing data with Python, make one instance of your class for every person listed in this worksheet.

Think of a way to analyze this data, to show patterns in the data. Focus on the kinds of questions we can ask about this data, and about the issue of police violence overall. What analysis would help answer these questions, or give us more specific information in thinking about these questions? Think of a way to summarize or visualize this data, in a way that addresses your questions. Write code that completes this analysis, and generates the output you want to see.

[top](#top)

---

## Chapter 17

### CSJ 17-1: Sorting Data

In this chapter we also saw how to use `itemgetter()` to sort a list of dictionaries by one of the keys. In many of the challenges listed here, the data is sorted alphabetically by state or country. Choose one of the previous exercises listed here, and sort the data in a non-alphabetical way. For example, you might sort a comparison of US states by the rate of police violence instead of alphabetically.

[top](#top)

---