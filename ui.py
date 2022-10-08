from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score_label = Label()
        self.score_label.config(text="Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280, text="Some Question text", fill=THEME_COLOR
                                , font=("arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command=self.true_button)
        self.true_button.grid(row=2,column=0)
        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image,highlightthickness=0,command=self.false_button)
        self.wrong_button.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
       self.canvas.config(bg="white")
       if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

       else:
            self.canvas.itemconfig(self.question_text,text ="You've reached the end of the quizz ")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button(self):

        self.feedback(self.quiz.check_answer("True"))

    def false_button(self):
        is_wrong = self.quiz.check_answer("False")
        self.feedback(is_wrong)

    def feedback(self,is_wrong):
       if is_wrong:
            self.canvas.config(bg="red",highlightthickness=0)
       else:
            self.canvas.config(bg="green",highlightthickness=0)
       self.window.after(1000,self.get_next_question)



