import PySimpleGUI as sg

#sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()
layout = [[sg.Text("Hello from PySimpleGUI",justification="center")], [sg.Button("I want to go")],[sg.Button("I'll think ill skip it")]]

# Create the window
window = sg.Window(title= "New message from Darren!", margins=(15,100),layout=layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "YES" or event == sg.WIN_CLOSED:
        break
    else:
        

window.close()
