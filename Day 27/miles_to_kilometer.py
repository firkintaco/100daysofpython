from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=10)
window.config(padx=40, pady=20)

def calculate():
    miles_to_calculate = int(miles.get())
    kms = round((miles_to_calculate * 1.60934), 2)
    text2.config(text=kms)

#First entry
miles = Entry(width=10)
miles.grid(column=1, row=0)

# Label for text "is equal to"
text = Label(text="is equal to")
text.grid(column=0, row=1)

# Label for converted miles
text2 = Label(text="0")
text2.grid(column=1, row=1)

# Label for Miles text
text3 = Label(text="Miles")
text3.grid(column=2, row=0)

# Label for Km
text4 = Label(text="Km")
text4.grid(column=2, row=1)

# Calculate button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)

window.mainloop()