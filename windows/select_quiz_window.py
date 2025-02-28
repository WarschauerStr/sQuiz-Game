from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from quiz import get_available_themes
from windows.game_window import GameWindow

class SelectQuizWindow(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app  # Reference to main application (for accessing current_user_id)
        loader = QUiLoader()
        self.ui = loader.load("ui/select_quiz_window.ui", self)
        
        self.populate_quiz_selection()
        
        # Connect the start quiz button to the start_selected_quiz function.
        self.ui.start_quiz_button.clicked.connect(self.start_selected_quiz)
    
    def populate_quiz_selection(self):
        """Retrieve available quiz themes and populate the combo box."""
        themes = get_available_themes()
        self.ui.select_quiz_comboBox.clear()
        if themes:
            self.ui.select_quiz_comboBox.addItems(themes)
        else:
            self.ui.select_quiz_comboBox.addItem("No quizzes available")
    
    def start_selected_quiz(self):
        """Starts a new quiz using the selected theme and difficulty."""
        # Get the selected theme.
        selected_theme = self.ui.select_quiz_comboBox.currentText()
        if not selected_theme or selected_theme == "No quizzes available":
            QMessageBox.warning(self, "Warning", "Please select a valid quiz theme!")
            return
        
        # Retrieve and validate the selected difficulty.
        difficulty_text = self.ui.choose_difficulty_comboBox.currentText()
        try:
            difficulty = int(difficulty_text)
            if difficulty not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid difficulty! Please choose 1, 2, or 3.")
            return
        
        # Ensure a user is logged in.
        user_id = self.main_app.current_user_id
        if user_id is None:
            QMessageBox.critical(self, "Error", "No logged-in user found.")
            return
        
        # Remove any existing GameWindow instance to avoid duplicate windows.
        for i in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(i)
            if isinstance(widget, GameWindow):
                self.stacked_widget.removeWidget(widget)
                widget.deleteLater()
        
        # Create a new GameWindow instance.
        # Note: Make sure your GameWindow class is updated to accept 'difficulty' as a parameter.
        game_window = GameWindow(self.stacked_widget, selected_theme, difficulty, user_id)
        self.stacked_widget.addWidget(game_window.ui)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(game_window.ui))
