from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.answer = str
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Insert question here",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        tick_img = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.tick_button.grid(column=0, row=2)
        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, bd=0, command=self.false_pressed)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        self.answer = "True"
        self.give_feedback(self.quiz.check_answer(self.answer))


    def false_pressed(self):
        self.answer = "False"
        is_right = self.quiz.check_answer(self.answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green", highlightthickness=0)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
        self.window.after(1000, self.get_next_question)











