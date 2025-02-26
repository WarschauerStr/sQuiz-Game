from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from quiz_creation import create_quiz_from_ui


class CreateQuizWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        loader = QUiLoader()
        self.ui = loader.load("ui/create_quiz_window.ui", self)

        # Ensure input fields are enabled
        self.ui.theme_lineEdit.setEnabled(True)
        self.ui.quiestion_lineEdit.setEnabled(True)
        self.ui.answer_A_lineEdit.setEnabled(True)
        self.ui.answer_B_lineEdit.setEnabled(True)
        self.ui.answer_C_lineEdit.setEnabled(True)
        self.ui.answer_D_lineEdit.setEnabled(True)
        self.ui.points_lineEdit.setEnabled(True)  # New field for points

        # Connect buttons
        self.ui.confirm_button.clicked.connect(self.submit_quiz)

    def submit_quiz(self):
        """Retrieve input from UI and pass it to quiz_creation.py."""
        theme = self.ui.theme_lineEdit.text().strip()
        difficulty = self.ui.choose_difficulty_comboBox.currentText().strip()
        question = self.ui.quiestion_lineEdit.text().strip()
        option_A = self.ui.answer_A_lineEdit.text().strip()
        option_B = self.ui.answer_B_lineEdit.text().strip()
        option_C = self.ui.answer_C_lineEdit.text().strip()
        option_D = self.ui.answer_D_lineEdit.text().strip()
        answer = self.ui.choose_correct_answer_comboBox.currentText().strip()
        points_text = self.ui.points_lineEdit.text().strip()  # Retrieving points input

        # Validate fields
        if not theme or not question or not option_A or not option_B or not option_C or not option_D or not points_text:
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        try:
            difficulty = int(difficulty)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid difficulty selection!")
            return

        try:
            points = int(points_text)
            if points <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Points must be a positive number!")
            return

        # Call function to save quiz
        result = create_quiz_from_ui(theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points)

        if "Question added successfully" in result:
            QMessageBox.information(self, "Success", result)
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Error", result)

    def clear_fields(self):
        """Clear input fields after successful quiz creation."""
        self.ui.theme_lineEdit.clear()
        self.ui.quiestion_lineEdit.clear()
        self.ui.answer_A_lineEdit.clear()
        self.ui.answer_B_lineEdit.clear()
        self.ui.answer_C_lineEdit.clear()
        self.ui.answer_D_lineEdit.clear()
        self.ui.points_lineEdit.clear()  # Clear points field
