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

## Contributors

* [Ben Osband](https://github.com/ben-osband)
* [Alex Sviriduk](https://github.com/ZexyMLG360)
* [Shayaan Paracha](https://github.com/4PFShay)

## Making Contributions

* See [Contributing.md](Contributing.md)
