import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eazy Temperature Converter")
        self.setGeometry(100, 100, 400, 100)
        self.setFixedSize(400, 130)

        self.init_ui()

    def init_ui(self):

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Type the desired temperature in one of the fields", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label)

        input_layout = QGridLayout()
        input_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(input_layout)

        self.label_celsius = QLabel("Celsius", self)
        self.label_celsius.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.label_celsius, 0, 0)

        self.temp_celsius = QLineEdit(self)
        self.temp_celsius.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.temp_celsius, 1, 0)

        self.label_fahrenheit = QLabel("Fahrenheit", self)
        self.label_fahrenheit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.label_fahrenheit, 0, 1)

        self.temp_fahrenheit = QLineEdit(self)
        self.temp_fahrenheit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.temp_fahrenheit, 1, 1)

        self.label_kelvin = QLabel("Kelvin", self)
        self.label_kelvin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.label_kelvin, 0, 2)

        self.temp_kelvin = QLineEdit(self)
        self.temp_kelvin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(self.temp_kelvin, 1, 2)

        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        self.convert_btn = QPushButton("Convert", self)
        self.convert_btn.setFixedWidth(120)
        button_layout.addWidget(self.convert_btn)
        self.convert_btn.clicked.connect(self.handle_button_click)

        self.clear_btn = QPushButton("Clear", self)
        self.clear_btn.setFixedWidth(120)
        button_layout.addWidget(self.clear_btn)
        self.clear_btn.clicked.connect(self.clear_text)
        self.clear_btn.setEnabled(False)

    def handle_button_click(self):
        self.get_input()
        self.convert_clicked()

    def convert_clicked(self):
        self.convert_btn.setEnabled(False)
        self.clear_btn.setEnabled(True)

    def get_input(self):
        if not (any(char.isspace() for char in self.temp_celsius.text()) or self.temp_celsius.text().isalpha() or self.temp_celsius.text() == ""):
            self.celsius_to_fahrenheit_and_kelvin(self.temp_celsius.text())
            self.change_ui_color()
        elif not (any(char.isspace() for char in self.temp_fahrenheit.text()) or self.temp_fahrenheit.text().isalpha() or self.temp_fahrenheit.text() == ""):
            self.fahrenheit_to_celsius_and_kelvin(self.temp_fahrenheit.text())
            self.change_ui_color()
        elif not (any(char.isspace() for char in self.temp_kelvin.text()) or self.temp_kelvin.text().isalpha() or self.temp_kelvin.text() == ""):
            self.kelvin_to_celsius_and_fahrenheit(self.temp_kelvin.text())
            self.change_ui_color()
        else:
            self.show_error_message()

    def show_error_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText("Please insert valid values")
        msg_box.addButton(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def celsius_to_fahrenheit_and_kelvin(self, temp_celsius):
        if temp_celsius.isdigit():
            celsius = int(temp_celsius)
            fahrenheit = celsius * 1.80 + 32.00
            kelvin = celsius + 273.15
            self.temp_fahrenheit.setText(str(fahrenheit))
            self.temp_kelvin.setText(str(kelvin))
        else:
            celsius = float(temp_celsius.replace(",", "."))
            fahrenheit = celsius * 1.80 + 32.00
            kelvin = celsius + 273.15
            self.temp_fahrenheit.setText(str(fahrenheit))
            self.temp_kelvin.setText(str(kelvin))

    def fahrenheit_to_celsius_and_kelvin(self, temp_fahrenheit):
        if temp_fahrenheit.isdigit():
            fahrenheit = int(temp_fahrenheit)
            celsius = (fahrenheit - 32.00) * 5 / 9
            kelvin = celsius + 273.15
            self.temp_celsius.setText(str(celsius))
            self.temp_kelvin.setText(str(kelvin))
        else:
            fahrenheit = float(temp_fahrenheit.replace(",", "."))
            celsius = (fahrenheit - 32.00) * 5 / 9
            kelvin = celsius + 273.15
            self.temp_celsius.setText(str(celsius))
            self.temp_kelvin.setText(str(kelvin))

    def kelvin_to_celsius_and_fahrenheit(self, temp_kelvin):
        if temp_kelvin.isdigit():
            kelvin = int(temp_kelvin)
            celsius = kelvin - 273.15
            fahrenheit = celsius * 1.80 + 32.00
            self.temp_celsius.setText(str(celsius))
            self.temp_fahrenheit.setText(str(fahrenheit))
        else:
            kelvin = float(temp_kelvin.replace(",", "."))
            celsius = kelvin - 273.15
            fahrenheit = celsius * 1.80 + 32.00
            self.temp_celsius.setText(str(celsius))
            self.temp_fahrenheit.setText(str(fahrenheit))

    def change_ui_color(self):
        if int(float(self.temp_fahrenheit.text().replace(",", "."))) >= 91:
            self.setStyleSheet("background-color: red;")
        elif  55 < int(float(self.temp_fahrenheit.text().replace(",", "."))) < 114:
            self.setStyleSheet("background-color: grey;")
        else:
            int(float(self.temp_fahrenheit.text().replace(",", "."))) <= 55
            self.setStyleSheet("background-color: blue;")
            self.label.setStyleSheet("color: white")
            self.label_celsius.setStyleSheet("color: white")
            self.label_fahrenheit.setStyleSheet("color: white")
            self.label_kelvin.setStyleSheet("color: white")
            self.convert_btn.setStyleSheet("color: white")
            self.clear_btn.setStyleSheet("color: white")
            self.temp_celsius.setStyleSheet("color: white")
            self.temp_fahrenheit.setStyleSheet("color: white")
            self.temp_kelvin.setStyleSheet("color: white")

    def clear_text(self):
        self.temp_celsius.clear()
        self.temp_fahrenheit.clear()
        self.temp_kelvin.clear()
        self.convert_btn.setEnabled(True)
        self.clear_btn.setEnabled(False)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
