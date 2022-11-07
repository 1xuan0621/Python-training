from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = websitte_entry.get()
    email =  email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='please don\'t leave any fields enpty!')
    else:
        is_ok = messagebox.askokcancel(title=websitte_entry.get(), message=f'These are the details entered: \n'
    f'Email: {email}\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            with open('day29/data.txt', mode='a') as data:
                data.write(f'{website} | {email} | {password}')
                websitte_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title('Password Manager')
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# lables
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Passwore:')
password_label.grid(row=3, column=0)

# entry
websitte_entry = Entry(width=46)
websitte_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=46)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,'angela@gmail.com')
password_entry = Entry(width=29)
password_entry.grid(row=3, column=1)

# button
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column= 2)
add_button = Button(text='Add', width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)



screen.mainloop()