Overview
The Flashcard App is a graphical user interface (GUI) application designed to help users create, view, and test themselves with flashcards. It is built using Python's tkinter library, which allows for the creation of interactive desktop applications. The app enables users to:

- Organize flashcards by categories.
- Add new flashcards with a question and an answer.
- Select a category and view questions and answers randomly from that category.
- Reveal the answer for each question when desired.
- Move to the next question with ease.
- The app provides a visual interface with interactive buttons and text fields, and it also allows users to manage their categories and flashcards efficiently.

Installation
To run the Flashcard App, ensure that you have the following dependencies installed:

Prerequisites
- Python 3.x
- Tkinter (usually bundled with Python)

Steps to Install:

1.Clone or download this repository to your local machine.

2.Install Python (if not installed already) from python.org.

3.Install Tkinter (if not already installed) using the following command:

bash
-----------
pip install tk


4. Place the app's code (including all assets, images, etc.) in a folder on your local machine.

5. Run the app by executing the following command:

bash
----------------------
python flashcard_app.py

File Structure
Ensure that the folder structure follows this format:

Copy code
flashcard_app/
├── flashcard_app.py
├── assets/
│   ├── image_1.png
│   ├── Category.png
│   ├── CategoryHover.png
│   ├── AddFlashcard.png
│   ├── AddFlashcardHover.png
│   ├── NextQuestion.png
│   ├── NextQuestionHover.png
│   ├── ShowAnswer.png
│   └── ShowAnswerHover.png
Make sure the path for the assets matches the directory used in the ASSETS_PATH variable in the code.



Usage Instructions

Starting the App:
- Upon running the app, the main window will display the flashcard interface.
- You will see a background image with buttons for selecting categories, adding flashcards, and navigating through questions.


Adding Flashcards:
- To add new flashcards, click the "Add Flashcard" button at the top-left corner.
- A popup window will appear where you can specify the category, question, and answer for the flashcard.
- Click "Submit" to save the flashcard. The new flashcard will be stored and categorized for later use.


Selecting Categories:
- Click the "Category" button at the top-right corner to open a dropdown menu of available categories.
- Select a category to start viewing questions and answers from that category.


Viewing Questions and Answers:
- After selecting a category, the app will display a random question from the chosen category.
- Click the "Show Answer" button to reveal the answer to the displayed question.
- Click the "Next Question" button to move to a new random question within the selected category.


Error Handling:
- If no flashcards are available for the selected category, the question area will display a default message.


Example Functionality
Adding Flashcards:

When the user clicks the "Add Flashcard" button, a form is displayed where the user can enter:
Category: e.g., "Math", "History", etc.
Question: e.g., "What is 2 + 2?"
Answer: e.g., "4"

Selecting a Category:

Clicking the "Category" button shows a list of categories like "Math", "Science", "History". The user can choose one to filter flashcards by category.
Random Question Display:

After selecting a category, a random flashcard from that category is displayed with the question showing.
The user can then click "Show Answer" to reveal the answer, or click "Next Question" to display a different question from the same category.