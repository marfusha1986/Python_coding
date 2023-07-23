from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.canvas = Canvas(width=500,height=550,bg='#fff')
        self.question_text = self.canvas.create_text(250,
                                                     225,
                                                     width = 480,
                                                     text='Some Question Text',
                                                     fill=THEME_COLOR,
                                                     font=('Arial',15,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        self.label = Label(text = 'Score:0',bg=THEME_COLOR,fg='#fff')
        self.label.grid(column=1,row=0)

        known_image = PhotoImage(file='images/true.png')
        self.known_button = Button(image=known_image,highlightthickness=0,bg=THEME_COLOR,command=self.true_pressed)
        self.known_button.grid (column=0,row=2,pady=50)

        unknown_image = PhotoImage(file='images/false.png')
        self.unknown_button = Button(image=unknown_image,highlightthickness=0,bg=THEME_COLOR,command=self.false_pressed)
        self.unknown_button.grid(column=1,row=2,pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score:{self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.known_button.config(state='disabled')
            self.unknown_button.config(state='disabled')
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)