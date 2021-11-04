import tkinter as tk

# a function
def statement(event):
    print("I still can't see my label")

# creating a window

window = tk.Tk()
window.title('spotify_automator')
window.geometry('300x500')

# place a text in the app
label_name = tk.Label(window, text='some_text')
label_name.grid(row=0, column=1)
# label_name.pack(side=tk.TOP) # bug

# add a button
button_name = tk.Button(window, text='activate')
button_name.grid(row=150, column=150)
button_name.bind('<Button-1>', statement)

window.mainloop()
