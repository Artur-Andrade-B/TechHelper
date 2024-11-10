# frontend/draggable_widget.py

from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from frontend.radial_menu import RadialMenu  # Import the RadialMenu

class DraggableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # Frameless widget, always on top
        self.setGeometry(100, 100, 200, 200)  # Size and position of the widget
        self.setWindowTitle('Floating Widget')

        # Draggable area is the entire widget, so no specific area to handle.
        self._drag_position = None  # Track the drag position

        # Create a button at the bottom of the widget
        self.button = QPushButton("Open Menu", self)
        self.button.setStyleSheet("background-color: darkblue; color: white; font-weight: bold;")
        self.button.setGeometry(50, 150, 100, 40)  # Position it at the bottom

        # Create an instance of RadialMenu
        self.menu = RadialMenu()

        # Connect button click to open the radial menu
        self.button.clicked.connect(self.show_radial_menu)

    def mousePressEvent(self, event):
        """
        When mouse is pressed anywhere on the widget, start dragging.
        """
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """
        Move the widget while dragging.
        """
        if self._drag_position:
            self.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """
        End dragging when mouse button is released.
        """
        self._drag_position = None

    def show_radial_menu(self):
        """
        Show the radial menu when the button is clicked.
        """
        self.menu.exec_(self.button.mapToGlobal(self.button.rect().center()))
