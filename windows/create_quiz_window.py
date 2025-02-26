from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from quiz_creation import create_quiz_from_ui


class CreateQuizWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        loader = QUiLoader()
        self.ui = loader.load("ui/create_quiz_window.ui", self)

        # Debug: Check if UI loaded successfully
        if self.ui is None:
            print("Error: Failed to load create_quiz_window.ui")
            return

        # Ensure input fields are enabled
        self.ui.theme_lineEdit.setEnabled(True)
        self.ui.question_lineEdit.setEnabled(True)  # ✅ Updated name
        self.ui.answer_A_lineEdit.setEnabled(True)
        self.ui.answer_B_lineEdit.setEnabled(True)
        self.ui.answer_C_lineEdit.setEnabled(True)
        self.ui.answer_D_lineEdit.setEnabled(True)
        self.ui.points_lineEdit.setEnabled(True)  # New field for points

        # Debug: Check if button exists
        self.confirm_button = self.ui.findChild(QWidget, "confirm_button")
        if self.confirm_button is None:
            print("Error: confirm_button not found in UI!")
        else:
            self.confirm_button.clicked.connect(self.submit_quiz)
            print("✅ confirm_button successfully connected!")

        self.back_to_main_button = self.ui.findChild(QWidget, "back_to_main_button")
        if self.back_to_main_button:
            self.back_to_main_button.clicked.connect(self.go_to_main_menu)
            print("✅ back_to_main_button connected!")  # Debugging
        else:
            print("❌ Error: back_to_main_button not found in UI!")

    def submit_quiz(self):
        """Retrieve input from UI and pass it to quiz_creation.py."""
        print("✅ submit_quiz() function started!")  # Debugging

        theme = self.ui.theme_lineEdit.text().strip()
        difficulty = self.ui.choose_difficulty_comboBox.currentText().strip()
        question = self.ui.question_lineEdit.text().strip()
        option_A = self.ui.answer_A_lineEdit.text().strip()
        option_B = self.ui.answer_B_lineEdit.text().strip()
        option_C = self.ui.answer_C_lineEdit.text().strip()
        option_D = self.ui.answer_D_lineEdit.text().strip()
        answer = self.ui.choose_correct_answer_comboBox.currentText().strip()
        points_text = self.ui.points_lineEdit.text().strip()  # Retrieving points input

        # Print input values to debug
        print(f"Theme: {theme}, Difficulty: {difficulty}, Question: {question}")
        print(f"A: {option_A}, B: {option_B}, C: {option_C}, D: {option_D}")
        print(f"Correct Answer: {answer}, Points: {points_text}")

        # Validate fields
        if not theme or not question or not option_A or not option_B or not option_C or not option_D or not points_text:
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            print("❌ Validation failed: Missing fields")
            return

        try:
            difficulty = int(difficulty)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid difficulty selection!")
            print("❌ Validation failed: Invalid difficulty")
            return

        try:
            points = int(points_text)
            if points <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Points must be a positive number!")
            print("❌ Validation failed: Invalid points value")
            return

        # Debug: Check function execution
        print(f"✅ Submitting quiz: {theme}, Difficulty: {difficulty}, Points: {points}")

        # Call function to save quiz
        result = create_quiz_from_ui(theme, difficulty, question, answer, option_A, option_B, option_C, option_D, points)

        # Print result from function
        print(f"🔄 create_quiz_from_ui() returned: {result}")

        if "Question added successfully" in result:
            QMessageBox.information(self, "Success", result)
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Error", result)

    def clear_fields(self):
        """Clear input fields after successful quiz creation."""
        self.ui.theme_lineEdit.clear()
        self.ui.question_lineEdit.clear()  # ✅ Updated name
        self.ui.answer_A_lineEdit.clear()
        self.ui.answer_B_lineEdit.clear()
        self.ui.answer_C_lineEdit.clear()
        self.ui.answer_D_lineEdit.clear()
        self.ui.points_lineEdit.clear()  # Clear points field

    def go_to_main_menu(self):
        """Switch back to the logged options window."""
        self.stacked_widget.setCurrentIndex(2)  # ✅ Move back to logged_options_window
