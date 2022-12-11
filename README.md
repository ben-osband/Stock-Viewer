# Stock-Ticker

This is a python program that creates a graphical interface that allows the user to view information about the historical prices of stocks. The user can choose:

* What stock they want to look at
* The start date and end date of data OR the start date and how long of a period to look at
* The interval of data points
* The type of graph to plot

## Packages

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
```

### Import Uses

1. [FigureCanvasTkAgg](https://matplotlib.org/3.3.4/api/backend_tkagg_api.html)
    * Used to integrate the matplotlib plot into the GUI. See the `draw_figure(graph, figure)` function
2. [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
    * Used to plot the data retrieved from the Yahoo Finance API
4. [matplotlib](https://matplotlib.org/stable/index.html)
    * The entire matplotlib package had to be imported in order to write `matplotlib.use('TkAgg')` which assists the integration of the plots into the GUI
3. [PySimpleGUI](https://www.pysimplegui.org/en/latest/)
    * Used to create the user interface
4. [yfinance](https://python-yahoofinance.readthedocs.io/en/latest/api.html)
    * Used to get historical data of stock prices
