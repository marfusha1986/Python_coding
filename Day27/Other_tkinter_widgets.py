from tkinter import *
window = Tk()
window.title("I'm learning tkinter")
window.minsize(width=600,height= 500)


entry = Entry(width=25)
entry.pack()

#Add some text to begin with
entry.insert(END,string='Some text to begin with')

#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5,width=30)
#Puts cursor in textbox
text.focus()
#Adds some text to begin with
text.insert(END,'Example of multi-line text  entry.')

#Gets current value in textbox at line 1,character 0
print(text.get('1.0',END))
text.pack()
#Spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0,to=100,command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
     #Prints 1if On button checked,otherwise 0.
    print(checked_state.get())
#Variables to hold on to checked state.0 is off,1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text='Is ON?',variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option1',value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text='Option2',value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple','Pear','Banana','Orange']
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()




window.mainloop()