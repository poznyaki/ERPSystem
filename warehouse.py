import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication
from  basewindow import BaseWindow

class Warehouse(BaseWindow):
    def __init__(self):
        super(Warehouse, self).__init__("WarehouseWindow")
        layout = QVBoxLayout(self)
        self.setMinimumSize(0, 0)
        layout.addWidget(QLabel("Warehouse"))
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Warehouse()
    window.show()
    sys.exit(app.exec_())