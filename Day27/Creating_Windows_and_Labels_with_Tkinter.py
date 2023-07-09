from tkinter import *

window =Tk()
window.title('My first GUI program')
window.minsize(width=600,height=400)
window.config(padx = 100,pady = 200)

#Label
my_label =Label(text= 'I am a label',font=('Arial',24,'bold'))
#my_label.pack(expand = True)


my_label['text'] = 'New text'
#my_label.place(x = 0,y = 0)
my_label.grid(column=0,row=0)
my_label.config(padx = 20,pady = 20)

#Button

def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text='Click me',command=button_clicked)
#button.pack()
button.grid(column=1,row=1)

new_button = Button(text='New Button')
new_button.grid(column=2,row=0)


#Entry component
input = Entry(width=10)
#input.pack()
input.grid(column=3,row=3)





window.mainloop()
