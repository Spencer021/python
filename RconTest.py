from rcon.source import Client
import PySimpleGUI as sg
cp = sg.cprint

sg.ChangeLookAndFeel('Dark')  # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Push(), sg.Text('Enter Your Host Name'), sg.InputText(), sg.Push()],
            [sg.Push(), sg.Text('Enter Your RCON Port'), sg.InputText(), sg.Push()],
            [sg.Push(), sg.Text('Enter Your RCON Password'), sg.InputText(password_char='*'),sg.Push()],
            [sg.Push(), sg.Text('Enter your Command'), sg.Input(key='-SendCommand-'), sg.Button('Send Command'), sg.Push()],
            [sg.Push(), sg.Text('Enter chat message'), sg.Input(key='-chat-'), sg.Button('Chat'), sg.Push()],
            [sg.Push(), sg.Multiline(reroute_stdout=True, autoscroll=True, disabled=True, reroute_cprint=True, size=(50,10), key='-OUTPUT-'), sg.Push()],
            [sg.Push(), sg.Button('Ok'), sg.Button('Clear'), sg.Button('Cancel'), sg.Button('Restart'), sg.Button('Save'), sg.Push()]

]
# Create the Window
window = sg.Window('ARKON Ascended Utility', layout, size=(750,400))
sg.cprint_set_output_destination(window, '-output-')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Clear':
            window['-OUTPUT-'].update('')
    if event == 'Restart':
            with Client(values[0], int(values[1]), passwd=values[2]) as client:
                response = client.run('DoRestartLevel')
                cp(response)
    if event == 'Save':
            with Client(values[0], int(values[1]), passwd=values[2]) as client:
                response = client.run('SaveWorld')
                cp(response)
    if event == 'Chat':
            with Client(values[0], int(values[1]), passwd=values[2]) as client:
                response = client.run("Serverchat " + values['-chat-'])
                cp(response)
    if event == 'Send Command':
            with Client(values[0], int(values[1]), passwd=values[2]) as client:
                response = client.run(values['-SendCommand-'])
                cp(response)
        
        


window.close()

