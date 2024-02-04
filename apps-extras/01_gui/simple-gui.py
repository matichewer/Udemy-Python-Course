import PySimpleGUI as sg

layout = [
    [sg.Text("Type some text")], 
    [sg.InputText(tooltip="Enter some text", key="input")], 
    [sg.Button("Add")]
]

window = sg.Window('My app test', 
                   layout=layout,
                   font=('Helvetica, 16')
                   )

while True:
    event, values = window.read()

    print(event)
    print(values)


window.close()
