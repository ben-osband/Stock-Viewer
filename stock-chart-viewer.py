# Benjamin Osband
# 12/7/2022
# stock-ticker.py
# description

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import yfinance as yf
import numpy as np
import matplotlib

#* Variables to take in data from the GUI and pass into the
#* yahoo finance api .history() method to get the data
#? What different options can I add
ticker = ''
start_date = ''
end_date = ''
period_value = ''
interval_value = ''
plot_type = ''

# Draws the graph on the canvas
# @param canvas the canvas object in the GUI
# @param figure the graph being drawn on the canvas
def draw_figure(graph, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, graph.Widget)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

#* Tells matplotlib to use Tkinter Agg
matplotlib.use('TkAgg')

######################################## GUI Base ##########################################

layout = [
    [
        sg.Text('Ticker', font='SYSTEM_DEFAULT'),
        sg.In(
            size=(5, 1),
            default_text='MSFT',
            font='SYSTEM_DEFAULT',
            enable_events=True,
            key='-TICKER-',
        ),
        sg.Text('Start Date', font='SYSTEM_DEFAULT'),
        sg.In(
            default_text='2020-01-01',
            size=(10, 1),
            font='SYSTEM_DEFAULT',
            enable_events=True,
            key='-START-',
        ),
        sg.Text('End Date', font='SYSTEM_DEFAULT'),
        sg.In(
            default_text='2021-01-01',
            size=(10, 1),
            font='SYSTEM_DEFAULT',
            enable_events=True,
            key='-END-',
        ),
        sg.Text('Period'),
        sg.OptionMenu(values=[
            '1d',
            '5d',
            '1mo',
            '3mo',
            '6mo',
            '1y',
            '2y',
            '5y',
            '10y',
            'ytd',
            'max'
        ], default_value='1y', key='-P_MENU-'),
        sg.Text('Interval'),
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
        sg.OptionMenu(values=[
            'line'
        ], default_value='line', key='-G_MENU-'),
        sg.Button(
            button_text='GO',
            enable_events=True,
            size=(2, 1),
            button_color='green',
            font='SYSTEM_DEFAULT',
            key='-GO-',
        ),
    ],
    [
        sg.Graph(
            canvas_size=(500, 500),
            graph_bottom_left=(0, 0),
            graph_top_right=(500, 500),
            background_color='white',
            key='-GRAPH-',
        ),
        sg.Button(
            button_text='CLEAR',
            enable_events=True,
            size=(5, 1),
            button_color='red',
            font="SYSTEM_DEFAULT",
            key='-CLEAR-',
        ),
    ],
]

window = sg.Window(
    'Stock Ticker',
    layout,
    location = (0, 0),
    finalize = True,
    font = 'Helvetica 18',
)

###################################### Event Listener ######################################

while True:

    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-GO-':
      
        ticker = values['-TICKER-']
        start_date = values['-START-']
        end_date = values['-END-']
        period_value = values['-P_MENU-']
        interval_value = values['-I_MENU-']
        plot_type = values['-G_MENU-']

        hist = yf.Ticker(ticker).history(
            period=period_value,
            interval=interval_value,
            start=start_date,
            end=end_date,
        )

        plt.plot(hist)

        plt.title(ticker)
        plt.xlabel('Date')
        plt.ylabel('Price')
            
        fig = plt.gcf()

        draw_figure(window['-GRAPH-'], fig)
    
    #if event == '-CLEAR-':

        #plt.clf()
        #canvas = window['-CANVAS-'].TKCanvas
        #canvas.delete('all')

window.close()