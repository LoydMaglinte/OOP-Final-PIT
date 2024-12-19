from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, StringVar, Label
import random
import mysql.connector

# Asset directory
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Database connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="",  # Your MySQL password
        database="flashcards_db"
    )

# The flashcard class
class FlashcardApp:
    def __init__(self, window):
        self.window = window
        self.window.title("OOP Group 5 Flashcard App")
        self.window.geometry("1000x560")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.category_var = StringVar()
        self.category_var.set("Category")

        # Background image creation
        self.background_image = PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=560,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.canvas.place(x=0, y=0)

        # Initialize buttons and other elements
        self.CategoryImage = PhotoImage(file=relative_to_assets("Category.png"))
        self.CategoryHoverImage = PhotoImage(file=relative_to_assets("CategoryHover.png"))

        self.AddFlashcardImage = PhotoImage(file=relative_to_assets("AddFlashcard.png"))
        self.AddFlashcardHoverImage = PhotoImage(file=relative_to_assets("AddFlashcardHover.png"))

        self.NextQuestionImage = PhotoImage(file=relative_to_assets("NextQuestion.png"))
        self.NextQuestionHoverImage = PhotoImage(file=relative_to_assets("NextQuestionHover.png"))

        self.ShowAnswerImage = PhotoImage(file=relative_to_assets("ShowAnswer.png"))
        self.ShowAnswerHoverImage = PhotoImage(file=relative_to_assets("ShowAnswerHover.png"))

        self.category_button = Button(
            image=self.CategoryImage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.open_category_popup
        )
        self.category_button.place(x=710.0, y=42.0, width=258.0, height=61.0)
        self.category_button.bind('<Enter>', lambda e: self.category_button.config(image=self.CategoryHoverImage))
        self.category_button.bind('<Leave>', lambda e: self.category_button.config(image=self.CategoryImage))

        self.AddFlashcard = Button(
            image=self.AddFlashcardImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_add_flashcard_window,
            relief="flat"
        )
        self.AddFlashcard.place(x=33.0, y=42.0, width=258.0, height=60.95)
        self.AddFlashcard.bind('<Enter>', lambda e: self.AddFlashcard.config(image=self.AddFlashcardHoverImage))
        self.AddFlashcard.bind('<Leave>', lambda e: self.AddFlashcard.config(image=self.AddFlashcardImage))

        # Initialize question and answer entry widgets
        self.QuestionTextboxImage = PhotoImage(file=relative_to_assets("QuestionTextbox.png"))
        self.canvas.create_image(500.0, 229.5, image=self.QuestionTextboxImage)

        self.question_label = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20),
            justify="center"
        )
        self.question_label.place(x=81.0, y=126.0, width=838.0, height=205.0)

        self.AnswerTextboxImage = PhotoImage(file=relative_to_assets("AnswerTextbox.png"))
        self.canvas.create_image(500.0, 394.5, image=self.AnswerTextboxImage)

        self.answer_label = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20),
            justify="center"
        )
        self.answer_label.place(x=125.0, y=356.0, width=750.0, height=75.0)

        # Answer and Next buttons
        self.ShowAnswer = Button(
            image=self.ShowAnswerImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_answer,
            relief="flat"
        )
        self.ShowAnswer.place(x=200.0, y=455.5, width=240.0, height=62.68)
        self.ShowAnswer.bind('<Enter>', lambda e: self.ShowAnswer.config(image=self.ShowAnswerHoverImage))
        self.ShowAnswer.bind('<Leave>', lambda e: self.ShowAnswer.config(image=self.ShowAnswerImage))

        self.NextQuestion = Button(
            image=self.NextQuestionImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.next_question,
            relief="flat"
        )
        self.NextQuestion.place(x=540.0, y=455.5, width=240.0, height=62.68)
        self.NextQuestion.bind('<Enter>', lambda e: self.NextQuestion.config(image=self.NextQuestionHoverImage))
        self.NextQuestion.bind('<Leave>', lambda e: self.NextQuestion.config(image=self.NextQuestionImage))

        # Initialize first question
        self.current_question = None
        self.next_question()

        # Category label
        self.selected_category_label = Label(
            window,
            textvariable=self.category_var,
            font=("Arial", 16, "bold"),
            bg="#FFFFFF"
        )
        self.selected_category_label.place(x=371, y=10, width=258, height=30)

    def open_category_popup(self):
        category_popup = Toplevel(self.window)
        category_popup.title("Select Category")
        category_popup.geometry("300x200")
        category_popup.configure(bg='#FFFFFF')

        def select_category(category):
            self.category_var.set(category)
            category_popup.destroy()

        # Fetch categories from the database
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT DISTINCT category FROM flashcards")
        categories = cursor.fetchall()

        y_position = 20
        for category in categories:
            category_button = Button(
                category_popup,
                text=category[0],
                command=lambda c=category[0]: select_category(c),
                width=20
            )
            category_button.place(x=50, y=y_position)
            y_position += 40

        db.close()

    def open_add_flashcard_window(self):
        add_flashcard_window = Toplevel(self.window)
        add_flashcard_window.title("Add Flashcard")
        add_flashcard_window.geometry("400x300")
        add_flashcard_window.configure(bg='#FFFFFF')

        category_label = Text(add_flashcard_window, height=1, width=15)
        category_label.insert("1.0", "Category:")
        category_label.place(x=20, y=20)

        category_entry = Entry(add_flashcard_window, width=30)
        category_entry.place(x=150, y=20)

        question_label = Text(add_flashcard_window, height=1, width=15)
        question_label.insert("1.0", "Question:")
        question_label.place(x=20, y=80)

        question_entry = Entry(add_flashcard_window, width=30)
        question_entry.place(x=150, y=80)

        answer_label = Text(add_flashcard_window, height=1, width=15)
        answer_label.insert("1.0", "Answer:")
        answer_label.place(x=20, y=140)

        answer_entry = Entry(add_flashcard_window, width=30)
        answer_entry.place(x=150, y=140)

        def submit_flashcard():
            category = category_entry.get().strip()
            question = question_entry.get().strip()
            answer = answer_entry.get().strip()

            if category and question and answer:
                # Store flashcard in the database
                db = connect_to_db()
                cursor = db.cursor()
                cursor.execute(
                    "INSERT INTO flashcards (category, question, answer) VALUES (%s, %s, %s)",
                    (category, question, answer)
                )
                db.commit()
                db.close()
                self.update_category_dropdown()
                add_flashcard_window.destroy()
            else:
                print("Please fill in all fields!")

        submit_button = Button(
            add_flashcard_window,
            text="Submit",
            command=submit_flashcard,
            width=10
        )
        submit_button.place(x=150, y=200)

    def update_category_dropdown(self):
        pass

    def show_answer(self):
        if self.current_question:
            self.answer_label.delete(0, "end")
            self.answer_label.insert(0, self.current_question[1])

    def next_question(self):
        category = self.category_var.get()
        if category:
            db = connect_to_db()
            cursor = db.cursor()
            cursor.execute("SELECT question, answer FROM flashcards WHERE category = %s", (category,))
            flashcards = cursor.fetchall()
            db.close()

            if flashcards:
                self.current_question = random.choice(flashcards)
                self.question_label.delete("0", "end")
                self.question_label.insert("0", self.current_question[0])
                self.answer_label.delete(0, "end")
            else:
                self.question_label.delete("0", "end")
                self.question_label.insert("0", "No questions in this category.")
                self.answer_label.delete(0, "end")
                self.answer_label.insert("0", "No answer available.")
        else:
            self.question_label.delete("0", "end")
            self.question_label.insert("0", "This is the question area.")
            self.answer_label.delete(0, "end")
            self.answer_label.insert("0", "This is the answer area.")

if __name__ == "__main__":
    window = Tk()
    app = FlashcardApp(window)
    window.mainloop()

