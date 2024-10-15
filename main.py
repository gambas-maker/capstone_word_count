import tkinter as tk

from tkinter import Tk, Label, Button, messagebox
from wonderwords import RandomWord


rw = RandomWord()
list_of_words = []
root = tk.Tk()

# to generate a list of random words
root.title('Word couter')

for i in range(100):
    list_of_words.append(rw.word())
print("List of words populated.")

# to create the window where we display the words
var = tk.Variable(value=list_of_words)
listbox = tk.Listbox(root, listvariable=var, height=15)
listbox.pack()

count = 0


# to listen to the customer input
def print_user_response(event):
    global count
    response = entry.get()
    # to count the number of words
    # on space key press to compare the word with the list and check if it is correct
    list_response = response.split()
    test_selection = listbox.curselection()[-1]
    print(test_selection)
    if list_response[-1] in list_of_words:
            # to check when double space bar, to not count a point
            count+=1
            # config updates the label already displayed
            count_label.config(text=f"Number of words: {count}.")


# to display the counter
count_label = Label(text=f"Number of words: {count}.")
count_label.pack()

entry = tk.Entry(root, width=50)

# to scroll down the list of words
entry.pack(padx=10, pady=5)
# you have to pass an event to the function when you bind an event to the function.
# the event object contains information about the event, if you want to manipulate it

root.bind('<space>', print_user_response)


# to display a chrono
time_left = 60
time_running = True
chrono_label = Label(text=f"Time left: {time_left}.")
chrono_label.pack()


def chrono():
    global time_left, time_running
    print("Hello")
    if time_running == True and time_left > 0:
        time_left-=1
        chrono_label.config(text=f"Time left:{time_left}.")
        root.after(1000, chrono)
    else:
        chrono_label.config(text="Time left: 0.")
        messagebox.showinfo("Time is up!", f"60 seconds have passed. Here is your score: {count}.")



def stop_chrono():
    global time_running
    time_running = False


# to start a minute upon any key press or button start?
button_start = Button(text="Start", command=chrono)
button_start.pack()

# upon the 60 seconds, stop the chrono
button_stop = Button(text="Stop", command=stop_chrono)
button_stop.pack()


#TODO - To scroll down word list
    # upon space bar press, scroll one word down
#TODO - When double space after a word successfully typed increments +1. to be fixed.
#TODO - Implement a start again button
#TODO - Tkinter interface gets irresponsive whil open it
root.mainloop()