import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add padding to elements
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I'm here!", font=("Arial", 24, "bold"))
# my_label.pack() # must be top, bottom, left, or right
# my_label.place(x=500, y=10) # Places widget on x,y coords
my_label.grid(column=0, row=0)
my_label.config(pady=20, padx=20)

# Button
def button_clicked():
    """Prints I Got Clicked to console and changes label text to inputted text"""
    print("I got clicked")
    if not input.get() == "":
        my_label.config(text=input.get()) # input.get() takes text from input
    else:
        my_label["text"] = "Input something"


my_button = tkinter.Button(fg="white", bg="blue", text="Click Me", command=button_clicked)
my_button.grid(column=1, row=2)
my_button2 = tkinter.Button(fg="white", bg="blue", text="New Btn", command=button_clicked)
my_button2.grid(column=3, row=0)

# Entry

input = tkinter.Entry(bg="Blue", fg="white", width=10)
input.grid(column=4, row=3)


window.mainloop()