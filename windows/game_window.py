from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from user import update_user_score


class GameWindow(QWidget):
    def __init__(self, stacked_widget, theme, difficulty, user_id, questions):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.theme = theme
        self.difficulty = difficulty
        self.user_id = user_id
        self.questions = questions  # Already fetched
        self.current_question_index = 0
        self.score = 0

        loader = QUiLoader()
        self.ui = loader.load("ui/game_window.ui")

        # Connect answer buttons
        self.ui.A_button.clicked.connect(lambda: self.check_answer("A"))
        self.ui.B_button.clicked.connect(lambda: self.check_answer("B"))
        self.ui.C_button.clicked.connect(lambda: self.check_answer("C"))
        self.ui.D_button.clicked.connect(lambda: self.check_answer("D"))

        # Show the first question immediately
        self.show_question()

    def show_question(self):
        """Display the current question and answer options."""
        question_data = self.questions[self.current_question_index]
        self.ui.question_label.setText(question_data[1])  # The question text
        self.ui.answer_A_label.setText(f"A: {question_data[3]}")
        self.ui.answer_B_label.setText(f"B: {question_data[4]}")
        self.ui.answer_C_label.setText(f"C: {question_data[5]}")
        self.ui.answer_D_label.setText(f"D: {question_data[6]}")

    def check_answer(self, selected_answer):
        """Check if the selected answer is correct and update score."""
        correct_answer = self.questions[self.current_question_index][2]
        if selected_answer == correct_answer:
            self.score += self.questions[self.current_question_index][7]

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        """Handle quiz completion and update the user's score."""
        QMessageBox.information(self, "Quiz Finished", f"Your total score: {self.score}")
        update_user_score(self.user_id, self.score)
        self.stacked_widget.setCurrentIndex(2)
