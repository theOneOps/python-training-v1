from tkinter import *
import html

THEME_COLOR = "#375362"

class QuizUi():
    def __init__(self, thelist):

        self.window = Tk()
        self.block = 0
        self.theListLength = len(thelist)
        self.qlist = thelist
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=200, height=300)
        self.current_question = -1
        self.playerAnswer = 'True'
        self.score = 0
        self.falseImg = PhotoImage(file="./images/false.png")
        self.trueImg = PhotoImage(file="./images/true.png")

        self.theLabel = Label(text=f"score:{self.score}", font=("Arial", 10, "normal"))
        self.theLabel.config(bg=THEME_COLOR, fg="white")
        self.theLabel.grid(column=1, row=0)

        self.theCanvas = Canvas(width=300, height=250, highlightthickness=0, bg="#ffffff")
        self.text = self.theCanvas.create_text(150, 125, width=120, text="Some Question Text", font=("Arial", 12, "italic"), fill=THEME_COLOR)
        self.theCanvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.falseBtn = Button(text="", height=97, width=100, image=self.falseImg, command=self.commandFalse)
        self.falseBtn.grid(column=1, row=2)
        self.trueBtn = Button(text="", height=97, width=100, image=self.trueImg, command=self.commandTrue)
        self.trueBtn.grid(column=0, row=2)

        self.nextQuestion()

        self.window.mainloop()

    def nextQuestion(self):
        self.theCanvas.config(bg="white")
        self.block = 0
        if self.current_question == self.theListLength-1:
            self.theCanvas.itemconfig(self.text, text="You've reached the end of the questions... \n"
                                      f"your final note is {self.score}/ {self.theListLength}")
            self.trueBtn.config(state="disabled")
            self.falseBtn.config(state="disabled")


        else:
            self.current_question += 1
            theQuestion = html.unescape(self.qlist[self.current_question].text)
            self.theCanvas.itemconfig(self.text, text=theQuestion)
            print(self.current_question, self.theListLength)

    def commandFalse(self):
        self.playerAnswer = 'False'
        self.block += 1
        if self.block == 1:
            self.verifyAnswer()
        else:
            pass


    def commandTrue(self):
        self.playerAnswer = 'True'
        self.block += 1
        if self.block == 1:
            self.verifyAnswer()
        else:
            pass

    def verifyAnswer(self):
        if self.block == 1:
            if self.playerAnswer == self.qlist[self.current_question].answer:
                self.score += 1
                self.theCanvas.config(bg="Green")
                self.theLabel.config(text=f"score:{self.score}")
            else:
                self.theCanvas.config(bg="Red")
            self.window.after(1000, self.nextQuestion)
        else:
            pass






