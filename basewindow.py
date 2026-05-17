from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
import sys

class BaseWindow(QWidget):
    def __init__(self, header: str, size_x=400, size_y=300) -> None:
        super().__init__()
        self.setWindowTitle(header)
        self.setWindowIcon(QIcon("baseicon.png"))
        self.setFixedSize(size_x, size_y)

        with open('style.qss', 'r') as style:
            self.setStyleSheet(style.read())

class Drawer:
    def __init__(self) -> None:
        self.widget = QWidget()
        self.widget.setObjectName("drawer-wrapper")
        self.drawer_layout = QVBoxLayout()
        self.button_size = 50
        self.widget.setMaximumWidth(self.button_size * 4)
        self.widget.setMinimumWidth(self.button_size)
        self.object_widgets = None
        self.animation = None
        self.is_moving = False

    def init_layout(self, *widgets) -> None:
        self.object_widgets = widgets

        self.drawer_layout.setContentsMargins(0, 0, 0, 0)
        self.drawer_layout.setSpacing(0)

        self.toggle_button = QPushButton("☰")
        self.toggle_button.setFixedSize(self.button_size, self.button_size)
        self.toggle_button.setObjectName("toggle-drawer-button")
        self.toggle_button.clicked.connect(self.toggle_drawer)

        self.drawer_layout.addWidget(self.toggle_button, alignment=Qt.AlignCenter)
        self.drawer_layout.setAlignment(Qt.AlignTop)

        for widget in self.object_widgets:
            button = widget.widget
            button.setFixedHeight(self.button_size)
            self.drawer_layout.addWidget(button, Qt.AlignTop)

        self.widget.setLayout(self.drawer_layout)

    def toggle_drawer(self) -> None:
        if self.is_moving:
            return
        def on_animation_finished():
            self.is_moving = False

        self.widget.animation = QPropertyAnimation(self.widget, b"maximumWidth")
        self.widget.animation.setDuration(200)
        self.widget.animation.finished.connect(on_animation_finished)

        self.is_moving = True
        if self.widget.width() == self.button_size:
            self.widget.animation.setStartValue(self.button_size)
            self.widget.animation.setEndValue(self.button_size * 4)
            self.toggle_button.setText("❌")
            for widget in self.object_widgets:
                widget.widget.setText(widget.open_icon)

        else:
            self.widget.animation.setStartValue(self.button_size * 4)
            self.widget.animation.setEndValue(self.button_size)
            self.toggle_button.setText("☰")
            for widget in self.object_widgets:
                widget.widget.setText(widget.close_icon)

        self.widget.animation.start()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BaseWindow("Base window")
    window.show()
    sys.exit(app.exec_())