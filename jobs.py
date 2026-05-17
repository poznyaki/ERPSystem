import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QHBoxLayout, QPushButton
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
        self.header_layout.addWidget(self.add_job_button)

        self.delete_job_button = QPushButton("Delete Job")
        self.delete_job_button.setObjectName("jobs-button")
        self.header_layout.addWidget(self.delete_job_button)
#game pin: 184 3001
        self.edit_job_button = QPushButton("Edit Job")
        self.edit_job_button.setObjectName("jobs-button")
        self.header_layout.addWidget(self.edit_job_button)


    def show_table(self):
        ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Jobs()
    window.show()
    sys.exit(app.exec_())