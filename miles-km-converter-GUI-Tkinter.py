from tkinter import *


def miles_km_converter():
    miles = int(miles_input.get())
    new_text = miles*1.609
    output_label.config(text=f"{new_text}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_km_converter)
calculate_button.grid(column=1, row=2)


window.mainloop()

