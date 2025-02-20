from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from windows.game_window import GameWindow
from quiz import get_available_themes  # Import function to fetch themes

class LoggedOptionsWindow(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app  # Store main app reference
        loader = QUiLoader()
        self.ui = loader.load("ui/logged_options_window.ui")

        # Populate available quiz themes
        self.populate_quiz_selection()

        # Connect buttons
        self.ui.start_quiz_button.clicked.connect(self.start_selected_quiz)
        self.ui.log_out_button.clicked.connect(self.go_to_login)

    def populate_quiz_selection(self):
        """Retrieve quiz themes from the database and populate the combo box."""
        themes = get_available_themes()
        self.ui.select_quiz_comboBox.clear()  # Clear previous entries
        if themes:
            self.ui.select_quiz_comboBox.addItems(themes)  # Add themes
        else:
            self.ui.select_quiz_comboBox.addItem("No quizzes available")

    def start_selected_quiz(self):
        """Start a new quiz with the selected theme and reset the game state."""
        selected_theme = self.ui.select_quiz_comboBox.currentText()
        if not selected_theme or selected_theme == "No quizzes available":
            QMessageBox.warning(self, "Warning", "Please select a valid quiz theme!")
            return

        user_id = self.main_app.current_user_id
        if user_id is None:
            QMessageBox.critical(self, "Error", "No logged-in user found.")
            return

        # Remove old GameWindow instance to prevent frozen buttons & incorrect quizzes
        for i in range(self.stacked_widget.count()):
            widget = self.stacked_widget.widget(i)
            if isinstance(widget, GameWindow):
                self.stacked_widget.removeWidget(widget)
                widget.deleteLater()  # Clear from memory

        # Create a fresh GameWindow instance
        game_window = GameWindow(self.stacked_widget, selected_theme, user_id)
        self.stacked_widget.addWidget(game_window.ui)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(game_window.ui))  # Move to game window


    # def start_selected_quiz(self):
    #     """Start a quiz with the selected theme and correct user_id."""
    #     selected_theme = self.ui.select_quiz_comboBox.currentText()
    #     if not selected_theme or selected_theme == "No quizzes available":
    #         QMessageBox.warning(self, "Warning", "Please select a valid quiz theme!")
    #         return

    #     # Get the logged-in user ID
    #     user_id = self.main_app.current_user_id
    #     if user_id is None:
    #         QMessageBox.critical(self, "Error", "No logged-in user found.")
    #         return

    #     # Create GameWindow with user_id and selected theme
    #     game_window = GameWindow(self.stacked_widget, selected_theme, user_id)
    #     self.stacked_widget.addWidget(game_window.ui)
    #     self.stacked_widget.setCurrentIndex(3)  # Move to game_window

    def go_to_login(self):
        self.stacked_widget.setCurrentIndex(0)  # Move back to login_register_window
