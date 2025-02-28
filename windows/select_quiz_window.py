from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from quiz import get_available_themes, get_quiz_questions
from windows.game_window import GameWindow

class SelectQuizWindow(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app
        loader = QUiLoader()
        self.ui = loader.load("ui/select_quiz_window.ui", self)

        self.populate_quiz_selection()
        self.ui.start_quiz_button.clicked.connect(self.start_selected_quiz)

    def populate_quiz_selection(self):
        themes = get_available_themes()
        self.ui.select_quiz_comboBox.clear()
        if themes:
            self.ui.select_quiz_comboBox.addItems(themes)
        else:
            self.ui.select_quiz_comboBox.addItem("No quizzes available")

    def start_selected_quiz(self):
        """Starts a new quiz using the selected theme and difficulty."""
        # 1. Validate the selected theme
        selected_theme = self.ui.select_quiz_comboBox.currentText()
        if not selected_theme or selected_theme == "No quizzes available":
            QMessageBox.warning(self, "Warning", "Please select a valid quiz theme!")
            return

        # 2. Validate the selected difficulty
        difficulty_text = self.ui.choose_difficulty_comboBox.currentText()
        try:
            difficulty = int(difficulty_text)
            if difficulty not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid difficulty! Please choose 1, 2, or 3.")
            return

        # 3. Check that a user is logged in
        user_id = self.main_app.current_user_id
        if user_id is None:
            QMessageBox.critical(self, "Error", "No logged-in user found.")
            return

        # 4. Fetch questions for the selected theme and difficulty
        questions = get_quiz_questions(selected_theme, difficulty)
        if not questions:
            QMessageBox.warning(self, "Error", "No questions found for this theme and difficulty.")
            self.stacked_widget.setCurrentIndex(2)  # Return to logged_options_window
            return

        # 5. Remove any old GameWindow instances
        for i in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(i)
            if isinstance(widget, GameWindow):
                self.stacked_widget.removeWidget(widget)
                widget.deleteLater()

        # 6. Create a fresh GameWindow instance and show it
        game_window = GameWindow(self.stacked_widget, selected_theme, difficulty, user_id, questions)
        self.stacked_widget.addWidget(game_window.ui)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(game_window.ui))
