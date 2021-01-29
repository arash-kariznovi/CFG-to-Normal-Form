import NormalForm as NF
import PySimpleGUI as sg


if __name__ == '__main__':

#Gui: Using PySimpleGui

#layout
    layout =[[sg.Text("Welcome to the Converter!", size=(500, 1), font=("Helvetica", 25), text_color='white',justification='center')],
                [sg.Text("Enter Number of Productions:",justification="left"),
                    sg.InputText(size=(3, 1))],
                [sg.Text("Enter Productions and Submit:")],
                [sg.Multiline(default_text='First Read the Notes:'
                                           '\n 1. Write every production in 1 line after erasing these notes'
                                           '\n 2. lambda = e ', size=(100,10))],
                [sg.Submit()],
                [sg.Text("Choose the Method:")],
                [sg.Button("Remove Lambda"),
                    sg.Button("Remove Useless"),
                    sg.Button("Remove Unit")],
                [sg.Button("Chomsky Form"),
                    sg.Button("Greibach Form")],
                [sg.Text("Developed by Arash Kariznovi.", size=(500, 1),font=("Helvetica", 10), text_color='white',justification='center')]
            ]
# create window
    window = sg.Window(title="CFG Converter", layout=layout, margins=(10, 10), size=(500, 420))


    while True:
        event, values = window.read()

        product_numbers = int(values[0])
        productions = str(values[1])


        f = open("sample.txt", "w")
        f.write(productions)
        f.close()

        a_file = open("sample.txt", "r")
        product = []
        for line in a_file:
            stripped_line = line.strip()
            product.append(stripped_line)
        a_file.close()

        grammar1 = NF.NormalForm(product, product_numbers)

        if event == "Remove Lambda":
            grammar1.remove_lambda()
            sg.popup(grammar1.productions)
        elif event == "Remove Useless":
            grammar1.remove_useless()
            sg.popup(grammar1.productions)
        elif event == "Remove Unit":
            grammar1.remove_unit()
            sg.popup(grammar1.productions)

        if event == sg.WIN_CLOSED:
            break






