# Stock-Viewer

For this project, we wrote a python program that creates a graphical interface that allows the user to view information about the historical prices of stocks. The program allows the user to choose:

* What stock they want to look at
* The start date and end date of data
* The interval of data points

## Core Packages

1. [PySimpleGUI](https://www.pysimplegui.org/en/latest/)
    * Used to create the user interface
2. [Yahoo Finance](https://python-yahoofinance.readthedocs.io/en/latest/api.html)
    * Used to get historical data of stock prices
3. [Matplotlib](https://matplotlib.org/stable/index.html)
    * Used to plot the data obtained from the Yahoo Finance API

## Imports

```Python
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import yfinance as yf
import matplotlib
from matplotlib import style
import csv
import datetime
import os
```

### Import Uses

1. [FigureCanvasTkAgg](https://matplotlib.org/3.3.4/api/backend_tkagg_api.html)
    * Used to integrate the matplotlib plot into the GUI. See the `draw_figure(graph, figure)` function
2. [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
    * Used to plot the data retrieved from the Yahoo Finance API
3. [matplotlib](https://matplotlib.org/stable/index.html)
    * The entire matplotlib package had to be imported in order to write `matplotlib.use('TkAgg')` which assists the integration of the plots into the GUI
4. [style](https://www.dunderdata.com/blog/view-all-available-matplotlib-styles)
    * Used to change the style of the plots
5. [PySimpleGUI](https://www.pysimplegui.org/en/latest/)
    * Used to create the user interface
6. [yfinance](https://python-yahoofinance.readthedocs.io/en/latest/api.html)
    * Used to get historical data of stock prices
7. [csv](https://docs.python.org/3/library/csv.html)
    * Used to read in data from the [nasdaq csv file](Public/Data/nasdaq_data.csv)
7. [datetime](https://docs.python.org/3/library/datetime.html)
    * Used to check the validity of dates entered by the user
8. [os](https://docs.python.org/3/library/os.html)
    * Used to run installations.py to make sure all dependencies are satisfied

## Contributors

* [Ben Osband](https://github.com/ben-osband)
* [Alex Sviriduk](https://github.com/ZexyMLG360)
* [Shayaan Paracha](https://github.com/4PFShay)

## Making Contributions

* See [Contributing.md](Contributing.md)