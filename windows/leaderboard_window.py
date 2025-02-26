from PySide2.QtWidgets import QWidget
from PySide2.QtUiTools import QUiLoader
from leaderboard import get_top_users


class LeaderboardWindow(QWidget):
    def __init__(self, stacked_widget):
        print("LeaderboardWindow initialized!")
        super().__init__()
        self.stacked_widget = stacked_widget
        loader = QUiLoader()
        self.ui = loader.load("ui/leaderboard_window.ui", self)

        # Load top users when window is opened
        self.display_top_users()

        # Connect button to return to logged_options_window
        self.ui.back_to_main_button.clicked.connect(self.go_to_main_menu)

    def display_top_users(self):
        """Fetch and display the top 3 users in the leaderboard."""
        top_users = get_top_users()

        # Default message if no scores are available
        placeholders = ["No data", "No data", "No data"]

        # Populate labels with usernames and points
        for idx, (username, points) in enumerate(top_users):
            placeholders[idx] = f"{idx + 1}. {username} - {points} points"

        self.ui.top_1_username_label.setText(placeholders[0])
        self.ui.top_2_username_label.setText(placeholders[1])
        self.ui.top_3_username_label.setText(placeholders[2])

    def go_to_main_menu(self):
        """Switch back to the logged options window."""
        self.stacked_widget.setCurrentIndex(2)
