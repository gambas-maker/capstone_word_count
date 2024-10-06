import tkinter as tk

from tkinter import Tk, Label, Button
from wonderwords import RandomWord

rw = RandomWord()
list_of_words = []
root = tk.Tk()

# to generate a list of random words
root.title('Word couter')

for i in range(100):
    list_of_words.append(rw.word())

print(list_of_words)
# to create the window where we display the words
var = tk.Variable(value=list_of_words)
listbox = tk.Listbox(root, listvariable=var, height=6)
# to start a minute upon any key press or button start?
listbox.pack()

# to listen to the customer input
def print_user_response(event):
    response = entry.get()
    # on space key press to compare the word with the list and check if it is correct
    print(f"User answer: {response}")

entry = tk.Entry(root, width=50)

# to count the number of words

# to scroll down the list of words


entry.pack(padx=10, pady=5)
# you have to pass an event to the function when you bind an event to the function.
# the event object contains information about the event, if you want to manipulate it

root.bind('<space>', print_user_response)

button = tk.Button(root, text='Submit', command=print_user_response)
button.pack(padx=10, pady=10)

root.mainloop()