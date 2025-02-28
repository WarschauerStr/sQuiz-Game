from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt
from quiz_creation import create_quiz_from_ui


class CreateQuizWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        loader = QUiLoader()
        self.ui = loader.load("ui/create_quiz_window.ui", self)

        # Enable input fields
        self.ui.theme_lineEdit.setEnabled(True)
        self.ui.question_lineEdit.setEnabled(True)
        self.ui.answer_A_lineEdit.setEnabled(True)
        self.ui.answer_B_lineEdit.setEnabled(True)
        self.ui.answer_C_lineEdit.setEnabled(True)
        self.ui.answer_D_lineEdit.setEnabled(True)
        self.ui.points_lineEdit.setEnabled(True)
        self.ui.choose_difficulty_lineEdit.setEnabled(True)
        self.ui.choose_correct_answer_lineEdit.setEnabled(True)

        # Connect Confirm Button
        self.ui.confirm_button.clicked.connect(self.submit_quiz)

        # Connect Back to Main Button
        self.back_to_main_button = self.ui.findChild(QWidget, "back_to_main_button")
        if self.back_to_main_button:
            self.back_to_main_button.clicked.connect(self.go_to_main_menu)
            print("✅ back_to_main_button connected!")
        else:
            print("❌ Error: back_to_main_button not found in UI!")

    def go_to_main_menu(self):
        self.stacked_widget.setCurrentIndex(2)

    def submit_quiz(self):
        theme = self.ui.theme_lineEdit.text().strip()
        difficulty_text = self.ui.choose_difficulty_lineEdit.text().strip()
        question = self.ui.question_lineEdit.text().strip()
        option_A = self.ui.answer_A_lineEdit.text().strip()
        option_B = self.ui.answer_B_lineEdit.text().strip()
        option_C = self.ui.answer_C_lineEdit.text().strip()
        option_D = self.ui.answer_D_lineEdit.text().strip()
        answer = self.ui.choose_correct_answer_lineEdit.text().strip()
        points_text = self.ui.points_lineEdit.text().strip()

        # Validate fields
        if not theme or not difficulty_text or not question or not option_A or not option_B or not option_C or not option_D or not answer or not points_text:
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        try:
            difficulty = int(difficulty_text)
            if difficulty not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid difficulty selection! Please enter a number (1, 2, or 3).")
            return

        try:
            points = int(points_text)
            if points <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Points must be a positive number!")
            return

        # Validate that the answer is one of the allowed choices.
        if answer.upper() not in ["A", "B", "C", "D"]:
            QMessageBox.warning(self, "Error", "Correct answer must be A, B, C, or D!")
            return

        result = create_quiz_from_ui(
            theme, difficulty, question, answer.upper(),
            option_A, option_B, option_C, option_D, points
        )

        if "Question added successfully" in result:
            QMessageBox.information(self, "Success", result)
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Error", result)

    def clear_fields(self):
        self.ui.theme_lineEdit.clear()
        self.ui.question_lineEdit.clear()
        self.ui.answer_A_lineEdit.clear()
        self.ui.answer_B_lineEdit.clear()
        self.ui.answer_C_lineEdit.clear()
        self.ui.answer_D_lineEdit.clear()
        self.ui.points_lineEdit.clear()
        self.ui.choose_difficulty_lineEdit.clear()
        self.ui.choose_correct_answer_lineEdit.clear()
