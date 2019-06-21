---
layout: default
title: Chapter 16
parent: Solutions
nav_order: 120
---

# Solutions - Chapter 16
{: .no_toc }

* 
{:toc}

Back to [solutions](../solutions).

---

## 16-1: Sitka Rainfall

Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file *sitka_weather_2018_simple.csv* is a header called `PRCP`, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.

```python
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and rainfall amounts from this file.
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)

# Plot the rainfall amounts.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

# Format plot.
plt.title("Daily Rainfall Amounts - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

Output

![Daily rainfall for Sitka, Alaska in 2018](../../images/solution_images/sitka_rainfall.png)

[top](#top)