import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)

        self.last_result = ''
        self.initUI()

    def initUI(self):
        # Crear un widget central y establecer el layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Crear una disposición de pantalla y botón de cambio de color
        top_layout = QHBoxLayout()
        
        self.color_button = QPushButton("Cambiar Color")
        self.color_button.clicked.connect(self.change_color)
        top_layout.addWidget(self.color_button)

        self.display_input = QLineEdit()
        self.display_input.setReadOnly(True)
        self.display_input.setAlignment(Qt.AlignRight)
        self.display_result = QLineEdit()
        self.display_result.setReadOnly(True)
        self.display_result.setAlignment(Qt.AlignRight)

        top_layout.addWidget(self.display_input)
        top_layout.addWidget(self.display_result)
        main_layout.addLayout(top_layout)

        # Crear los botones de la calculadora
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('ANS', '0', '=', '+'),
            ('C',)
        ]

        grid_layout = QVBoxLayout()
        for row in buttons:
            row_layout = QHBoxLayout()
            for btn_text in row:
                button = QPushButton(btn_text)
                button.clicked.connect(self.buttonClicked)
                row_layout.addWidget(button)
            grid_layout.addLayout(row_layout)

        main_layout.addLayout(grid_layout)

        # Conectar el evento del teclado
        self.setFocusPolicy(Qt.StrongFocus)

        # Configurar el color de fondo
        self.set_background_color('#f0f0f0')

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display_input.clear()
            self.display_result.clear()
        elif text == 'ANS':
            self.display_input.setText(self.last_result)
        elif text == '=':
            try:
                expression = self.display_input.text()
                result = str(eval(expression))
                self.display_result.setText(result)
                self.last_result = result
            except Exception as e:
                self.display_result.setText('SYNTAX ERROR')
        else:
            current_text = self.display_input.text()
            new_text = current_text + text
            self.display_input.setText(new_text)

    def keyPressEvent(self, event):
        key = event.key()
        if key in [Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9]:
            self.display_input.setText(self.display_input.text() + event.text())
        elif key in [Qt.Key_Plus, Qt.Key_Minus, Qt.Key_Asterisk, Qt.Key_Slash]:
            self.display_input.setText(self.display_input.text() + event.text())
        elif key == Qt.Key_Enter or key == Qt.Key_Return:
            try:
                expression = self.display_input.text()
                result = str(eval(expression))
                self.display_result.setText(result)
                self.last_result = result
            except Exception as e:
                self.display_result.setText('SYNTAX ERROR')
        elif key == Qt.Key_Backspace:
            current_text = self.display_input.text()
            self.display_input.setText(current_text[:-1])
        elif key == Qt.Key_C:
            self.display_input.clear()
            self.display_result.clear()

    def set_background_color(self, color_hex):
        palette = QPalette()
        color = QColor(color_hex)
        palette.setColor(QPalette.Background, color)
        self.setPalette(palette)
        self.display_input.setStyleSheet(f"background-color: {color_hex};")
        self.display_result.setStyleSheet(f"background-color: {color_hex};")

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.set_background_color(color.name())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
