import sys
from PySide2.QtWidgets import QApplication, QStackedWidget, QDesktopWidget
from PySide2.QtCore import Qt
from windows.login_register_window import LoginRegisterWindow
from windows.register_window import RegisterWindow
from windows.logged_options_window import LoggedOptionsWindow
from windows.game_window import GameWindow
from windows.leaderboard_window import LeaderboardWindow
from windows.create_quiz_window import CreateQuizWindow
from windows.select_quiz_window import SelectQuizWindow

# Ensure OpenGL context is set correctly before QApplication starts
QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.stacked_widget = QStackedWidget()
        self.current_user_id = None  # Store user_id after login

        # Initialize windows
        self.login_register_window = LoginRegisterWindow(
            self.stacked_widget, self)
        self.register_window = RegisterWindow(self.stacked_widget)
        self.logged_options_window = LoggedOptionsWindow(
            self.stacked_widget, self)
        self.leaderboard_window = LeaderboardWindow(self.stacked_widget)
        self.create_quiz_window = CreateQuizWindow(self.stacked_widget)
        self.select_quiz_window = SelectQuizWindow(self.stacked_widget, self)

        # Add windows to stacked widget
        # Index 0
        self.stacked_widget.addWidget(self.login_register_window.ui)
        # Index 1
        self.stacked_widget.addWidget(self.register_window.ui)
        # Index 2
        self.stacked_widget.addWidget(self.logged_options_window.ui)
        # Index 3
        self.stacked_widget.addWidget(self.leaderboard_window.ui)
        # Index 4
        self.stacked_widget.addWidget(self.create_quiz_window.ui)
        # Index 5
        self.stacked_widget.addWidget(self.select_quiz_window.ui)

        # Adjust window size dynamically
        self.adjust_window_size()

        # Set initial window
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.setWindowTitle("sQuiz Game")
        self.stacked_widget.show()
        sys.exit(self.app.exec_())

    def adjust_window_size(self):
        width = 640
        height = 480
        screen = QDesktopWidget().screenGeometry()
        self.stacked_widget.setGeometry(
            (screen.width() - width) // 2,  # Center horizontally
            (screen.height() - height) // 2,  # Center vertically
            width,
            height
        )

    def start_game(self, theme):
        if self.current_user_id is None:
            print("Error: User is not logged in.")
            return

        self.game_window = GameWindow(
            self.stacked_widget, theme, self.current_user_id)
        self.stacked_widget.addWidget(
            self.game_window.ui)
        self.stacked_widget.setCurrentIndex(
            self.stacked_widget.indexOf(self.game_window.ui))


if __name__ == "__main__":
    main_app = MainApp()
