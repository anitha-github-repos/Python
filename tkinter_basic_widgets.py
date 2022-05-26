import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)


#label

my_label = Label(text="I Am a Label", font=("Arial",24,"bold"))
my_label.pack()

# def add(*args):
#     su = 0
#     for n in args:
#         su = su+n
#     return su
#
# print(add(4,5,6,7))
# print(add(9,10,11))
# print(add(20,19))

#Button

def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()


#Entry

input = Entry(width=30)
input.insert(END, string = "Some text to begin with.")
input.pack()


#text

text = Text(height=5, width=30)
#Puts cursor in textbox
text.focus()
#Adds some text to begin woth
text.insert(END, "Example of multi-line text entry.")
#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


#Spinbox

def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#Scale
#called with current scale value

def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkboxbutton


def checkbutton_used():
    #print 1 if on button checked, otherwise 0.
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="IS On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command= radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox

def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Plums", "Orange", "Banana", "Mango"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()