from dataclasses import dataclass
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLineEdit,
                             QLabel,
                             QVBoxLayout,
                             QHBoxLayout,)
from basewindow import BaseWindow, Drawer
from warehouse import Warehouse
from jobs import Jobs
import sys

class BusinessERP(BaseWindow):
    def __init__(self):
        super().__init__("Business ERP")
        main_layout = QHBoxLayout()
        drawer_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        content_layout.addWidget(QLabel("Main block"))
        self.drawer = Drawer()
        self.init_drawer()
        self.warehouse_window = Warehouse()
        self.jobs_window = Jobs()

        drawer_layout.addWidget(self.drawer.widget)

        main_layout.addLayout(drawer_layout)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def init_drawer(self) -> None:
        @dataclass
        class DrawerButton:
            widget: QPushButton
            open_icon: str
            close_icon: str

        home_page_button = QPushButton("🏠 Home")
        home_page_button.setObjectName("drawer-button")
        home_page_button_widget = DrawerButton(home_page_button, "🏠 Home", "🏠")

        ware_house_page_button = QPushButton("🏢 Warehouse")
        ware_house_page_button.setObjectName("drawer-button")
        ware_house_page_button.clicked.connect(lambda: self.open_home_page(self.warehouse_window))
        ware_house_page_button_widget = DrawerButton(ware_house_page_button, "🏢 Warehouse", "🏢")

        jobs_page_button = QPushButton("📄 Jobs")
        jobs_page_button.setObjectName("drawer-button")
        jobs_page_button.clicked.connect(lambda: self.open_home_page(self.jobs_window))
        jobs_page_button_widget = DrawerButton(jobs_page_button, "📄 Jobs", "📄")

        settings_page_button = QPushButton("⚙️ Settings")
        settings_page_button.setObjectName("drawer-button")
        settings_page_button_widget = DrawerButton(settings_page_button, "⚙️ Settings", "⚙️")

        quit_page_button = QPushButton("🚪 Quit")
        quit_page_button.setObjectName("drawer-button")
        quit_page_button_widget = DrawerButton(quit_page_button, "🚪 Quit", "🚪")

        self.drawer.init_layout(home_page_button_widget,
                                ware_house_page_button_widget,
                                jobs_page_button_widget,
                                settings_page_button_widget,
                                quit_page_button_widget)

    def show_window(self, widget_window):
        if self.current_content_widget is not None:
            self.content_layout.removeWidget(self.current_content_widget)
            self.current_content_widget.setParent(None)

        self.current_layout.addWidget(self.current_content_widget)
        self.current_content_widget = widget_window



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BusinessERP()
    window.show()
    sys.exit(app.exec_())