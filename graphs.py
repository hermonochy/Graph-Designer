import PySimpleGUI as sg
import matplotlib.pyplot as plt

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

layout = [
    [sg.Text('Enter values for pie chart separated by commas:')],
    [sg.InputText(key='pie_values')],
    [sg.Text('Enter labels for pie chart separated by commas (optional):')],
    [sg.InputText(key='pie_labels')],
    [sg.Button('Create Pie Chart')],
    [sg.Text('Enter x values for bar chart separated by commas:')],
    [sg.InputText(key='bar_x_values')],
    [sg.Text('Enter y values for bar chart separated by commas:')],
    [sg.InputText(key='bar_y_values')],
    [sg.Button('Create Bar Chart')],
    [sg.Button('Quit')]
]

window = sg.Window('Chart Creator', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break

    if event == 'Create Pie Chart':
        pie_values = [int(val.strip()) for val in values['pie_values'].split(',')]
        pie_labels = [label.strip() for label in values['pie_labels'].split(',') if label.strip()]
        create_pie_chart(pie_values, pie_labels)

    if event == 'Create Bar Chart':
        bar_x_values = [val.strip() for val in values['bar_x_values'].split(',')]
        bar_y_values = [val.strip() for val in values['bar_y_values'].split(',') if val.strip().isdigit()]
        if len(bar_x_values) != len(bar_y_values):
            sg.popup_error('Number of x values must match number of y values!')
        else:
            bar_y_values = [int(val) for val in bar_y_values]
            create_bar_chart(bar_x_values, bar_y_values)

window.close()
