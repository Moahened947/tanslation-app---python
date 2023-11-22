import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QComboBox, QLabel
from libretranslatepy import LibreTranslateAPI

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Header
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("Libre Translator"))
        main_layout.addLayout(header_layout)

        # Language selection
        lang_layout = QHBoxLayout()
        self.source_lang_combo = QComboBox()
        self.source_lang_combo.addItems(["en", "es", "de", "fr"])
        lang_layout.addWidget(QLabel("From:"))
        lang_layout.addWidget(self.source_lang_combo)

        self.target_lang_combo = QComboBox()
        self.target_lang_combo.addItems(["en", "es", "de", "fr"])
        lang_layout.addWidget(QLabel("To:"))
        lang_layout.addWidget(self.target_lang_combo)

        self.swap_button = QPushButton("Swap")
        self.swap_button.clicked.connect(self.swap_languages)
        lang_layout.addWidget(self.swap_button)
        main_layout.addLayout(lang_layout)

        # Text edit fields
        self.text_edit = QTextEdit()
        main_layout.addWidget(QLabel("Text:"))
        main_layout.addWidget(self.text_edit)

        self.translated_text_edit = QTextEdit()
        self.translated_text_edit.setReadOnly(True)
        main_layout.addWidget(QLabel("Translation:"))
        main_layout.addWidget(self.translated_text_edit)

        # Translate button
        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate_text)
        main_layout.addWidget(self.translate_button)

        self.setLayout(main_layout)

    def swap_languages(self):
        source_lang = self.source_lang_combo.currentText()
        target_lang = self.target_lang_combo.currentText()

        self.source_lang_combo.setCurrentText(target_lang)
        self.target_lang_combo.setCurrentText(source_lang)

    def translate_text(self):
        source_lang = self.source_lang_combo.currentText()
        target_lang = self.target_lang_combo.currentText()
        text_to_translate = self.text_edit.toPlainText()

        lt = LibreTranslateAPI("LibreTranslate is awesome!", "en", "es")
        translated_text = lt.translate(text_to_translate, source_lang, target_lang)
        self.translated_text_edit.setPlainText(translated_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TranslatorApp()
    ex.show()
    sys.exit(app.exec_())
