import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QStackedWidget

from user import register_user, login_user  # Import the necessary functions


# RegisterWindow
class RegisterWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle('Register')
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        # Fullname input
        self.fullname_input = QLineEdit(self)
        self.fullname_input.setPlaceholderText('Fullname (First Last)')
        self.layout.addWidget(self.fullname_input)

        # Email input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText('Email')
        self.layout.addWidget(self.email_input)

        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        # Username input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText('Username')
        self.layout.addWidget(self.username_input)

        # Register button
        self.register_button = QPushButton('Register', self)
        self.register_button.clicked.connect(self.on_register_click)
        self.layout.addWidget(self.register_button)

        # Switch to Login button
        self.switch_to_login_button = QPushButton('Already have an account? Login', self)
        self.switch_to_login_button.clicked.connect(self.switch_to_login)
        self.layout.addWidget(self.switch_to_login_button)

        # Status label (added)
        self.status_label = QLabel('', self)  # This is where the status will be displayed
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def on_register_click(self):
        # Get values from the input fields
        fullname = self.fullname_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        username = self.username_input.text().strip()

        # Call register_user function from user.py with the gathered input data
        register_user(fullname, email, password, username)

        self.status_label.setText("✅ Registration successful!")  # Display success message

    def switch_to_login(self):
        self.stacked_widget.setCurrentIndex(0)  # Switch to login window


# LoginWindow
class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.handle_login)

        # Switch to Register button
        self.switch_to_register_button = QPushButton('Don\'t have an account? Register', self)
        self.switch_to_register_button.clicked.connect(self.switch_to_register)
        self.layout.addWidget(self.switch_to_register_button)

        self.setLayout(self.layout)

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        user = login_user(username, password)

        if user:
            QMessageBox.information(self, "Success", f"Welcome, {user[2]}!")
            # Show the dashboard after login is successful
            self.stacked_widget.setCurrentIndex(2)  # Switch to the dashboard window
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def switch_to_register(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to register window


# DashboardWindow
class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        # Start Quiz button
        self.start_quiz_button = QPushButton("Start Quiz")
        self.layout.addWidget(self.start_quiz_button)

        # View Leaderboard button
        self.view_leaderboard_button = QPushButton("View Leaderboard")
        self.layout.addWidget(self.view_leaderboard_button)

        # Create a Quiz button
        self.create_quiz_button = QPushButton("Create a Quiz")
        self.layout.addWidget(self.create_quiz_button)

        # Log Out button
        self.logout_button = QPushButton("Log Out")
        self.layout.addWidget(self.logout_button)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the stacked widget
    stacked_widget = QStackedWidget()

    # Create the windows and add them to the stacked widget
    login_window = LoginWindow(stacked_widget)
    register_window = RegisterWindow(stacked_widget)
    dashboard_window = DashboardWindow()

    stacked_widget.addWidget(login_window)  # Login window at index 0
    stacked_widget.addWidget(register_window)  # Register window at index 1
    stacked_widget.addWidget(dashboard_window)  # Dashboard window at index 2

    # Set the initial window to be the login window
    stacked_widget.setCurrentIndex(0)

    stacked_widget.setWindowTitle("sQuiz Game Login")
    stacked_widget.setGeometry(100, 100, 300, 250)

    stacked_widget.show()

    sys.exit(app.exec())
