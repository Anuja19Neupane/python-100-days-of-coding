from tkinter import *  # it should be installed

# Tk()It helps to display the root window and  manages all the other components of the tkinter application.
window = Tk()
window.minsize(width=600, height=400)
window.config(padx=20,pady=20) #  padding le screen ko side badauxa


# Label is a widget that is used to implement display boxes where you can place text or images.
my_label = Label(window, text="I said i will never fall,",
                 font=("Arial", 24, "bold"))
my_label.config(text="Again untill I found her. ")
#my_label.pack()
# pack() le scsreen ma appear garauxa
#  pack() fill option is used to make a widget fill the entire frame
# my_label.pack(side="left")
# config le change garxa, here text is changed
# pack ma co-ordinates dina mildaina, so use place
my_label.place(x=0,y=0) 
# also can use grid for same purpose
## my_label.grid(column=0,row=0)

# Call the mainloop of Tk.
# window.mainloop() tells Python to run the Tkinter event loop.


# button


def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    # get() method returns the value of the item with the specified key
    my_label.config(text=new_text)


button = Button(window, text="Click Me", command=button_clicked)
button.pack()
# pack ra grid eutei program ma use garna paidaina, use only one

# entry

input = Entry(width=10)
# add some text to begin with
input.insert(END, string="e-mail")
# The end parameter in the print function is used to add any string. ...
input.pack()
print(input.get())


# text
text = Text(height=5, width=30)
text.focus  # focus le cursor tya rakhirakhxa
text.insert(END, "anujaneupane20@gmail.com")
print(text.get("1.0", END))  # 1 denotes line and 0 is 1st position of line
text.pack()


# spinbox
def spinbox_used():
    print(spinbox.get())
    spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    spinbox.pack()

# scale


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# checkbox


def checkbutton_used():
    print(checked_state.get())
    # prints 1 if on button checked otherwise 0
    # variable to  hold on to checked state,0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# radiobutton
# it is use to pick an option
def radio_used():
    print(radio_state.get())
# variable to hold on to which radio button value is checked.
radio_state=IntVar()
radiobutton1=Radiobutton(text="Optional1", value=1,variable=radio_state,command=radio_used)
radiobutton2=Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=4)
fruits=["apple","pear","orange"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()




window.mainloop()
