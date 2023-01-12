# Benjamin Osband
# Alexander Sviriduk
# Shayaan Paracha
# 1/11/2023
# stock-chart-viewer.py
# This is a python program that creates a graphical interface that 
# allows the user to view information about the historical prices of stocks.

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import yfinance as yf
import matplotlib
from matplotlib import style
import csv
import datetime
import os

# Makes sure all necesssary packages are installed
os.system('python Public/Scripts/installations.py')

# Variables to take in data from the GUI and pass into the
# yahoo finance api .history() method to get the data
symbol = ''
start_date = ''
end_date = ''
interval_value = ''

# Variables to track the figure and the figure agg in order to fix
# the plot replacement issue
fig = plt.figure()
fig_agg = None

# Font variable
font = 'Helvetica'

# Tells matplotlib to use Tkinter Agg and to use the ggplot style
matplotlib.use('TkAgg')
style.use('grayscale')

# Variable to store valid symbols
all_symbols = []

# Reads in the all the stock symbols from the nasdaq csv file
# and adds them to the all_symbols list
with open('Public/Data/nasdaq_data.csv', 'r') as f:
    reader = csv.reader(f)
    amr_csv = list(reader)
    for line in amr_csv:
        all_symbols.append(line[0])

#*################################ Helper functions ##################################

# Breaks down the interval value into a string and a number
# @param string interval the interval chosen by the user
# @return int string returns the number in the interval as an integer
#                    and the string as a string
def breakInterval(interval):

    num = ''
    alpha = ''

    for c in interval:
        if c.isalpha():
            alpha += c
        else:
            num += c
    
    return int(num), alpha


# Takes in a string that represents a date and converts it
# to a datetime object
# @param string date the date being converted
# @return datetime the object representing the date entered
def stringToDatetime(date):

    info = date.split('-')

    year = int(info[0])
    month = int(info[1])
    day = int(info[2])

    return datetime.datetime(year, month, day)


# Takes in a date and checks if it is formatted correctly
# @param date the date entered by the user
# @return boolean string returns True and an empty string if date
#                        is formatted correctly and False with a
#                        message if not
def checkDateFormat(date):

    try:
        date_info = date.split('-')

        year = date_info[0]
        month = date_info[1]
        day = date_info[2]
    
    except:
        return False, 'Invalid date format. Format dates as \'YYYY-MM-DD\''

    if len(year) == 4 and len(month) == 2 and len(day) == 2:
        return True, ''
    else:
        return False, 'Invalid date format. Format dates as \'YYYY-MM-DD\''


# Checks if the symbol is valid
# @param symbol the symbol put in by the user
# @return boolean string returns False and a string with a message if the
#                        symbol is not found in the list
#                        otherwise, returns True and an empty string
def checkSymbol(symbol):

    if not symbol in all_symbols:
        return False, f'{symbol} is not a valid symbol'

    return True, ''


# Checks if the dates gives by the user are valid. Makes sure both dates
# are not simply empty strings, makes sure they are formatted correctly
# via checkDateFormat(date) and makes sure the start date comes before the
# end date.
# @param start_date the start date entered by the user
# @param end_date the end date entered by the user
# @return boolean string returns True and an empty string if dates are valid
#                        and False with a message if the dates are not valid
def checkDates(start_date, end_date):

    if start_date == '' or end_date == '':
        return False, 'Missing date or dates'

    result, msg = checkDateFormat(start_date)

    if result == False:
        return result, msg
    
    result, msg = checkDateFormat(end_date)

    if result == False:
        return result, msg

    start_date_object = stringToDatetime(start_date)
    end_date_object = stringToDatetime(end_date)

    if start_date_object > end_date_object:
        return False, 'Start date must be before end date'
    
    return True, ''


# Checks if the number of data points (period / interval) is too large
# @param string start_date the start date entered by the user
# @param string end_date the end date entered by the user
# @param string interval the interval entered by the user
# @return boolean string returns false and an error message if the
#                        interval is not valid, returns true and
#                        and empty string otherwise
def checkInterval(start_date, end_date, interval):

    start_date_object = stringToDatetime(start_date)
    end_date_object = stringToDatetime(end_date)

    period = end_date_object - start_date_object

    intervalValue, unit = breakInterval(interval)

    if unit == 'm':
        intervalValue /= 1440
    elif unit == 'h':
        intervalValue /= 24
    elif unit == 'wk':
        intervalValue *= 7
    elif unit == 'mo':
        intervalValue *= 30
    
    numPoints = period.days / intervalValue

    if numPoints > 2000:
        return False, 'Too short of an interval'
    elif numPoints < 20:
        return False, 'Too long of an interval'
    
    return True, ''


# Checks if all the information put in by the user can be used to
# properly obtain data from the yahoo finance API
# @param symbol the symbol entered by the user
# @param start_date the start date entered by the user
# @param end_date the end date entered by the user
# @param interval the interval chosen by the user
# @return boolean string returns False and a message if there is an error with the data
#                        or True and an empty string if all the data is valid
def checkData(symbol, start_date, end_date, interval):
    
    result, msg = checkSymbol(symbol)

    if result == False:
        return result, msg

    result, msg = checkDates(start_date, end_date)
    
    if result == False:
        return result, msg

    result, msg = checkInterval(start_date, end_date, interval)

    if result == False:
        return result, msg
    
    return True, ''


# Draws the graph on the PySimpleGUI graph element
# @param canvas the canvas object in the GUI
# @param figure the graph being drawn on the canvas
# @return object the generated figure agg
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# Takes in all the date entered by the user, checks it via checkData()
# and then either plots data according to the inputs or displays an
# error message
# return object returns the figure object created by matplotlib
def plotData(symbol, start_date, end_date, interval):

    result, msg = checkData(symbol, start_date, end_date, interval)

    if result == True:

        window['-ERROR-'].update('')

        hist = yf.Ticker(symbol).history(
            interval=interval,
            start=start_date,
            end=end_date
        )

        plt.plot(hist)

        plt.title(symbol)
        plt.xlabel('Date')
        plt.ylabel('Price')

        fig = plt.gcf()

        return fig
    
    else:

        window['-ERROR-'].update(msg)


#*####################################### GUI Base ##########################################

sg.theme('Dark2')

layout = [
    [
        sg.Text('Symbol', font=font),
        sg.In(
            size=(5, 1),
            default_text='MSFT',
            font=font,
            enable_events=True,
            key='-SYMBOL-',
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
        ], default_value='1d', key='-I_MENU-'),
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
            size=(625,425),
            key='-CANVAS-',
        ),
        sg.Button(
            button_text='CLEAR',
            enable_events=True,
            size=(7, 1),
            button_color='red',
            font=font,
            key='-CLEAR-',
        ),
        sg.VSeperator(),
        sg.Text('', font=font, size=(20, 3), key='-ERROR-'),
    ],
]

window = sg.Window(
    'Stock Viewer',
    layout,
    location = (0, 0),
    finalize = True,
    font = 'Helvetica 18',
    element_justification='c'
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
      
        symbol = values['-SYMBOL-']
        start_date = values['-START-']
        end_date = values['-END-']
        interval_value = values['-I_MENU-']

        figure = plotData(symbol=symbol, start_date=start_date, end_date=end_date, interval=interval_value)

        fig_agg = draw_figure(window['-CANVAS-'].TKCanvas, figure)
    
    if event == '-CLEAR-':
        fig_agg.get_tk_widget().forget()
        window['-ERROR-'].update('')
    

window.close()