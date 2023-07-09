from tkinter import *
window = Tk()
window.minsize(width=60,height=50)
window.title('Mile to Km Converter')
window.config(padx=20,pady=20)

miles_input= Entry(width=10)
miles_input.insert(END,string='0')
miles_input.grid(column=1,row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal_to=Label(text='is equal to')
is_equal_to.grid(column=0,row=1)

km_result_label = Label(text='0')
km_result_label.grid(column=1,row=1)


km_label = Label(text = 'KM')
km_label.grid(column=2,row=1)


def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f'{km}')


button = Button(text='Calculate',command=button_clicked)
button1 = Button()
button.grid(column=1,row=2)


window.mainloop()