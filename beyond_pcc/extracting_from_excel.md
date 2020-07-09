---
layout: default
title: Extracting Data from Excel Files
parent: Beyond PCC
nav_order: 50
---

# Extracting Data from Excel Files
{: .no_toc }

When people save data in the JSON or CSV format, they're intending for that data to be accessed programmatically. But much of the world's data is stored in spreadsheet files, and many of those files are in the Excel format. Excel is used because people can manipulate it easily, and it's a powerful tool in its own right. However, there is a lot of automation that can be done by extracting data from a spreadsheet, and this process also allows you to bring data from multiple sources into one program.

We'll first take a quick look at how to save an Excel file as a CSV file. This is sometimes the quickest and easiest way to extract data. But it's a manual process, so you would have to open the file in Excel and save it as a CSV again every time the file is updated. It's much better in many situations to just extract the data from Excel directly.

The example we'll use is the data you can download from [Mapping Police Violence](). If you can't download this from the site for some reason, you can also find a snapshot of this spreadsheet from 6/19/20 in the `beyond_pcc/social_justice_datasets/` directory of the online resources for Python Crash Course.

* 
{:toc}

---

## Converting an Excel File to CSV

You can create a CSV file from any single worksheet in an Excel workbook. To do this, first click on the tab for the worksheet you want to focus on. Then choose File > Save As, and in the File Format dropdown choose *CSV UTF-8 (Comma-delimited) (.csv)*. You'll get a message that the entire workbook can't be saved in this format, but if you click OK you'll get a copy of the current worksheet in CSV format.

To look at the file and make sure it contains the data you expect it to, locate the new CSV file in a file browser and open it with a text editor. If you open the file with a spreadsheet application like Excel, it won't look any different than a regular Excel file.

[top](#top)

## Installing `openpyxl`

We'll be using the [openpyxl](https://openpyxl.readthedocs.io/en/stable/) library to access the data in an Excel file. You can install this library with pip:

```
$ pip install --user openpyxl
```

[top](#top)

## Opening an Excel File

To follow along with this tutorial, make a folder somewhere on your system called *extracting_from_excel*. Make a *data* folder inside this directory; it's a good idea to keep your data files in their own directory. I have saved the file *mapping_police_violence_snapshot_061920.xlsx* in my *data* directory; you can work with any .xls or .xlsx file you're interested in.

The following code will open the Excel file and _____:

```python
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# List all the sheets in the file.
print("Found the following worksheets:")
for sheetname in wb.sheetnames:
    print(sheetname)
```

First we import the `load_workbook()` function, and assign the path to the data file to `data_file`. Then we call `load_workbook()` with the correct path, and assign the returned object, representing the entire workbook, to `wb`. You'll see this convention in the documentation for openpyxl.

The names of all worksheets in the file are stored in the `sheetnames` attribute. Here's the output for this data file:

```
Found the following worksheets:
2013-2019 Police Killings
2013-2019 Killings by PD
2013-2019 Killings by State
Police Killings of Black Men
```

[top](#top)

## Accessing Data in a Worksheet

We want to access the actual data in a specific worksheet. To do this, we grab the worksheet we're interested in, and then extract the data from all rows in the worksheet:

```python
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# Load one worksheet.
ws = wb['2013-2019 Killings by State']
all_rows = list(ws.rows)

print(f"Found {len(all_rows)} rows of data.")

print("\nFirst rows of data:")
for row in all_rows[:5]:
    print(row)
```

Worksheets are accessed by name through the workbook object. Here we assign a worksheet to `ws`. Once you have a worksheet object, you can access all the rows through the `ws.rows` attribute. This attribute is a *generator*, a Python object that efficiently returns one item at a time from a collection. We can convert this to the more familar list through the `list()` function. Here we create a list of all the rows in the workbook. We then print a message about how many rows were found, and print the first few rows of data:

```
Found 55 rows of data.

First rows of data:
(<Cell '2013-2019 Killings by State'.A1>, <Cell...
(<Cell '2013-2019 Killings by State'.A2>, <Cell...
(<Cell '2013-2019 Killings by State'.A3>, <Cell...
```

In this worksheet, we found 55 rows of data. Each row of data is made up of a series of cell objects.

[top](#top)

## Accessing Data from Cells

So far we have accessed the Excel file, an individual worksheet, and a series of rows. Now we can access the actual data in the cells.

To begin with, we'll look at just the data in the first row:

```python
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# Load one worksheet.
ws = wb['2013-2019 Killings by State']
all_rows = list(ws.rows)

for cell in all_rows[0]:
    print(cell.value)
```

We loop through all cells in the row, and print the value of each cell. This is accessed through the `value` attribute of the cell object.

```
State
Population
African-American Alone
% African-American
% Victims Black
Disparity
-- snip --
```

[top](#top)

## Extracting Data from Specific Cells

The previous example is helpful, perhaps, when looking at a list of headings for a worksheet over a remote connection. But usually when we're analyzing the data from a spreadsheet we can just open the file in Excel, look for the information we want, and then write code to extract that information. We usually aren't interested in every single cell in a row, though. We're often interested in selected cells in every row in the sheet.

The following example pulls data from three specific columns in each row in the file except the header row:

```python
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# Load one worksheet.
ws = wb['2013-2019 Killings by State']
all_rows = list(ws.rows)

# Pull information from specific cells.
for row in all_rows[1:5]:
    state = row[0].value
    percent_aa = row[3].value
    percent_aa_victims = row[4].value

    print(f"{state}")
    print(f"  % residents who are African American: {percent_aa}")
    print(f"  % killed by police who are African American: {percent_aa_victims}")
```

Here we loop through the first four rows after the header row. For each row, we pull the values at index 0, 3, and 4, and assign each of these to an appropriate variable name. We then print a statement summarizing what these values mean.

The output isn't quite what we expect:

```
Alabama
 =C2/B2% of residents are African American
 =G2/N2% killed by police were African American

Alaska
 =C3/B3% of residents are African American
 =G3/N3% killed by police were African American

Arizona
 =C4/B4% of residents are African American
 =G4/N4% killed by police were African American

Arkansas
 =C5/B5% of residents are African American
 =G5/N5% killed by police were African American
```

The values in these cells are actually formulas. If we want the values computed from these formulas, we need to pass the `data_only=True` flag when we load the workbook:

```python
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file, data_only=True)

# Load one worksheet.
ws = wb['2013-2019 Killings by State']
all_rows = list(ws.rows)

# Pull information from specific cells.
for row in all_rows[1:5]:
    state = row[0].value
    percent_aa = row[3].value
    percent_aa_victims = row[4].value

    print(f"\n{state}")
    print(f" {percent_aa}% of residents are African American")
    print(f" {percent_aa_victims}% killed by police were African American")
```

Now we see output that's much more like what we were expecting:

```
Alabama
 0.2617950029039261% of residents are African American
 0.37681159420289856% killed by police were African American

Alaska
 0.032754132106314705% of residents are African American
 0.12195121951219512% killed by police were African American

Arizona
 0.04052054304611518% of residents are African American
 0.09037900874635568% killed by police were African American

Arkansas
 0.15428931814955016% of residents are African American
 0.27184466019417475% killed by police were African American
```

Data analysis almost always involves some degree of reformatting. For this output, we'll round the percentages to two decimal places, and turn them into neatly-formatted integers for display:

```python
# Pull information from specific cells.
for row in all_rows[1:5]:
    state = row[0].value
    percent_aa = int(round(row[3].value, 2) * 100)
    percent_aa_victims = int(round(row[4].value, 2) * 100)
```

Here's the cleaner output:

```
Alabama
 26% of residents are African American
 38% killed by police were African American

Alaska
 3% of residents are African American
 12% killed by police were African American

Arizona
 4% of residents are African American
 9% killed by police were African American

Arkansas
 15% of residents are African American
 27% killed by police were African American
```

Be careful about rounding data during the processing phase. If you were going to pass this data to a plotting library, you probably want to do the rounding in the plotting code. This can affect your visualization. For example if two percentages round to the same value in two decimal places but they're different in the third decimal place, you'll lose the ability to sort items precisely. In this situation, it's important to ask whether the third decimal place is meaningful or not.

Also, note that you will often need to identify the specific rows that need to be looped over. Spreadsheets are nice and structured, but people are also free to write anything they want in any cell. Many spreadsheets have some notes in a few cells after all the rows of data. These can be notes about sources of the raw data, dates of data collection, authors, and more. You will probably need to exclude these rows, either by looping over a slice as shown here, or using a try/except block to only extract data if the operation for each row is successful.

[top](#top)

## Refactoring

That's probably enough to get you started working with data that's stored in Excel files, but it's worth showing a bit of refactoring on the program we've been using in this tutorial. Here's what the code looks like at this point:

```python
from openpyxl import load_workbook

data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file, data_only=True)

# Load one worksheet.
ws = wb['2013-2019 Killings by State']
all_rows = list(ws.rows)

# Pull information from specific cells.
for row in all_rows[1:5]:
    state = row[0].value
    percent_aa = int(round(row[3].value, 2) * 100)
    percent_aa_victims = int(round(row[4].value, 2) * 100)

    print(f"\n{state}")
    print(f" {percent_aa}% of residents are African American")
    print(f" {percent_aa_victims}% killed by police were African American")
```

If all we wanted to do was generate a text summary of this data, this code is probably fine. But we're probably going to do some visualization work, and maybe we want to bring in some data from another file. If we're going to do anything further, it's worth breaking this in to a couple functions. Here's how we might organize this code:

```python
from openpyxl import load_workbook


def get_all_rows(data_file, worksheet_name):
    """Get all rows from the given workbook and worksheet."""
    # Load the entire workbook.
    wb = load_workbook(data_file, data_only=True)

    # Load one worksheet.
    ws = wb[worksheet_name]
    all_rows = list(ws.rows)

    return all_rows

def summarize_data(all_rows):
    """Summarize demographic data for police killings of African Americans,
    for each state in the dataset.
    """

    for row in all_rows[1:5]:
        state = row[0].value
        percent_aa = int(round(row[3].value, 2) * 100)
        percent_aa_victims = int(round(row[4].value, 2) * 100)

        print(f"\n{state}")
        print(f" {percent_aa}% of residents are African American")
        print(f" {percent_aa_victims}% killed by police were African American")


data_file = 'data/mapping_police_violence_snapshot_061920.xlsx'
data = get_all_rows(data_file, '2013-2019 Killings by State')
summarize_data(data)
```

We organize the code into two functions, one for retrieving data and one for summarizing data. The function `get_all_rows()` can be used to load all the rows from any worksheet in any data file. The function `summarize_data()` is specific to this context, and would probably have a more specific name in a more complete project.

[top](#top)

## Further Reading

There's a lot more you can do with Excel files in your Python programs. For example, you can modify data in an existing Excel file, or you can extract the data you're interested in and generate an entirely new Excel file. To learn more about this, see the [openpyxl documentation](https://openpyxl.readthedocs.io/en/stable/index.html).

You can also extract the data from Excel and rewrite it in any other data format such as JSON or CSV.

---

[top](#top)

