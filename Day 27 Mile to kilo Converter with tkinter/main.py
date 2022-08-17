from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


#label
my_label = Label(text="I Am a label", font=('Arial', 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text =  input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()
