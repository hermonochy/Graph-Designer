import modules.PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def create_pie_chart(values, labels):
    if labels:
        plt.pie(values, labels=labels, autopct='%1.1f%%')
    else:
        plt.pie(values, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

def create_bar_chart(x_labels, values):
    plt.bar(x_labels, values)
    plt.show()

def create_scatter_plot(x_values, y_values, x_label, y_label):
    plt.scatter(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def create_line_graph(x_values, y_values, x_label, y_label):
    plt.plot(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def create_line_fit(x_values, y_values, x_label, y_label):
    slope, intercept, r_value, p_value, std_err = linregress(x_values, y_values)
    line = slope * np.asarray(x_values) + intercept
    plt.plot(x_values, y_values, 'o', label='Data')
    plt.plot(x_values, line, label='Line of Best Fit', color='red')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()

    
layout = [
    [sg.Text('Enter values for pie chart separated by commas:')],
    [sg.InputText(key='pie_values')],
    [sg.Text('Enter labels for pie chart separated by commas (optional):')],
    [sg.InputText(key='pie_labels')],
    [sg.Button('Create Pie Chart')],
    [sg.Text('Enter x values for bar/chart/line plot separated by commas:')],
    [sg.InputText(key='x_values')],
    [sg.Text('Enter y values for bar chart/line plot separated by commas:')],
    [sg.InputText(key='y_values')],
    [sg.Text('X Axis Label:')],
    [sg.InputText(key='x_label')],
    [sg.Text('Y Axis Label:')],
    [sg.InputText(key='y_label')],
    [sg.Button('Create Bar Chart'), sg.Button('Create Scatter Plot'), sg.Button('Create Line Graph')],
    [sg.Button('Generate Line of Best Fit')],
    [sg.Button('Quit')]
]

window = sg.Window('Graph Designer', layout)

x_values = None
y_values = None

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'Create Pie Chart':
        try:
            pie_values = [int(val.strip()) for val in values['pie_values'].split(',')]
            pie_labels = [label.strip() for label in values['pie_labels'].split(',') if label.strip()]
            create_pie_chart(pie_values, pie_labels)
        except ValueError:
            sg.popup('Please write something!')

    if event == 'Create Bar Chart':
        x_values = [val.strip() for val in values['x_values'].split(',')]
        y_values = [val.strip() for val in values['y_values'].split(',') if val.strip().isdigit()]
        if len(x_values) != len(y_values):
            sg.popup('Number of x values must match number of y values!')
        else:
            y_values = [int(val) for val in y_values]
            create_bar_chart(x_values, y_values)

    if event == 'Create Scatter Plot':
        try:
            x_values = [float(val.strip()) for val in values['x_values'].split(',')]
            y_values = [float(val.strip()) for val in values['y_values'].split(',') if val.strip()]
            x_label = values['x_label']
            y_label = values['y_label']
            if len(x_values) != len(y_values):
                sg.popup('Number of x values must match number of y values!')
            else:
                create_scatter_plot(x_values, y_values, x_label, y_label)
        except ValueError:
            sg.popup('Please write something!')

    if event == 'Create Line Graph':
        try:
            x_values = [float(val.strip()) for val in values['x_values'].split(',')]
            y_values = [float(val.strip()) for val in values['y_values'].split(',') if val.strip()]
            x_label = values['x_label']
            y_label = values['y_label']
            if len(x_values) != len(y_values):
                sg.popup('Number of x values must match number of y values!')
            else:
                create_line_graph(x_values, y_values, x_label, y_label)
        except ValueError:
            sg.popup('Please write something!')

    if event == 'Generate Line of Best Fit':
        if x_values is not None and y_values is not None:
          try:
            create_line_fit(x_values, y_values, values['x_label'], values['y_label'])
          except:
            sg.popup('Cannot plot!') 
        else:
            sg.popup('Please create a Graph first')

window.close()
