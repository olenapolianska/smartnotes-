import PyQt5
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget ()
listNotesLbl = QLabel("Список заміток")
textedit = QTextEdit()
listnotes = QListWidget()
listtegLbl = QLabel("Список тегів")
addnote = QPushButton("Створити замітку")
deletenote = QPushButton("Видалити замітку")
savenote = QPushButton("Зберегти замітку")
listteg = QListWidget()
searchonteg = QLineEdit()
addtonote = QPushButton("Додати до замітки")
deletefromnote = QPushButton("Видалити від замітки")
searchnote = QPushButton("Шукати замітки по тегу")

mainline= QHBoxLayout ()
mainline.addWidget(textedit)

line = QVBoxLayout()
line.addWidget(listNotesLbl)
line.addWidget(listnotes)
line.addWidget(addnote)
line.addWidget(deletenote)
line.addWidget(savenote)
line.addWidget(listtegLbl)
line.addWidget(listteg)
line.addWidget(searchonteg)
line.addWidget(addtonote)
line.addWidget(deletefromnote)
line.addWidget(searchnote)


mainline.addLayout(line)
window.setLayout(mainline)
window.show()
app.exec()