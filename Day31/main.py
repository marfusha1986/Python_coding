from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


#############Create  New Flash Cards##################
def new_random_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title,text = 'French',fill='black')
    canvas.itemconfig(card_word,text = current_card['French'],fill='black')
    canvas.itemconfig(card_background,image=front_image)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word,text=current_card['English'],fill='white')
    canvas.itemconfig(card_background,image=card_back)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv',index=False)
    new_random_card()
#############Create UI#############
window = Tk()
window.title('French Flash Cards')
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
front_image= PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400,263,image=front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_back = PhotoImage('images/card_back.png')
card_title = canvas.create_text(400,150,text='',font=('Ariel',40,'italic'))
card_word = canvas.create_text(400,263,text='',font=('Ariel',60,'bold'))
canvas.grid(column=0,row=0,columnspan=2)

my_image_right = PhotoImage(file='images/right.png')
right_button = Button(image=my_image_right,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

my_image_wrong = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=my_image_wrong,highlightthickness=0,command=new_random_card)
wrong_button.grid(column=0,row=1)


new_random_card()

window.mainloop()