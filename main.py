import sys
from dataclasses import dataclass
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QVBoxLayout,
                             QHBoxLayout,
                             QStackedWidget)  # Додали QStackedWidget

from basewindow import BaseWindow, Drawer
from warehouse import Warehouse
from jobs import Jobs


class BusinessERP(BaseWindow):
    def __init__(self):
        super().__init__("Business ERP", size_x=600, size_y=400)

        main_layout = QHBoxLayout()
        drawer_layout = QVBoxLayout()

        self.pages_stack = QStackedWidget()

        self.home_window = QWidget()
        home_layout = QVBoxLayout(self.home_window)
        home_layout.addWidget(QLabel("Main block / Home Page"))

        self.warehouse_window = Warehouse()
        self.jobs_window = Jobs()

        self.pages_stack.addWidget(self.home_window)  # Індекс 0
        self.pages_stack.addWidget(self.warehouse_window)  # Індекс 1
        self.pages_stack.addWidget(self.jobs_window)  # Індекс 2

        self.drawer = Drawer()
        self.init_drawer()

        drawer_layout.addWidget(self.drawer.widget)

        main_layout.addLayout(drawer_layout)
        main_layout.addWidget(self.pages_stack)
        self.setLayout(main_layout)

    def init_drawer(self) -> None:
        @dataclass
        class DrawerButton:
            widget: QPushButton
            open_icon: str
            close_icon: str

        home_page_button = QPushButton("🏠 Home")
        home_page_button.setObjectName("drawer-button")
        home_page_button.clicked.connect(lambda: self.show_page(0))  # Показує home_window
        home_page_button_widget = DrawerButton(home_page_button, "🏠 Home", "🏠")

        ware_house_page_button = QPushButton("🏢 Warehouse")
        ware_house_page_button.setObjectName("drawer-button")
        ware_house_page_button.clicked.connect(lambda: self.show_page(1))  # Показує warehouse_window
        ware_house_page_button_widget = DrawerButton(ware_house_page_button, "🏢 Warehouse", "🏢")

        jobs_page_button = QPushButton("📄 Jobs")
        jobs_page_button.setObjectName("drawer-button")
        jobs_page_button.clicked.connect(lambda: self.show_page(2))  # Показує jobs_window
        jobs_page_button_widget = DrawerButton(jobs_page_button, "📄 Jobs", "📄")

        settings_page_button = QPushButton("⚙️ Settings")
        settings_page_button.setObjectName("drawer-button")
        settings_page_button.clicked.connect(lambda: self.show_page(0))
        settings_page_button_widget = DrawerButton(settings_page_button, "⚙️ Settings", "⚙️")

        quit_page_button = QPushButton("🚪 Quit")
        quit_page_button.setObjectName("drawer-button")
        quit_page_button.clicked.connect(QApplication.instance().quit)  # Вихід з програми
        quit_page_button_widget = DrawerButton(quit_page_button, "🚪 Quit", "🚪")

        self.drawer.init_layout(home_page_button_widget,
                                ware_house_page_button_widget,
                                jobs_page_button_widget,
                                settings_page_button_widget,
                                quit_page_button_widget)

    def show_page(self, page_index: int):
        self.pages_stack.setCurrentIndex(page_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BusinessERP()
    window.show()
    sys.exit(app.exec_())