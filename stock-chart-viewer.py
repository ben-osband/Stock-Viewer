# Benjamin Osband
# Alexander Sviriduk
# Shayaan 
# 12/13/2022
# stock-chart-viewer.py
# In this project, we wrote a python program that creates a graphical interface 
# that allows the user to view information about the historical prices of stocks.

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import yfinance as yf
import matplotlib
from matplotlib import style
import csv

# Variables to take in data from the GUI and pass into the
# yahoo finance api .history() method to get the data
ticker = ''
start_date = ''
end_date = ''
period_value = ''
interval_value = ''

# Variables to track the figure and the figure agg in order to fix
# the plot replacement issue
fig = plt.figure()
fig_agg = None

# Font variable
font = 'Helvetica'

# Tells matplotlib to use Tkinter Agg and to use the ggplot style
matplotlib.use('TkAgg')
style.use("ggplot")

# Variable to store valid ticker values
all_tickers = []

# Reads in the all the stock tickers from the nasdaq csv file
# and adds them to the all_tickers list
with open('Public/Data/nasdaq_data.csv', 'r') as f:
    reader = csv.reader(f)
    amr_csv = list(reader)
    for line in amr_csv:
        all_tickers.append(line[0])

#*################################ Helper functions ##################################

# Checks if all the information put in by the user can be used to
# properly obtain data from the yahoo finance API
# @param ticker the ticker entered by the user
# @param start_date the start date entered by the user
# @param end_date the end date entered by the user
# @param period the period chosen by the user
# @param interval the interval chosen by the user
def checkData(ticker, start_date, end_date):
    
    result, msg = checkTicker(ticker)

    if result == False:
        return result, msg
    
    if start_date == '' or end_date == '':
        return False, 'Missing date or dates'
    
    return True, ''


# Checks if the ticker is valid
# @param ticker the ticker symbol put in by the user
# @return boolean string returns False and a string with a message if the
#                        ticker is not found in the list
#                        otherwise, returns True and an empty string
def checkTicker(ticker):
    
    result = ticker in all_tickers

    if result != True:
        return False, 'Please enter a valid ticker'

    return result, ''


# Draws the graph on the PySimpleGUI graph element
# @param canvas the canvas object in the GUI
# @param figure the graph being drawn on the canvas
# @return object the generated figure agg
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def plotData(ticker, start_date, end_date, period, interval):

    result, msg = checkData(ticker, start_date, end_date)

    if result == True:

        window['-ERROR-'].update('')

        hist = yf.Ticker(ticker).history(
            period=period,
            interval=interval,
            start=start_date,
            end=end_date
        )

        plt.plot(hist)

        plt.title(ticker)
        plt.xlabel('Date')
        plt.ylabel('Price')

        fig = plt.gcf()

        return fig
    
    else:

        window['-ERROR-'].update(msg)


#*####################################### GUI Base ##########################################

layout = [
    [
        sg.Text('Ticker', font=font),
        sg.In(
            size=(5, 1),
            default_text='MSFT',
            font=font,
            enable_events=True,
            key='-TICKER-',
        ),
        sg.Text('Start Date', font=font),
        sg.In(
            default_text='2020-01-01',
            size=(10, 1),
            font=font,
            enable_events=True,
            key='-START-',
        ),
        sg.Text('End Date', font=font),
        sg.In(
            default_text='2021-01-01',
            size=(10, 1),
            font=font,
            enable_events=True,
            key='-END-',
        ),
        sg.Text('Period', font='SYSTEM_DEFUALT'),
        sg.OptionMenu(values=[
            'None',
            '1d',
            '5d',
            '1mo',
            '3mo',
            '6mo',
            '1y',
            '2y',
            '5y',
            '10y'
        ], default_value='1y', key='-P_MENU-'),
        sg.Text('Interval', font=font),
        sg.OptionMenu(values=[
            '1m',
            '2m',
            '5m',
            '15m',
            '30m',
            '60m',
            '90m',
            '1h',
            '1d',
            '5d',
            '1wk',
            '1mo',
            '3mo'
        ], default_value='5d', key='-I_MENU-'),
        sg.Button(
            button_text='GO',
            enable_events=True,
            size=(3, 1),
            button_color='green',
            font=font,
            key='-GO-',
        ),
    ],
    [
        sg.Canvas(
            size=(500,500),
            background_color='white',
            key='-CANVAS-'
        ),
        sg.Button(
            button_text='CLEAR',
            enable_events=True,
            size=(5, 1),
            button_color='red',
            font=font,
            key='-CLEAR-',
        ),
        sg.VSeperator(color='black'),
        sg.Text('', font=font, size=(20, 1), key='-ERROR-'),
    ],
]

window = sg.Window(
    'Stock Ticker',
    layout,
    location = (0, 0),
    finalize = True,
    font = 'Helvetica 18',
)

#*##################################### Event Listener ######################################

while True:

    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-GO-':

        # clears the current figure and forgets the figure agg if one
        # already exists
        if fig_agg != None:
            fig.clf()
            fig_agg.get_tk_widget().forget()
      
        ticker = values['-TICKER-']
        start_date = values['-START-']
        end_date = values['-END-']
        period_value = values['-P_MENU-']
        interval_value = values['-I_MENU-']

        figure = plotData(ticker=ticker, start_date=start_date, end_date=end_date, period=period_value, interval=interval_value)

        fig_agg = draw_figure(window['-CANVAS-'].TKCanvas, figure)
    
    if event == '-CLEAR-':
        fig_agg.get_tk_widget().forget()
        window['-ERROR-'].update('')
    

window.close()