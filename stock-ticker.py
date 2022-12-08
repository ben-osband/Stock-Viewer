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

##################################### GUI Base ##########################################

ticker = ''
start_date = ''
end_date = ''
period_value = ''
interval_value = ''
plot_type = ''

#* Draws the graph on the canvas
# @param canvas the canvas object in the GUI
# @param figure the graph being drawn on the canvas
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

layout = [
    [
        sg.Text('Ticker', font='SYSTEM_DEFAULT'),
        sg.In(default_text='e.x. \'MSFT\'', size=(5, 1), font='SYSTEM_DEFAULT', enable_events=True, key='-TICKER-'),
        sg.Text('Start Date', font='SYSTEM_DEFAULT'),
        sg.In(default_text='YYYY-MM-DD', size=(10, 1), font='SYSTEM_DEFAULT', enable_events=True, key='-START-'),
        sg.Text('End Date', font='SYSTEM_DEFAULT'),
        sg.In(default_text='YYYY-MM-DD', size=(10, 1), font='SYSTEM_DEFAULT', enable_events=True, key='-END-'),
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
        sg.Button(button_text='GO', enable_events=True, size=(2, 1), button_color='green', font='SYSTEM_DEFAULT', key='-GO-'),
    ],
    [
        sg.Canvas(key='-Canvas-'),
    ],
]

window = sg.Window(
    'Stock Ticker',
    layout,
    location = (0, 0),
    finalize = True,
    font = 'Helvetica 18',
)

while True:

    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-GO-':
        try:
            
            ticker = values['-TICKER-']
            start_date = values['-START-']
            end_date = values['-END-']
            period_value = values['-P_MENU']
            interval_value = values['-I_MENU-']
            plot_type = values['-G_MENU-']

            hist = yf.Ticker(ticker).history(
                period=period_value,
                interval=interval_value,
                start=start_date,
                end=end_date,
            )
            
            fig = plt.Figure(figsize=(5, 4), dpi=100)
            
            fig.add_subplot(111).plot(hist)

            matplotlib.use('TkAgg')

            draw_figure(window['-CANVAS-'].TKCanvas, fig)

        except:
            pass

window.close()