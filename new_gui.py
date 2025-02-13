import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QStackedWidget, QFrame, QPlainTextEdit
from PySide2.QtCore import QRect, Qt
from user import register_user, login_user  # Import the necessary functions


# RegisterWindow
class RegisterWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle('Register')
        self.setGeometry(100, 100, 350, 360)

        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(20, 10, 321, 341))
        self.frame.setStyleSheet("background-color:rgb(222, 221, 218);"
                                 "border: 3px solid rgb(0, 0, 0);"
                                 "border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        # Fullname input
        self.fullname_input = QLineEdit(self.frame)
        self.fullname_input.setGeometry(QRect(10, 50, 301, 41))
        self.fullname_input.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.fullname_input.setPlaceholderText('Fullname (First Last)')

        # Email input
        self.email_input = QLineEdit(self.frame)
        self.email_input.setGeometry(QRect(10, 100, 301, 41))
        self.email_input.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.email_input.setPlaceholderText('Email')

        # Password input
        self.password_input = QLineEdit(self.frame)
        self.password_input.setGeometry(QRect(10, 150, 301, 41))
        self.password_input.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.password_input.setPlaceholderText('Password')

        # Username input
        self.username_input = QLineEdit(self.frame)
        self.username_input.setGeometry(QRect(10, 200, 301, 41))
        self.username_input.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.username_input.setPlaceholderText('Username')

        # Register button
        self.register_button = QPushButton('Register', self.frame)
        self.register_button.setGeometry(QRect(110, 270, 89, 25))
        self.register_button.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.register_button.clicked.connect(self.on_register_click)

        # Switch to Login button
        self.switch_to_login_button = QPushButton('Already have an account? Login', self.frame)
        self.switch_to_login_button.setGeometry(QRect(20, 300, 271, 25))
        self.switch_to_login_button.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.switch_to_login_button.clicked.connect(self.switch_to_login)

    def on_register_click(self):
        # Get values from the input fields
        fullname = self.fullname_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        username = self.username_input.text().strip()

        # Call register_user function from user.py with the gathered input data
        register_user(fullname, email, password, username)

        QMessageBox.information(self, "Success", "✅ Registration successful!")

    def switch_to_login(self):
        self.stacked_widget.setCurrentIndex(0)  # Switch to login window


# LoginWindow
class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 350, 300)

        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(10, 9, 311, 281))
        self.frame.setStyleSheet("background-color:rgb(222, 221, 218);"
                                 "border: 3px solid rgb(0, 0, 0);"
                                 "border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        # Username label and input
        self.username_label = QLabel("Username:", self.frame)
        self.username_label.setGeometry(QRect(10, 20, 91, 21))
        self.username_label.setStyleSheet("background-color: rgb(143, 240, 164);"
                                          "border: 3px solid rgb(0, 0, 0);"
                                          "border-radius: 10px;")
        self.username_input = QPlainTextEdit(self.frame)
        self.username_input.setGeometry(QRect(10, 50, 291, 41))
        self.username_input.setStyleSheet("background-color: rgb(246, 245, 244);")

        # Password label and input
        self.password_label = QLabel("Password:", self.frame)
        self.password_label.setGeometry(QRect(10, 120, 91, 21))
        self.password_label.setStyleSheet("background-color: rgb(143, 240, 164);"
                                          "border: 3px solid rgb(0, 0, 0);"
                                          "border-radius: 10px;")
        self.password_input = QPlainTextEdit(self.frame)
        self.password_input.setGeometry(QRect(10, 150, 291, 41))
        self.password_input.setStyleSheet("background-color: rgb(246, 245, 244);")

        # Login button
        self.login_button = QPushButton('Login', self.frame)
        self.login_button.setGeometry(QRect(110, 210, 89, 25))
        self.login_button.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.login_button.clicked.connect(self.handle_login)

        # Switch to Register button
        self.switch_to_register_button = QPushButton('Don\'t have an account? Register', self.frame)
        self.switch_to_register_button.setGeometry(QRect(20, 240, 271, 25))
        self.switch_to_register_button.setStyleSheet("background-color: rgb(98, 160, 234);")
        self.switch_to_register_button.clicked.connect(self.switch_to_register)

    def handle_login(self):
        username = self.username_input.toPlainText().strip()
        password = self.password_input.toPlainText().strip()

        user = login_user(username, password)

        if user:
            QMessageBox.information(self, "Success", f"Welcome, {user[2]}!")
            self.stacked_widget.setCurrentIndex(2)  # Switch to dashboard window
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def switch_to_register(self):
        self.stacked_widget.setCurrentIndex(1)  # Switch to register window


# DashboardWindow
class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 350, 250)

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
    stacked_widget.setGeometry(100, 100, 350, 300)

    stacked_widget.show()

    sys.exit(app.exec_())
