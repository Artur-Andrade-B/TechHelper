# frontend/radial_menu.py

from PyQt5.QtWidgets import QMenu, QAction, QApplication
import os

class RadialMenu(QMenu):
    def __init__(self):
        super().__init__()

        # Create actions for the radial menu
        self.menu_action = QAction("Menu", self)
        self.help_action = QAction("Help", self)
        self.desktop_action = QAction("Open Desktop Folder", self)
        self.quit_action = QAction("Quit", self)

        # Add actions to the radial menu
        self.addAction(self.menu_action)
        self.addAction(self.help_action)
        self.addAction(self.desktop_action)
        self.addAction(self.quit_action)

        # Connect actions to their respective functions
        self.quit_action.triggered.connect(self.quit_program)
        self.desktop_action.triggered.connect(self.open_desktop_folder)
        self.help_action.triggered.connect(self.show_help)

    def quit_program(self):
        print("Quitting the application...")
        QApplication.quit()

    def open_desktop_folder(self):
        print("Opening desktop folder...")
        os.startfile(os.path.expanduser("~/Desktop"))  # Works on Windows

    def show_help(self):
        print("Help action triggered")
        # For example, you could open a dialog here
