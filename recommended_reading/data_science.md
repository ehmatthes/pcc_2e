---
layout: default
title: Data Science Resources
parent: Recommended Reading
nav_order: 30
---

# Data Science Resources
{: .no_toc }

Data Science is one of the most popular areas of programming right now, and that makes sense. There's a lot of data available to work with, and the better we understand that data the more we can do with it.

*Python Crash Course* just scratches the surface of what you can do with Python in this field. If you'd like to go further with Python in Data Science, there are a large number of resouces available. I hope this helps you figure out where to go next, and if you have feedback about any of these recommendations please don't hesitate to reach out.

Note: Some of the resources mentioned in the [General Python Resources](../general_python/) have sections focused on data science. I won't repeat those resources here, but you should check them out.

* 
{:toc}

---

## Books and Print Resources

### Fundamentals of Data Visualization, by [Claus O. Wilke](https://twitter.com/ClausWilke)

This first recommendation is non-technical, because working with data is more than just a technical endeavor. When we present data, we use it to tell a story. Even if you only work with raw data and someone else creates visualizations based on your work, you are still involved in using data to tell a story. And the stories we tell with data impact people's lives more and more all the time.

*Fundamentals of Data Visualization* is language-agnostic - there's no code in the book. Other texts mentioned here will show you how to change the colors in your visualizations; this text will tell you when and why to change the colors, and how that will impact the stories your data will tell.

You can read *Fundamentals of Data Visualization* through [O'Reilly's online platform](http://shop.oreilly.com/product/0636920137733.do), or you can buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/fundamentals-of-data-visualization-claus-o-wilke/1128580869) or [Amazon](https://www.amazon.com/Fundamentals-Data-Visualization-Informative-Compelling/dp/1492031089). You can also see all of the visualizations in the book, and an earlier draft of the text, at the [author's website](https://serialmentor.com/dataviz/).

![](../../images/recommended_reading/fdv_cover.jpg)

[top](#top)

### Python Data Science Handbook, by [Jake VanderPlas](https://twitter.com/jakevdp)

Jake VanderPlas has been involved in the Python data science and visualization community for a long time. He has given many talks, and contributed to a number of prominent open source libraries in this area. *Python Data Science Handbook* came out in December of 2016, but it's still receiving strong reviews. I haven't read the book, but I have attended many of Jake's talks and learned a great deal from following his work. This book covers common Python data science tools, loading and processing data, visualizing data, and getting started with machine learning. When I have time to do more reading, this is the first data science book I'll work through.

You can read *Python Data Science Handbook* through [O'Reilly's online platform](http://shop.oreilly.com/product/0636920034919.do), or you can buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/python-data-science-handbook-jake-vanderplas/1124463128?ean=9781491912058) or [Amazon](https://www.amazon.com/Python-Data-Science-Handbook-Essential/dp/1491912057/). You can also find the entire text online at [the author's site](https://jakevdp.github.io/PythonDataScienceHandbook/).

![](../../images/recommended_reading/pdsh_cover.jpeg)

[top](#top)

### Python for Data Analysis, by [Wes McKinney](https://twitter.com/wesmckinn)

Wes McKinney is the creator of [pandas](https://pandas.pydata.org), a prominent Python library for loading and working with raw data. Wes knows pandas inside and out, so the information is accurate and reliable. There's some criticism that the material is dry and just like reading documentation, but if you like books better than documenation this book will probably be worthwhile. If you want to read a more detailed comparison between this book and *Python Data Science Handbook*, there's a nice writeup [here](http://sam-koblenski.blogspot.com/2019/02/tech-book-face-off-python-for-data.html).

You can read *Python for Data Analysis* through [O'Reilly's online platform](http://shop.oreilly.com/product/0636920050896.do), or you can buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/python-for-data-analysis-wes-mckinney/1124074589) or [Amazon](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662/). You can also find the code for the book online at [github.com/wesm/pydata-book/](https://github.com/wesm/pydata-book).

![](../../images/recommended_reading/pda_cover.jpg)

[top](#top)

### Data Science from Scratch, by [Joel Grus](https://twitter.com/joelgrus)

*Data Science from Scratch* should be a good followup to PCC if you're new to programming and data science. With the understanding of Python you've gained from PCC, you should be able to follow the code examples and learn the more data science-focused concepts the book presents. If you already understand data science and machine learning concepts and want to focus on using the latest libraries to implement these methods, a book like *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* is proably a better fit.

You can read *Data Science from Scratch* through [O'Reilly's online platform](https://www.oreilly.com/library/view/data-science-from/9781492041122/), or you can buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/data-science-from-scratch-joel-grus/1121709189) or [Amazon](https://www.amazon.com/Joel-Grus/dp/1492041130/). You can see the [table of contents](https://www.oreilly.com/library/view/data-science-from/9781492041122/), and you can find the code for the book at the [author's GitHub site](https://github.com/joelgrus/data-science-from-scratch).

![](../../images/recommended_reading/dss_cover.jpg)

[top](#top)

### Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (2nd Edition), by [Aurélien Géron](https://twitter.com/aureliengeron/)

This book focuses on using the Scikit-Learn and TensorFlow libraries to do applied machine learning work. If you want to get straight to the point of using machine learn processes in code, this is probably a good book to consider.

You can read *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* through [O'Reilly's online platform](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/), or you can buy it from [Barnes and Noble](https://www.barnesandnoble.com/w/hands-on-machine-learning-with-scikit-learn-keras-and-tensorflow-aurelien-geron/1128814321?ean=9781492032649) or [Amazon](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646/). You can also read the [table of contents here](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/).

![](../../images/recommended_reading/hml_cover.jpg)

[top](#top)

---

## Data Science Tools and Libraries

If you're interested in data science using Python, there are a nubmer of tools and libraries you should be aware of. All of these tools are covered to differing degrees in the books above, and whichever resources you choose to work from you should be aware of these different libraries.

### Jupyter Notebooks and IPython

Jupyter Notebooks are a really powerful tool with many uses, and one of the most prominent uses is exploratory data analysis. Jupyter Notebooks run in a browser, and they're made up of cells. Each cell can be a code cell or a text cell. When a code cell is run, all the variables and objects created in that cell are then available to the other code cells in the notebook. Text cells are implemented in markdown, a text-based formatting language that's used extensively in technical documentation work.

Jupyter Notebooks ar prominent in data analysis and scientific fields becasuse you can write all the explanatory text you want around your code. They're not perfect; you can sometimes run into difficulty when code cells affect each other in unexpected ways. Code cells can also be run in any order; this is good most of the time, but can generate reproducibilty issues without a clear set of guidelines for how a notebook is used.

IPython is an enhanced version of a Python terminal session. Jupyter Notebooks are built on top of IPython, but IPython itself is still used in many areas.

The Jupyter homepage is at [jupyter.org](https://jupyter.org), and the official documentation is [here](https://jupyter.readthedocs.io/en/latest/). The documentation for IPython is [here](https://ipython.readthedocs.io/en/stable/).

### pandas

The pandas library is a critical tool in the Python data science ecosystem. pandas is used to load, clean, and analyze data before feeding the data into a visualization package. It's also heavily used in machine learning applications.

The homepage for pandas is at [pandas.pydata.org](https://pandas.pydata.org).

### NumPy

NumPy is a math-focused Python package which focuses on making a wide range of mathematical operations efficient and easy to work with from within Python. For example, NumPy offers an efficient and powerful representation of multidimensional arrays. NumPy also provides an interface for working with mathematical code written in other languages such as Fortran and C++. Many other Python data science projects depend on NumPy. Even if you rarely work with NumPy directly, you're probably using it under the hood through the other data science-focused libraries you're working with.

The NumPy homepage is at [numpy.org](https://numpy.org).

### Scikit-Learn

Scikit-Learn is a library focused on implementing machine learning algorithms. It's used for classification, regression, clustering, modeling, and more.

The homepage is at [scikit-learn.org](https://scikit-learn.org/stable/).

### PyTorch

PyTorch is another Python machine learning library. 

The homepage is at [pytorch.org](https://pytorch.org).

### TensorFlow

TensorFlow was originally developed for internal use at Google. It was later released for public use. TensorFlow is focused on deep learning, and working with larger data sets.

The homepage for TensorFlow is at [tensorflow.org](https://www.tensorflow.org).




### Anaconda

[top](#top)