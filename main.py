import PyQt5
from PyQt5.QtWidgets import *

import json

try:
    with open("note_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    notes = {}

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

def add_note():
    note_name, ok = QInputDialog.getText(window,"Додати замітку", "Назва замітки:")
    if ok and note_name != "":
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
        listnotes.clear()
        textedit.clear()
        listnotes.addItems(notes)
        with open("note_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

def save_note():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        notes[key]["текст"] = textedit.toPlainText()
        with open("note_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Замітка для збереження не вибрана!")

def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
    key = listnotes.selectedItems()[0].text()
    print(key)
    textedit.setText(notes[key]["текст"])
    listteg.clear()
    listteg.addItems(notes[key]["теги"])

def del_note():
    if listnotes.selectedItems():
        key = listnotes.selectedItems()[0].text()
        notes.pop(key)
        listnotes.clear()
        listteg.clear()
        textedit.clear()
        listnotes.addItems(notes)
        with open("note_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")

def del_tag(): #кнопка видалити тег
    if listteg.selectedItems():
        key = listnotes.selectedItems()[0].text()
        tag = listteg.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        listteg.clear()
        listteg.addItems(notes[key]["теги"])
        with open("note_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний!")


def search_tag(): #кнопка "шукати замітку за тегом"
    button_text = searchnote.text()
    tag = field_tag.text()

    if button_text == "Шукати замітки за тегом":
        apply_tag_search(tag)
    elif button_text == "Скинути пошук":
        reset_search()

def apply_tag_search(tag):
    notes_filtered = {}
    for note, value in notes.items():
        if tag in value["теги"]:
            notes_filtered[note] = value

    button_tag_search.setText("Скинути пошук")
    list_notes.clear()
    list_tags.clear()
    list_notes.addItems(notes_filtered)

def reset_search():
    field_tag.clear()
    list_notes.clear()
    list_tags.clear()
    list_notes.addItems(notes)
    button_tag_search.setText("Шукати замітки за тегом")
deletefromnote.clicked.connect(del_tag)
deletenote.clicked.connect(del_note)
listnotes.itemClicked.connect(show_note)
savenote.clicked.connect(save_note)
addnote.clicked.connect(add_note)
print(notes)
listnotes.addItems(notes)
app.exec()

