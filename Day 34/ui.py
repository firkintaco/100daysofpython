THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        # Images
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(140,125, width=250,text="Question text", font=FONT)

        # True/Checkmark button
        self.true_btn = Button(image=self.true_img, borderwidth=0, highlightthickness=0, command=self.true_button)
        self.true_btn.grid(column=0, row=2)

        # False / X button
        self.false_btn = Button(image=self.false_img, borderwidth=0, highlightthickness=0, command=self.false_button)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Get new question from QuizBrain and display it"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_button(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def false_button(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
