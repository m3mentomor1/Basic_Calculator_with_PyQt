import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtGui import QFont


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setFixedSize(345, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setFixedHeight(40)
        self.display.setMaxLength(15)
        font = QFont()
        font.setPointSize(14)
        self.display.setFont(font)  # Set font size of the text field
        self.layout.addWidget(self.display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, button in zip(positions, buttons):
            btn = QPushButton(button)
            btn.clicked.connect(lambda _, text=button: self.display.insert(text))
            btn.setFixedSize(75, 75)
            btn.setStyleSheet("font-weight: bold; font-size: 18px;")
            grid_layout.addWidget(btn, *position)

            if button == '=':
                btn.clicked.connect(self.calculate_result)
            elif button == 'C':
                btn.clicked.connect(self.clear_display)

    def calculate_result(self):
        try:
            expression = self.display.text()
            print("Expression:", expression)
            # Handling '=' at the end of the expression
            if expression.endswith('='):
                expression = expression[:-1]
            result = str(eval(expression))
            print("Result:", result)
            self.display.setText(result)
        except Exception as e:
            print("Error:", e)
            self.display.setText("Error")

    def clear_display(self):
        self.display.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
