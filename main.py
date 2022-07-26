# IMPORTANDO MODULOS
import sys
import os
from qt_core import *
from gui.window.main_window.ui_main_window import UI_MainWindow

# MAIN WINDOW


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primeiro app em Py")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # botao toggle
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # botao home
        self.ui.btn_1.clicked.connect(self.show_page_1)

        # botao widgets
        self.ui.btn_2.clicked.connect(self.show_page_2)

        # botao settings
        self.ui.btn_settings.clicked.connect(self.show_page_3)

        # exibir aplicacao
        self.show()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page3)
        self.ui.btn_settings.set_active(True)

    def toggle_button(self):
        # obter tanho do menu
        menu_width = self.ui.left_menu.width()

    # verificar o tamanho
        width = 50
        if menu_width == 50:
            width = 240

    # animacao do menu
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
