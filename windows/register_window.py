from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtUiTools import QUiLoader
from user import register_user


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

        register_user(fullname, email, password, username)
        QMessageBox.information(self, "Success", "✅ Registration successful!")
        self.stacked_widget.setCurrentIndex(0)  # Move back to login_register_window

    def go_to_login(self):
        self.stacked_widget.setCurrentIndex(0)  # Move to login_register_window
