import sys
from PyQt5.QtWidgets import (QVBoxLayout,
                             QLabel,
                             QApplication,
                             QHBoxLayout,
                             QPushButton,
                             QTableWidget,
                             QSizePolicy,
                             QWidget,
                             QHeaderView)
from  basewindow import BaseWindow

class Jobs(BaseWindow):
    def __init__(self):
        super(Jobs, self).__init__("JobsWindow")
        layout = QVBoxLayout(self)
        self.setMinimumSize(0, 0)
        self.header_layout = QHBoxLayout()
        self.content_layout = QVBoxLayout()

        self.init_header()
        self.show_table()

        layout.addLayout(self.header_layout)
        layout.addLayout(self.content_layout)
        self.setLayout(layout)

    def init_header(self):
        self.add_job_button = QPushButton("Add Job")
        self.add_job_button.setObjectName("jobs-button")
        self.add_job_button.clicked.connect(self.add_job)
        self.header_layout.addWidget(self.add_job_button)


        self.delete_job_button = QPushButton("Delete Job")
        self.delete_job_button.setObjectName("jobs-button")
        self.delete_job_button.clicked.connect(self.delete_job)
        self.header_layout.addWidget(self.delete_job_button)

        self.edit_job_button = QPushButton("Edit Job")
        self.edit_job_button.setObjectName("jobs-button")
        self.edit_job_button.clicked.connect(self.edit_job)
        self.header_layout.addWidget(self.edit_job_button)


    def show_table(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setMinimumSize(800,400)
        self.table.setSizePolicy(QWidget.QSizePolicy.Expanding, QWidget.QSizePolicy.Expanding)
        self.table.horizontalHeader().setSectionResizeMode(QWidget.QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(["Name", "Price", "Description", "Time", "Category"])


    def add_job(self):
        ...

    def delete_job(self):
        ...

    def edit_job(self):
        ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Jobs()
    window.show()
    sys.exit(app.exec_())