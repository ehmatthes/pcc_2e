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

You do not have to do every challenge in the set. If a challenge depends on completing another set, that is indicated in the challenge. Challenges are grouped by chapter, so you'll know when you can start on each challenge.

* 
{:toc}

---

## Chapter 3

### Photo Filter 3-1: RGB Colors

In one of the most common formats, a color is represented as a set of three values from 0-255. Each value represents how much red, green, and blue light to mix when displaying a pixel. The color `[255, 0, 0]` represents the brightest possible red, `[0, 255, 0]` represents bright green, and `[0, 0, 255]` represents blue. In this model `[0, 0, 0]` represents black, and `[255, 255, 255]` represents white. Taken altogether, this model makes 256\*\*3 (almost 17 million) possible colors.

Use a color picker to find a color you like. Store the RGB values for this color in a list. Print each of these component values.

### Photo Filter 3-2: HSL Colors

The HSL format represents colors as three components as well. In this model the values correspond to the *hue*, *saturation*, and *lightness* of each pixel. Most online color choosers will give you the RGB or HSL values for any color you're interested in.

Using the color picker you worked with in Challenge 3-1, store the HSL values for your color in a list. Print each of these component values.

### Photo Filter 3-3: Hex Colors

Another format stores individual colors as a hexadecimal string. In this model, each value ranges from 00 to FF. If you're unfamiliar with hexadecimal numbers, they start at 0 and keep going past nine; it's a base-16 number system, as opposed to the base-10 system most of us are accustomed to. In this system 00 represents 0, and FF represents 255, so you can represent just as many colors in hexadecimal as you can in the 0-255 format. The advantage is that each color is represented as a six-character string, typically preceeded by a # sign. The brightest red is `'#ff0000'`, bright green is `'#00ff00'`, and bright blue is `'#0000ff'`.

Pick three colors you like, and store them in a list using the hexadecimal color representation. Print each color.

### Photo Filter 3-4: RGB Decimal Colors

In some programs, RGB colors are represented using values from 0 to 1. In this model `[1, 0, 0]` represents bright red, `[0, 1, 0]` represents bright green, and blue is `[0, 0, 1]`.  A darker red would be `[0.75, 0, 0]`.

Choose a color you like, and store its RGB values in a list, in decimal format. Print each component value.

### Photo Filter 3-5: RGBa Colors

In this model there's a fourth value for each color, which is called *alpha*. This fourth value controls the opacity or transparency of the pixel. Higher alpha values are more opaque, and lower values are more transparent. The alpha component is usually a decimal value between 0 and 1, regardless of what system is used for defining the RGB components.

Choose a color you like, and store its RGBa component values in a list. Print the value of each component.

[top](#top)

---

## Chapter 4

### Photo Filter 4-1: Single Color Loop

Choose a color format that you want to work with. Choose a color that you like, and store its component values in a list. Write a loop that prints out each of the component values.

*Prerequisite: Any of the Chapter 3 Challenges on this page, or familiarity with a standard component-based digital color model.*

### Photo Filter 4-2: Modified Color

Start with a color you like, and store its component values in a list. Make a new color based on the original color. You can do this in a for loop, or in a comprehension.

Print the original color, and the modified color.

### Photo Filter 4-3: Grays

In digital color models, shades of gray are colors where the RGB component values are all equal. When converting a non-gray color to a shade of gray, there are a variety of ways to do this conversion, and each will usually result in a different shade of gray.

Start with a color you like, and store its component values in a list. Make the following new colors, based on your original color:

- `avg_gray`: Find the average of the three RGB values, and use this value for all three RGB values of the new color.
- `max_gray`: Find the maximum of the three RGB values, and use this value for all three RGB values of the new color.
- `min_gray`: Find the minimum of the three RGB values, and use this value for all three RGB values of the new color.
- `r_gray`: Use the red component of the original color as the value for all three RGB values of the new color.

Print your original color, and each shade of gray based on that color.

### Photo Filter 4-4: Bumped Reds

Let's say we wanted to brighten only the red values in an image. We could do this by adding a certain amount to the red component, or multiplying the red component by a value greater than one.

Start with a color you like. Make a new color by increasing the value of the red component by a set amount. Make a second new color by multiplying the value of the red component by a value such as 1.1. Print your original color, and your two new colors.

### Photo Filter 4-6: Brightening Colors

To make an individual pixel brighter, you need to increase the values of all three components. You can do this in a variety of ways.

Start with a color you like. Make a new color by adding a set amount to each of the component values in your original color. Make a second new color by multiplying each of the component values by a certain amount. Print your original color, and your two new colors.

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

[top](#top)

---

## Chapter 5

### Photo Filter 5-1: Clipped Reds

Every component of a color has a maximum value. In a 0-255 representation, this is 255. Values greater than 255 may be rendered as if they were 255, or they may cause an error, depending on how the image processing software was written. It's a good idea to manage component values yourself, so you are handling out-of-bounds values in exactly the way that you want.

Start with [Challenge 4-x, Bumped Reds](). Modify your code in a way that if the new red component has a value greater than the maximum legal value, it is reset to match the maximum value. For example if the original red value is 245 and you multiply by 1.1, you would get 269.5. This is beyond the 255 maximum, so the red value should be set to 255.

Print your original color, and your modified color. Make sure you start with a color that tests your error-checking code, such as `[254, 200, 200]`.

### Photo Filter 5-2: Bounds Checking

Store component values in a list, but make sure one or two of the component values are larger than they should be. For example, store a value greater than 255 if you're using the 0-255 model, or greater than 1 if you're using the 0-1 model.

Create a new, empty list called `new_color`. Loop through the components of your original color, and add each component to `new_color`. However, if any component is too high, store the maximum legal value for that component instead of the original value.

Print the original color, and the new color.

[top](#top)

---

## Chapter 6

### Photo Filter 6-1: Named Colors

With a dictionary, you can associate numerical color values with more user-friendly names. Choose a shade of red that you like, a shade of green, and a shade of blue. Make a dictionary with three keys: `'my_red'`, `'my_green'`, and `'my_blue'`. The value for each key should be a list containing the RGB components for that color.

Loop through your dictionary, and print the name of the color and the list containing that color's components.

Write a second loop that provides more detail. This loop should print the name of each color, the list of components in that color, and each individual component in the color.

### Photo Filter 6-2: Multiple Colors

Make a list that will hold a set of colors, and call it something like `my_colors`. Choose 4 or 5 colors that you like. For each color, store its component values in a list, and then add the list representing that color to `my_colors`.

Print `my_colors`. You should see a list containing 4 or 5 smaller lists, where each list represents a single color.

Loop through `my_colors`, and print each color individually.

Loop through `my_colors`. Inside that loop, make another loop that runs through all the component values of each color. Print the overall color, and print the component values of each color individually as well.

[top](#top)

---

## Chapter 7

### Photo Filter 7-1: Custom Brightening

Write a program that prompts the user for two values: a color, and a brightening factor. Make a new color that brightens each component in the original color by the amount specified by the brightening factor.

Print the original color, and the modified color.

[top](#top)

---

## Chapter 8

### Photo Filter 8-1: Grayscale Function

Write a function called `to_gray_avg()`. The function should take in a color. The function should find the average of the component values of the input color, and use this average to generate a shade of gray. The function should return the shade of gray.

Store a color you like, and call your function. Print the original color, and the shade of gray.

### Photo Filter 8-2: Grayscale Functions

Write a set of functions, one for each of the different ways to convert a color to grayscale. You should have functions like `to_gray_max()`, `to_gray_min()`, `to_gray_blue()`, and any others you want to try out.

Store a color you like, and call each of these functions in turn. Print the original color, and each shade of gray derived from that color.

### Photo Filter 8-3: Grayscale Mode

Make a function called `to_gray()`, which accepts two functions; a color, and a string representing a conversion mode. The conversion mode would be strings like `'avg'`, `'max'`, `'red'`, or something similar that tells how to convert the color to gray. Use the conversion mode to call the appropriate grayscale function that you have already written.

### Photo Filter 8-4: Adjustment Functions

Make a series of functions that adjust colors in other ways. You might have functions like `brighten_color()`, `darken_color()`, `bump_red()`, and others.

### Photo Filter 8-5: Photo Filter Module

Place any filtering functions you want to try out on an actual image in a module called *my_filter_functions.py*. Test your module by calling one of these functions from a separate file.

[top](#top)

---

## Chapter 9

This set of challenges lets you run your filter code on actual images. To do these challenges, you'll need to install the `pillow` package. The Pillow package is a fork of the older `PIL` library, which stood for *Python Imaging Library*. You can install it on any OS with pip. (You'll see more about pip in the project chapters, but you can start using it now.)

Run this command in a terminal window:

```
$ python -m pip install --user pillow
```

You may need to use the command **python3** instead of **python**, or whichever command you use to start a Python terminal session on your system.

Challenge



[top](#top)