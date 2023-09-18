#!/usr/bin/python3

import tkinter as tk

# Create the main window.
window = tk.Tk()
window.title("Calculator")

# Create the display.
display = tk.Entry(window, width=70)
display.grid(row=0, column=0, columnspan=6)

# Create the buttons a 4x4 grid.
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['.', '0', '=', '+']
]

# Define the button click handler.
def button_click(event):
    #retrieves the text of the clicked button
    button = event.widget.cget("text")
    
    if button == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif button == ".":
        if "." not in display.get():
            display.insert(tk.END, ".")
    else:
        display.insert(tk.END, button)

# Create and bind the buttons.
for i in range(4):
    for j in range(4):
        button = tk.Button(window, text=buttons[i][j])
        button.grid(row=i+1, column=j)
        button.bind("<Button-1>", button_click)  # Bind the click event

# Start the main loop.
window.mainloop()
