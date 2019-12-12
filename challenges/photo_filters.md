---
layout: default
title: Photo Filters
parent: Challenges
nav_order: 30
---

# Challenges - Photo Filters
{: .no_toc }

In this investigation, you'll start out by learning how colors are represented in code. You'll represent individual colors, and then a variety of colors. You'll get more practice working with nested structures, such as a list of lists. Then, you'll use these concepts to write your own photo filters, which you can apply to your own images.

For many of these challenges, it's really helpful to have access to a color picker tool. These tools help you see different ways of representing a wide variety of colors. If you don't already have a color tool that you like, check out [this one](https://htmlcolorcodes.com/color-picker/) from htmlcolorcodes.com or [this one](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool) from Mozilla Developer Network.

You do not have to do every challenge in the set. If one challenge depends on completing a previous challenge, that is indicated in the challenge. Challenges are grouped by chapter, so you'll know when you can start on each one.

* 
{:toc}

---

## Chapter 3

In these challenges you'll explore different ways of representing colors digitally.

### Photo Filter 3-1: RGB Colors

In one of the most common formats, a color is represented as a set of three values from 0-255. Each value represents how much red, green, and blue light to mix when displaying a pixel. The color `[255, 0, 0]` represents the brightest possible red, `[0, 255, 0]` represents bright green, and `[0, 0, 255]` represents blue. In this model `[0, 0, 0]` represents black, and `[255, 255, 255]` represents white. Taken altogether, this model makes 256\*\*3 (almost 17 million) possible colors.

Use a color picker to find a color you like. Store the RGB values for this color in a list. Print each of these component values.

### Photo Filter 3-2: HSL Colors

The HSL format represents colors as three components as well. In this model the values correspond to the *hue*, *saturation*, and *lightness* of each pixel. Most online color choosers will give you the RGB or HSL values for any color you're interested in.

Using the color picker you worked with in Challenge 3-1, store the HSL values for your color in a list. Print each of these component values.

*Prerequisite: [Photo Filter 3-1: RGB Colors](#photo-filter-3-1-rgb-colors).*

### Photo Filter 3-3: Hex Colors

Another format stores individual colors as a hexadecimal string. In this model, each value ranges from 00 to FF. If you're unfamiliar with hexadecimal numbers, they start at 0 and keep going past nine; it's a base-16 number system, as opposed to the base-10 system most of us are accustomed to. In this system 00 represents 0, and FF represents 255, so you can represent just as many colors in hexadecimal as you can in the 0-255 format. The advantage is that each color is represented as a six-character string, typically preceeded by a # sign. The brightest red is `'#ff0000'`, bright green is `'#00ff00'`, and bright blue is `'#0000ff'`.

Pick three colors you like, and store them in a list using the hexadecimal color representation. Print each color.

*Prerequisite: [Photo Filter 3-1: RGB Colors](#photo-filter-3-1-rgb-colors).*

### Photo Filter 3-4: RGB Decimal Colors

In some programs, RGB colors are represented using values from 0 to 1. In this model `[1, 0, 0]` represents bright red, `[0, 1, 0]` represents bright green, and blue is `[0, 0, 1]`.  A darker red would be `[0.75, 0, 0]`.

Choose a color you like, and store its RGB values in a list, in decimal format. Print each component value.

*Prerequisite: [Photo Filter 3-1: RGB Colors](#photo-filter-3-1-rgb-colors).*

### Photo Filter 3-5: RGBa Colors

In this model there's a fourth value for each color, which is called *alpha*. This fourth value controls the opacity or transparency of the pixel. Higher alpha values are more opaque, and lower values are more transparent. The alpha component is usually a decimal value between 0 and 1, regardless of what system is used for defining the RGB components.

Choose a color you like, and store its RGBa component values in a list. Print the value of each component.

*Prerequisite: [Photo Filter 3-1: RGB Colors](#photo-filter-3-1-rgb-colors).*

[top](#top)

---

## Chapter 4

In these challenges, you'll use loops to work more efficiently with colors. You'll also start to modify colors.

### Photo Filter 4-1: Single Color Loop

Choose a color format that you want to work with. Choose a color that you like, and store its component values in a list. Write a loop that prints out each of the component values.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 4-2: Modified Color

Start with a color you like, and store its component values in a list. Make a new color based on the original color. You can do this in a for loop, or in a comprehension.

Print the original color, and the modified color.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 4-3: Grays

In digital color models, shades of gray are colors where the RGB component values are all equal. When converting a non-gray color to a shade of gray, there are a variety of ways to do this conversion, and each will usually result in a different shade of gray.

Start with a color you like, and store its component values in a list. Make the following new colors, based on your original color:

- `avg_gray`: Find the average of the three RGB values, and use this value for all three RGB values of the new color.
- `max_gray`: Find the maximum of the three RGB values, and use this value for all three RGB values of the new color.
- `min_gray`: Find the minimum of the three RGB values, and use this value for all three RGB values of the new color.
- `r_gray`: Use the red component of the original color as the value for all three RGB values of the new color.

Print your original color, and each shade of gray based on that color.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 4-4: Bumped Reds

Let's say we wanted to brighten only the red values in an image. We could do this by adding a certain amount to the red component, or multiplying the red component by a value greater than one.

Start with a color you like. Make a new color by increasing the value of the red component by a set amount. Make a second new color by multiplying the value of the red component by a value such as 1.1. Print your original color, and your two new colors.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 4-6: Brightening Colors

To make an individual pixel brighter, you need to increase the values of all three components. You can do this in a variety of ways.

Start with a color you like. Make a new color by adding a set amount to each of the component values in your original color. Make a second new color by multiplying each of the component values by a certain amount. Print your original color, and your two new colors.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 4-7: Hex Components

The advantage of representing colors in the hexadecimal format is that each color can be represented by a single six-character string, or seven with a # symbol. The disadvantage is that you have to do some work to pull out the component values if you want to work with them individually.

A string is really a list of characters, so slice notation works on strings just like it does on lists. For example, the following code pulls the file extension from a filename:

```python
filename = 'my_photo.png'
file_extension = filename[-4:]
print(file_extension)
```

Output:

```
.png
```

Pick a color you like, and assign it to a variable as a hexadecimal string. Using slices, print the red, green, and blue components of the color.

*Prerequisite: [Photo Filter 3-3: Hex Colors](#photo-filter-3-3-hex-colors).*

[top](#top)

---

## Chapter 5

In this section you'll make sure you don't have any illegally-specified colors.

### Photo Filter 5-1: Clipped Reds

Every component of a color has a maximum value. In a 0-255 representation, this is 255. Values greater than 255 may be rendered as if they were 255, or they may cause an error, depending on how the image processing software was written. It's a good idea to manage component values yourself, so you are handling out-of-bounds values in exactly the way that you want.

Start with [Challenge 4-4, Bumped Reds](#photo-filters-4-4-bumped-reds). Modify your code in a way that if the new red component has a value greater than the maximum legal value, it is reset to match the maximum value. For example if the original red value is 245 and you multiply by 1.1, you would get 269.5. This is beyond the 255 maximum, so the red value should be set to 255.

Print your original color, and your modified color. Make sure you start with a color that tests your error-checking code, such as `[254, 200, 200]`.

### Photo Filter 5-2: Bounds Checking

Store component values in a list, but make sure one or two of the component values are larger than they should be. For example, store a value greater than 255 if you're using the 0-255 model, or greater than 1 if you're using the 0-1 model.

Create a new, empty list called `new_color`. Loop through the components of your original color, and add each component to `new_color`. However, if any component is too high, store the maximum legal value for that component instead of the original value.

Print the original color, and the new color.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

[top](#top)

---

## Chapter 6

In this section you'll assign names to colors, and work with nested lists.

### Photo Filter 6-1: Named Colors

With a dictionary, you can associate numerical color values with more user-friendly names. Choose a shade of red that you like, a shade of green, and a shade of blue. Make a dictionary with three keys: `'my_red'`, `'my_green'`, and `'my_blue'`. The value for each key should be a list containing the RGB components for that color.

Loop through your dictionary, and print the name of the color and the list containing that color's components.

Write a second loop that provides more detail. This loop should print the name of each color, the list of components in that color, and each individual component in the color.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 6-2: Multiple Colors

Make a list that will hold a set of colors, and call it something like `my_colors`. Choose 4 or 5 colors that you like. For each color, store its component values in a list, and then add the list representing that color to `my_colors`.

Print `my_colors`. You should see a list containing 4 or 5 smaller lists, where each list represents a single color.

Loop through `my_colors`, and print each color individually.

Loop through `my_colors`. Inside that loop, make another loop that runs through all the component values of each color. Print the overall color, and print the component values of each color individually as well.

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 6-3: All Colors

Make an empty list called `all_colors`. Use a series of nested loops to fill the list with all possible colors in the RGB 0-255 color space. Print the length of your list to make sure you have exactly 256\*\*3=16,777,216 colors in your list.

Completing this challenge can be satisfying because you now have all possible colors stored in a single list, generated in just a few lines of code!

*Prerequisite: Any of the [Chapter 3 Challenges](#chapter-3) on this page, or familiarity with a standard component-based digital color model.*

[top](#top)

---

## Chapter 7

In this section you'll allow users to specify how much to modify an existing color.

### Photo Filter 7-1: Custom Brightening

Write a program that prompts the user for two values: a color, and a brightening factor. Make a new color that brightens each component in the original color by the amount specified by the brightening factor.

Print the original color, and the modified color.

*Prerequisite: [Photo Filter 4-6: Brightening Colors](#photo-filter-4-6-brightening-colors).*

[top](#top)

---

## Chapter 8

In this section you'll create functions that you can call on any pixel, to modify its component values.

### Photo Filter 8-1: Grayscale Function

Write a function called `to_gray_avg()`. The function should take in a color. The function should find the average of the component values of the input color, and use this average to generate a shade of gray. The function should return the shade of gray.

Store a color you like, and call your function. Print the original color, and the shade of gray.

*Prerequisite: [Photo Filter 4-3: Grays](#photo-filter-4-3-grays).*

### Photo Filter 8-2: Grayscale Functions

Write a set of functions, one for each of the different ways to convert a color to grayscale. You should have functions like `to_gray_max()`, `to_gray_min()`, `to_gray_blue()`, and any others you want to try out.

Store a color you like, and call each of these functions in turn. Print the original color, and each shade of gray derived from that color.

*Prerequisite: [Photo Filter 8-1: Grayscale Function](#photo-filter-8-1-grayscale-function)*

### Photo Filter 8-3: Grayscale Mode

Make a function called `to_gray()`, which accepts two functions; a color, and a string representing a conversion mode. The conversion mode would be strings like `'avg'`, `'max'`, `'red'`, or something similar that tells how to convert the color to gray. Use the conversion mode to call the appropriate grayscale function that you have already written.

*Prerequisite: [Photo Filter 8-2: Grayscale Functions](#photo-filter-8-2-grayscale-functions)*

### Photo Filter 8-4: Adjustment Functions

Make a series of functions that adjust colors in other ways. You might have functions like `brighten_color()`, `darken_color()`, `bump_red()`, and others.

*Prerequisite: [Photo Filter 8-1: Grayscale Function](#photo-filter-8-1-grayscale-function)*

### Photo Filter 8-5: Photo Filter Module

Place any filtering functions you want to try out on an actual image in a module called *my_filter_functions.py*. Test your module by calling one of these functions from a separate file.

*Prerequisite: Any of the [Chapter 7 Challenges](#chapter-7) from this page.*

[top](#top)

---

## Chapter 10

After completing Chapter 10, you're ready to start working with images. Read through the guide [*Pillow - Working with Images*](../../beyond_pcc/pillow/) for an overview of how to load images, and how to work with individual pixels in an image.

If you are successful with any of these challenges, I'd love to see the results! Post them on Twitter with the hashtag [#pcc_photo_filter](https://twitter.com/search?q=%23pcc_photo_filter), or send them to me at ehmatthes@gmail.

### Photo Filter 10-1: Grayscale Filter

Choose one of your grayscale filter functions that you wrote earlier. Use your grayscale filter to convert an actual color image to black and white. If you're not sure what image to use, try using the *starr_bears.jpg* image in the *beyond_pcc* folder in the resources [available for download](https://github.com/ehmatthes/pcc_2e/zipball/master/).

*Prerequisite: [Photo Filter 8-1: Grayscale Function](#photo-filter-8-1-grayscale-function)*

### Photo Filter 10-2: All Grayscales

Use a loop to apply each of the grayscale functions you've written to an image. If you're saving the images, make sure to generate a unique filename for each filter application, so you get a different saved image for each of the filters you've applied.

*Prerequisite: [Photo Filter 8-2: Grayscale Functions](#photo-filter-8-2-grayscale-functions)*

### Photo Filter 10-3: Any Function

Apply any other filtering functions you're curious about to an image.

*Prerequisite: Any of the [Chapter 7 Challenges](#chapter-7) from this page.*

### Photo Filter 10-4: All Red and Green Colors

There's a section in the guide [*Pillow - Working with Images*](../../beyond_pcc/pillow/) that shows you how to start from a blank image, and set each pixel to any color you want. Make an image that's 256 pixels wide by 256 pixels high.

Pick a single blue component value for all pixels in the image; this could be 0, or 255, or something in the middle like 150. Then write a nested loop that runs through all the possible red values, and all the possible green values.

You should end up with an image where every one of the 65,025 pixels is a different color, and all regions of the image smoothly fade into different colors.

### Photo Filter 10-5: All Colors

There are 16,777,216 possible colors in the RGB model, using values from 0-255 for each of the components. That means you can fit all of these colors in an image that's 4096 pixels wide by 4096 pixels high.

Create a new, blank image that's 4096 x 4096 pixels. Make each pixel a different color.

*Don't spend much time trying to ensure smooth transitions through all the colors. Coming up with smooth transitions through an entire colorspace is a really hard problem. Once you come up with a first solution to this challenge, you'll appreciate the work people have done to create effective colormaps.*

*Prerequisite: [Photo Filter 10-4: All Red and Green Colors](#photo-filter-10-4-all-red-and-green-colors)*

### Photo Filter 10-6: Sharpening Images

Many image manipulation programs have tools for sharpening images. This can be done by looking for adjacent pixels that have significanly different component values, and increasing the difference between those values.

For example if you look at the total brightness of two adjacent pixels, and those two totals are different by a certain amount, you would want to increase the component values of the brighter pixel, and decrease the component values of the darker pixel. This increases the contrast between these two pixels, which makes a sharper edge in that region of the image. If the difference between the two pixels' brightness totals is not different by your threshold amount, you leave the pixels as they are.

Choose a threshold for sharpening pixels. Write a program that compares each pixel to its neighboring pixels, and modifies pixels where the total brightness of adjacent pixels is above your threshold.

*This is a fairly advanced challenge. Don't be discouraged if it takes many attempts to get a working solution. This is also a challenge that can run really slowly, depending on how large your image is and how many pixel-comparisons you are making. There are mathematical and programmatic ways to make this program more efficient; if you like this challenge, it is well worth revisiting your solution periodically as you learn more about programming.*

*Prerequisite: [Photo Filter 10-1: Grayscale Filter](#photo-filter-10-1-grayscale-filter) or [Photo Filter 10-3: Any Function](#photo-filter-10-3-any-function).*

[top](#top)

## Chapter 11

In this section you'll start to verify programmatically that your filters are doing what you want them to.

### Photo Filter 11-1: Gray Filter Test

Write a test that applies one of your black and white filter functions to a color photo. The test should verify that every pixel in the processed image is gray - that is, that the r, g, and b component values are equal for each pixel.

If your filter works, your test should pass when you run it. Check that your test works by modifying your filter so it doesn't make perfect shades of gray. Then run your test, and make sure the test fails. When you're finished, make sure you change your filter back to make perfect shades of gray, and make sure your test passes again.

*Prerequisite: [Photo Filter 10-1: Grayscale Filter](#photo-filter-10-1-grayscale-filter)*

### Photo Filter 11-2: Other Filter Tests

Take a filter function that you've written, and develop a series of tests for that filter. You might start with something simple like making sure the output image is the same size as the input image. You might make sure that a test image responds to the filter in the way you expect it to.

You might use the step argument of the range function to check every 10th pixel in the image, rather than checking every single pixel. This will make your test run 10 times faster, but it might miss bugs that only affect certain pixels.

You might feed a perfectly black image to your filter, and a perfectly white image, and make sure your filter works. This will test how your filter responds to the minimum component values (0, 0, 0), and the maximum component values (255, 255, 255) as well.

*Prerequisite: Any of the [Chapter 10 Challenges](#chapter-10) from this page.*

[top](#top)

---

## Chapter 15

In this section you'll run some analysis on the actual pixel data in images.

### Photo Filter 15-1: Red Histogram

Many cameras will show you a histogram of the image you've just taken. A histogram shows you the pixel count over the range of possible brightness values. A really bright image will have more pixels with higher component values, and a dark image will have more pixels with lower component values. A really red image will have higher red component values overall than green or blue.

Take any image you've worked with. Write a program that loops over all the pixels in the image, and counts how many pixels have a red component of 0, of 1, of 2, and on up to 255. Then create a histogram plot where the x values are the possible component values, and the y values are the pixel counts for each of these possible component values.

To see the difference, run your code against a really red image and check if the histogram values are higher.

*Prerequisite: Any of the [Chapter 10 Challenges](#chapter-10) from this page.*

### Photo Filter 15-2: RGB Histograms

Write a program that creates three separate histograms - one for red component values, one for green, and one for blue.

*Prerequisite: [Photo Filter 15-1: Red Histogram](#photo-filter-15-1-red-histogram)*

### Photo Filter 15-3: Brightness Histogram

Adding up the component values of a pixel is one way to measure the overall brightness of that pixel. For example, the brightest pixel possible has component values (255, 255, 255), for a total of 765.

Write a program that finds the adds the component values for each pixel in the image. Then count how many pixels correspond to each brightness value, and make a histogram plot of these brightness values.

*Prerequisite: [Photo Filter 15-1: Red Histogram](#photo-filter-15-1-red-histogram)*

[top](#top)

---

## Chapter 20

In this section you'll make an app that users can work with to modify their images.

### Photo Filter 20-1: Photo Filter App

You can create an app that allows you to apply filters through a browser. To do this you'll need to allow users to upload and store an image, and choose a filter to apply. You'll also need to be able to display the original and processed images.

To develop a model representing an image, look at the [ImageField](https://docs.djangoproject.com/en/3.0/ref/models/fields/#imagefield) entry in the [Django Model field](https://docs.djangoproject.com/en/3.0/ref/models/fields/) reference page. To allow users to upload files, take a look at the documenation about [File Uploads](https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/).

You will also need to add two settings to *settings.py*:

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

These settings tell Django where to store uploaded files. (Django stores the image's location in the database, but it doesn't store the actual image data in the database.)

To display an image, you need to retrieve the image from the database in the view function. Let's say you retrieve a processed photo from the database and assign it to the variable `processed_image`. Include this variable in the context dictionary that you send to the template. In the template, include a line with the following form:

```
<img src="{{ processed_image.url }}">
```

This will display the image in the browser when the user loads the page associated with that template.

Create an app that allows users to upload an image. They should be able to see their image, and choose which filter to apply. When they click on the filter, they should be taken to a page that displays the processed image.

*Prerequisite: Any of the [Chapter 10 Challenges](#chapter-10) from this page.*

[top](#top)