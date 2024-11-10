import sys
from PyQt5.QtWidgets import QApplication, QWidget
from frontend.draggable_widget import DraggableWidget


def run_desktop_app():
    app = QApplication(sys.argv)

    # Initialize and show the draggable widget
    widget = DraggableWidget()
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run_desktop_app()
