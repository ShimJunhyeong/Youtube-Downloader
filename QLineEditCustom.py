from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class QLineEditCustom(QLineEdit):
    clicked = Signal()

    def mousePressEvent(self, ev):
        self.clicked.emit()
