from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password=entry_password.get()
    new_data = {website:{
                'email':email,
                'password':password,
        }
    }

    #messagebox.showinfo(title='Title',message='Message')
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops',message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website,
        #                                message=f'These are the details entered: \nEmail:{email} \nPassword:{password}\nIs it ok to save?')
        # if is_ok:
        #     with open('data.txt','a') as data_file:
        #         data_file.write(f'{website} | {email} | {password}\n')
        try:
            with open('data.json','r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json','w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                #Saving  updated data
                json.dump(data,data_file, indent=4)
        finally:
            entry_website.delete(0,END)
            entry_password.delete(0,END)

# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='No Data File Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,message=f'Email: {email}\nPassword: {password}\n')
        else:
            messagebox.showinfo(title='Error',message=f'No details for {website} exists.')



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.minsize(width=500,height=500)
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
myPass_img = PhotoImage(file='./logo.png')
canvas.create_image(100,95,image=myPass_img)
canvas.grid(column=1,row=0)

label_website = Label(text='Website: ')
label_website.grid(column=0,row=1)

entry_website=Entry(width=25)
entry_website.grid(column=1,row=1)
entry_website.focus()

search_button = Button(text='Search',width=15,command=find_password)
search_button.grid(column=2,row=1)

label_email = Label(text='Email/Username: ')
label_email.grid(column=0,row=2)

entry_email = Entry(width=42)
entry_email.grid(column=1,row=2,columnspan=2)
entry_email.focus()
entry_email.insert(0,'afag@imanov.me')

label_password = Label(text='Password: ')
label_password.grid(column=0,row=3)

entry_password = Entry(width=25)
entry_password.grid(column=1,row=3)
entry_password.focus()

button_generate_password = Button(text='Generate Password',width=16,command=generate_password)
button_generate_password.grid(column=2,row=3)

button_add = Button(text='Add',width=42,command=save_password)
button_add.grid(column=1,row=4,columnspan=2)











window.mainloop()