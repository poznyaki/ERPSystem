import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication
from  basewindow import BaseWindow

class Jobs(BaseWindow):
    def __init__(self):
        super(Jobs, self).__init__("JobsWindow")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Jobs"))
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Jobs()
    window.show()
    sys.exit(app.exec_())