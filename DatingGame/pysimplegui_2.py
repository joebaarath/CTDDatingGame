import PySimpleGUI as sg      

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Shall we go on a date?')],
          [sg.Button('Reply immediately')],     
          [sg.Button('Reply 1h later')]]      

window = sg.Window(title='Window that stays open',margins=(15,100),layout=layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    #print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        print("Game Over")
        break     
    else:
        if event=="Reply immediately" or event=="Reply 1h later" :
            window.close()
            layout = [[sg.Text('Where do you want to go tmr?')],[sg.Button('Beach!')],[sg.Button('Cafe!')]] 
            window = sg.Window('Window that stays open', layout)  


window.close()