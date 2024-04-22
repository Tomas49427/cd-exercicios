import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QScrollArea
from PyQt6.QtGui import QPixmap, QPainter, QPen
from PyQt6.QtCore import QRect, QPoint, Qt
from encrypter import encrypt_full, encrypt_partial
from decrypter import decrypt_full, decrypt_partial


# Custom QLabel subclass for drawing rectangles on images
class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.start = QPoint()
        self.end = QPoint()
        self.drawing = False

    # Handles mouse press events to start drawing
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start = event.pos()
            self.drawing = True

    # Handles mouse move events to update the end point of the rectangle
    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end = event.pos()
            self.update()

    # Handles mouse release events to stop drawing
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    # Overrides paintEvent to draw a rectangle on the image
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.drawing:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.GlobalColor.red, 2))
            painter.drawRect(QRect(self.start, self.end).normalized())


# Main application window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.decryptButton = None
        self.encryptButton = None
        self.imageLabel = None
        self.fileLabel = None
        self.clearLabel = None
        self.fileOpenButton = None
        self.key_file = ""
        self.initUI()

    # Initializes the UI components
    def initUI(self):
        self.setWindowTitle('File Explorer and Encrypt')
        self.setGeometry(100, 100, 400, 300)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        layout = QVBoxLayout()

        self.fileOpenButton = QPushButton('Open File')
        self.fileOpenButton.clicked.connect(self.openFileNameDialog)
        content_layout.addWidget(self.fileOpenButton)

        self.clearLabel = QPushButton('Clear Selection')
        self.clearLabel.clicked.connect(self.clearSelection)
        content_layout.addWidget(self.clearLabel)

        self.fileLabel = QLabel('No file selected')
        content_layout.addWidget(self.fileLabel)

        self.imageLabel = ImageLabel(self)
        content_layout.addWidget(self.imageLabel)

        self.encryptButton = QPushButton('Encrypt')
        self.encryptButton.clicked.connect(self.encryptFile)
        self.encryptButton.setDisabled(True)
        content_layout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton('Decrypt')
        self.decryptButton.clicked.connect(self.decryptFile)
        self.decryptButton.setDisabled(True)
        content_layout.addWidget(self.decryptButton)

        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        self.setLayout(layout)

    # Opens a file dialog to select an image file
    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose File", "",
                                                  "Images (*.png *.xpm *.jpg *.tif);;All Files (*)")
        if fileName:
            self.fileLabel.setText(fileName)
            pixmap = QPixmap(fileName)
            self.imageLabel.setPixmap(pixmap)
        self.encryptButton.setDisabled(False)

    # Encrypts the selected image file
    def encryptFile(self):
        file_name = self.fileLabel.text()
        (encrypted_file, key) = encrypt_full(
            file_name) if self.imageLabel.start.isNull() and self.imageLabel.end.isNull() \
            else encrypt_partial(file_name, self.imageLabel.start.y(), self.imageLabel.end.y(),
                                 self.imageLabel.start.x(), self.imageLabel.end.x())
        pixmap = QPixmap(encrypted_file)
        self.imageLabel.setPixmap(pixmap)
        self.fileLabel.setText(encrypted_file)
        self.key_file = key
        self.decryptButton.setDisabled(False)

    # Decrypts the selected image file
    def decryptFile(self):
        file_name = self.fileLabel.text()
        decrypted_file = decrypt_full(file_name,
                                      self.key_file) if self.imageLabel.start.isNull() and self.imageLabel.end.isNull() \
            else decrypt_partial(file_name, self.key_file, self.imageLabel.start.y(), self.imageLabel.end.y(),
                                 self.imageLabel.start.x(), self.imageLabel.end.x())
        pixmap = QPixmap(decrypted_file)
        self.imageLabel.setPixmap(pixmap)
        self.fileLabel.setText(decrypted_file)
        self.key_file = ""

    # Clears the selection rectangle on the image
    def clearSelection(self):
        pixmap = QPixmap(self.fileLabel.text())
        self.imageLabel.end = QPoint()
        self.imageLabel.start = QPoint()
        self.imageLabel.setPixmap(pixmap)


# Entry point for the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
