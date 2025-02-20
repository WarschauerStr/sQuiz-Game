import sys
from PySide2.QtWidgets import QApplication, QStackedWidget
from windows.login_register_window import LoginRegisterWindow
from windows.register_window import RegisterWindow
from windows.logged_options_window import LoggedOptionsWindow
from windows.game_window import GameWindow

class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.stacked_widget = QStackedWidget()
        self.current_user_id = None  # Store user_id after login

        # Initialize windows with the correct arguments
        self.login_register_window = LoginRegisterWindow(self.stacked_widget, self)
        self.register_window = RegisterWindow(self.stacked_widget)
        self.logged_options_window = LoggedOptionsWindow(self.stacked_widget, self)  # Corrected

        # Add windows to stacked widget
        self.stacked_widget.addWidget(self.login_register_window.ui)  # Index 0
        self.stacked_widget.addWidget(self.register_window.ui)  # Index 1
        self.stacked_widget.addWidget(self.logged_options_window.ui)  # Index 2

        # Set initial window
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.setWindowTitle("sQuiz Game")
        self.stacked_widget.show()
        sys.exit(self.app.exec_())

    def start_game(self, theme):
        """Start the game with the selected quiz theme and pass the correct user_id."""
        if self.current_user_id is None:
            print("Error: User is not logged in.")
            return

        self.game_window = GameWindow(self.stacked_widget, theme, self.current_user_id)
        self.stacked_widget.addWidget(self.game_window.ui)  # Index 3
        self.stacked_widget.setCurrentIndex(3)  # Move to game_window

if __name__ == "__main__":
    main_app = MainApp()
