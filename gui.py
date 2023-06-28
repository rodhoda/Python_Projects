import functions
import tkinter as tk
import cli
# import PySimpleGUI as sg
#
# label = sg.Text("Enter a to-do: ")

# add_button = sg.Button("Add")
#
# window = sg.Window('My To-Do App',layout=[[label], [input_box, add_button]],
#                    font=("Helvetica",14))
#
# event = window.read()
# print(event)
# window.close()


# TKINTER

window = tk.Tk(className=" To-Do App")

canvas = tk.Canvas(window, width=300, height=100)
canvas.pack()

label = tk.Label(text="Enter a to-do:")
canvas.create_window(40, 20, window=label)

entry = tk.Entry(window)
canvas.create_window(140, 20, window=entry)

def add_to_do():
    input_todo = entry.get()
    todo = "add " + input_todo
    print(todo)
    cli.to_do_app(todo)
    return todo


add_button = tk.Button(text="Add", command=add_to_do)
canvas.create_window(220, 20, window=add_button)

window.mainloop()
