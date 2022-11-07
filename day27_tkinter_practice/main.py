# 2022/02/26

from tkinter import *

def button_clicked():
    # my_label['text'] = 'I got clicked'
    mile = int(input.get())
    my_label.config(text=f'{round(mile*1.609, 2)}')


window = Tk()
window.title('My Firsy GUI Program')
window.minsize(width=500, height=300)


mile_label = Label(text='Miles', font=('Arial', 24, 'bold'))
mile_label.grid(column=2, row=0)

equal_label = Label(text='is equal to', font=('Arial', 24, 'bold'))
equal_label.grid(column=0, row=1)

km_label = Label(text='Km', font=('Arial', 24, 'bold'))
km_label.grid(column=2, row=1)

my_label = Label(text='0', font=('Arial', 24, 'bold'))
my_label.grid(column=1, row=1)

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

# new_button = Button(text='New Botton')
# new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=1, row=0)




window.mainloop()