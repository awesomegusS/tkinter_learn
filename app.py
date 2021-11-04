import tkinter as tk
import sys

# a function
# def statement(event):
#     print(sys.path)

# creating a window
window = tk.Tk()
window.title('spotify_automator')
window.geometry('300x500')


# place a text in the app
label_name = tk.Label(window, text='enter your name:')
label_name.grid(row=0, column=1)
# label_name.pack(side=tk.TOP) # bug


# add an entry
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=0)

def get_input():
    name = name_entry.get()
    print('username is {}'.format(name))


# add a button
button_name = tk.Button(window, text='submit', command=get_input)
button_name.grid(row=3, column=1)

window.mainloop()
