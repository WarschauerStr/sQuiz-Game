from PySide2.QtWidgets import QWidget, QMessageBox, QLineEdit
from PySide2.QtUiTools import QUiLoader
from user import login_user

class LoginRegisterWindow(QWidget):
    def __init__(self, stacked_widget, main_app):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.main_app = main_app  # Reference to main app to store user_id
        loader = QUiLoader()
        self.ui = loader.load("ui/login_register_window.ui")

        # If you haven't set Echo mode in Qt Designer, do it in code:
        # self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)

        # Connect buttons
        self.ui.login_button.clicked.connect(self.handle_login)
        self.ui.register_button.clicked.connect(self.go_to_register)

    def handle_login(self):
        # Retrieve text from the line edits
        username = self.ui.username_lineEdit.text().strip()
        password = self.ui.password_lineEdit.text().strip()

        user = login_user(username, password)
        if user:
            user_id = user[0]  # Extract user_id from database result
            self.main_app.current_user_id = user_id  # Store user_id in main app
            QMessageBox.information(self, "Success", f"Welcome, {user[2]}!")
            self.stacked_widget.setCurrentIndex(2)  # Move to logged_options_window
        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def go_to_register(self):
        self.stacked_widget.setCurrentIndex(1)  # Move to register_window
