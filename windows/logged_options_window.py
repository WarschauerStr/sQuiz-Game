from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from windows.create_quiz_window import CreateQuizWindow  # Import the Create Quiz window

class LoggedOptionsWindow(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app  # Store main app reference
        loader = QUiLoader()
        self.ui = loader.load("ui/logged_options_window.ui")

        # Connect buttons
        self.ui.start_quiz_button.clicked.connect(self.open_select_quiz_window)
        self.ui.create_quiz_button.clicked.connect(self.open_create_quiz_window)
        self.ui.view_leaderboard_button.clicked.connect(self.open_leaderboard)
        self.ui.log_out_button.clicked.connect(self.go_to_login)

    def open_select_quiz_window(self):
        """Switch to the Select Quiz window."""
        # Assuming the select_quiz_window is added at index 5.
        self.stacked_widget.setCurrentIndex(5)

    def open_create_quiz_window(self):
        """Switch to the Create Quiz window."""
        self.stacked_widget.setCurrentIndex(4)

    def open_leaderboard(self):
        """Switch to the leaderboard window."""
        self.stacked_widget.setCurrentIndex(3)

    def go_to_login(self):
        """Return to the login screen."""
        self.stacked_widget.setCurrentIndex(0)
