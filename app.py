import htmlTemplate
from sys import argv, exit
from PyQt5.QtWidgets import (QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QWidget,
                             QFileDialog, QProgressBar, QComboBox)
from cambridge_dict import CambridgeDict


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 500, 350, 100)
        self.words = []
        self.init_ui()

    def init_ui(self):
        self.avaible_methods = ["Cambridge - English definitions (Recommend)"]
        label1 = QLabel('File: ')
        self.label_file = QLabel()
        self.line_edit1 = QLineEdit()
        self.button_browse = QPushButton('Select File')
        self.button_start = QPushButton('Start/Save Results')
        self.progress_bar = QProgressBar()
        self.combo_box = QComboBox(self)
        self.combo_box.addItem(self.avaible_methods[0])

        horizontal_box_file = QHBoxLayout()
        horizontal_box_file.addWidget(label1)
        horizontal_box_file.addWidget(self.label_file)

        horizontal_box_buttons = QHBoxLayout()
        horizontal_box_buttons.addWidget(self.button_browse)
        horizontal_box_buttons.addWidget(self.button_start)

        self.vertical_box = QVBoxLayout()
        self.vertical_box.addWidget(self.combo_box)
        self.vertical_box.addLayout(horizontal_box_file)
        self.vertical_box.addWidget(self.progress_bar)
        self.vertical_box.addLayout(horizontal_box_buttons)

        self.setLayout(self.vertical_box)

        self.setWindowTitle('Treya')

        self.button_browse.clicked.connect(self.open_file_dialog)
        self.button_start.clicked.connect(self.button_start_click)
        self.show()

    def button_start_click(self):
        definitions = []
        if self.words == list():
            return
        elif self.combo_box.currentText() == self.avaible_methods[0]:
            Translator = CambridgeDict()
        for word in self.words:
            definitions.append(Translator.define(word))
            self.progress_bar.setValue(int(round(len(definitions) / len(self.words), 2) * 100))
        html = self.html_conv(definitions)
        self.save_file_dialog(html)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                               "Text Files (*.txt);;Python Files (*.py)", options=options)
        if filename:
            with open(filename[0], 'r', encoding="utf8") as f:
                self.words = f.read().split()
                filename = filename[0][filename[0].rfind('/') + 1:]
            self.label_file.setText(filename)
        else:
            self.label_file.setText('Unable to open file')

    def save_file_dialog(self, html):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "output.html",
                                               "HTML (*.html)", options=options)
        if filename:
            with open(filename[0], 'wb') as f:
                html = html.encode('utf8')
                f.write(html)

    def html_conv(self, definitions):
        contents = []
        content = ""
        size = 0
        for word, definition in zip(self.words, definitions):
            content += f"<span title=\"{definition}\">{word} </span>"
            size += len(word) + 1
            if size > 4000:
                contents.append(content)
                content = ""
                size = 0
        contents.append(content)
        html = htmlTemplate.makeHTML(contents)
        return html


if __name__ == "__main__":
    app = QApplication(argv)
    our_window = Window()
    exit(app.exec_())
