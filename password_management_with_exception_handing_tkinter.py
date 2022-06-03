from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

EMAIL = "example@gmail.com"

# ----------------------------FIND PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
            user_mail = data[website_entry.get()]['Email']
            user_password = data[website_entry.get()]['Password']
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {user_mail} \nPassword: {user_password}")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showwarning(title="Error", message= f"No details for the {website_entry.get()} exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers+password_symbols+password_letters

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_to_file():
    f = open("password.txt", "a")
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "Email" : EMAIL,
            "Password" : password,
        }
    }

    if len(website)<=0 or len(password)<=0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {EMAIL} "
        #                                               f"\nPassword: {password}\nIs it ok to save?")
        try:
            with open("data.json", "r") as datafile:
                #Reading old data
                data = json.load(datafile)
        except FileNotFoundError:
            with open("data.json", "w") as datafile:
                # Saving updated data
                json.dump(new_data, datafile, indent=4)
        else:
            # updating old data
            data.update(new_data)
            with open("data.json", "w") as datafile:
                #Saving updated data
                json.dump(data, datafile, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


        # lst = [website, EMAIL, password]
        # line = ' | '.join(lst)
        # line1 = line + '\n'
        # if is_ok:
        #     f.write(line1)
        #     website_entry.delete(0, END)
        #     password_entry.delete(0, END)
    f.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search",width=20, command=search)
search_button.grid(column=2, row=1)


email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)


email_username_entry = Entry(width=41)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "example@gmail.com")

password_label = Label(text="Password:", width=35)
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=password, width=20)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=41, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()