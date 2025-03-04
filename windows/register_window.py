from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from user import register_user
from validators import validate_fullname, validate_email, validate_password


class RegisterWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        loader = QUiLoader()
        self.ui = loader.load("ui/register_window.ui")

        # Connect buttons
        self.ui.register_button.clicked.connect(self.handle_register)
        self.ui.login_button.clicked.connect(self.go_to_login)

    def handle_register(self):
        fullname = self.ui.fullname_lineEdit.text().strip()
        email = self.ui.email_lineEdit.text().strip()
        password = self.ui.password_lineEdit.text().strip()
        username = self.ui.username_lineEdit.text().strip()

        # Validate that all fields are filled
        if not fullname or not email or not password or not username:
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return

        # Validate fullname format
        if not validate_fullname(fullname):
            QMessageBox.warning(self, "Error", "Invalid fullname format. Please use 'First Last'.")
            return

        # Validate email format
        if not validate_email(email):
            QMessageBox.warning(self, "Error", "Invalid email format. Please enter a valid email (e.g., user@example.com).")
            return

        # Validate password format
        if not validate_password(password):
            QMessageBox.warning(self, "Error", "Invalid password. It must be at least 8 characters long, contain at least one uppercase letter and one number.")
            return

        # If all validations pass, register the user
        register_user(fullname, email, password, username)
        QMessageBox.information(self, "Success", "✅ Registration successful!")
        self.stacked_widget.setCurrentIndex(0)

    def go_to_login(self):
        self.stacked_widget.setCurrentIndex(0)
