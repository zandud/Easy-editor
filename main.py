from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout,
   QRadioButton, QGroupBox, QButtonGroup, QTextEdit, QLineEdit 
)
from os import *
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance
app = QApplication([])
window = QWidget()
window.resize(1000, 800)
window.setWindowTitle('Easy Editor')
pic1 = QLabel('Картинка')
spisok1 = QListWidget()
button1 = QPushButton('Папка')
button2 = QPushButton('Лево')
button3 = QPushButton('Право')
button4 = QPushButton('Зеркальный вид')
button5 = QPushButton('Резкость')
button6 = QPushButton('Ч/Б')
button7 = QPushButton('Контрастность')
button8 = QPushButton('Негатив')
button9 = QPushButton('Размытие')
v1 = QVBoxLayout()
v1.addWidget(button1)
v1.addWidget(spisok1)
v2 = QVBoxLayout()
v2.addWidget(pic1)
h1 = QHBoxLayout()
h1.addWidget(button2)
h1.addWidget(button3)
h1.addWidget(button4)
h1.addWidget(button5)
h1.addWidget(button9)
h1.addWidget(button6)
h1.addWidget(button7)
h1.addWidget(button8)
v2.addLayout(h1)
maneline = QHBoxLayout()
maneline.addLayout(v1, stretch=5)
maneline.addLayout(v2, stretch=15)
window.setLayout(maneline)
papka = ''

class ImageProcessor():
   def __init__(self):
      self.image = None
      self.papka = papka
      self.file_name = None
      self.new_papka = 'Изменённые_фото/'
   def loadImage(self, file_name):
      self.file_name = file_name
      self.file_path = path.join(self.papka, self.file_name)
      print(self.file_path)
      self.image = Image.open(self.file_path)
   def showImage(self, p):
      pic1.hide()
      pix = QPixmap(p)
      pix = pix.scaled(pic1.width(), pic1.height(), Qt.KeepAspectRatio)
      pic1.setPixmap(pix)
      pic1.show()
   def save_comp(self):
      p = path.join(self.papka, self.new_papka)
      if path.exists(p) != True or path.isdir(p) != True:
         mkdir(p)
      p = path.join(p, self.file_name)
      self.image.save(p)
    
   
   def gray(self):
      self.image = self.image.convert('L')
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def left(self):
      self.image = self.image.transpose(Image.ROTATE_90)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def right(self):
      self.image = self.image.transpose(Image.ROTATE_270)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def mirror(self):
      self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def sharp(self):
      self.image = self.image.filter(ImageFilter.SHARPEN)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def contrast(self):
      self.image = ImageEnhance.Contrast(self.image).enhance(2)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def negative(self):
      self.image = ImageEnhance.Contrast(self.image).enhance(-1)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)
   def blur(self):
      self.image = self.image.filter(ImageFilter.BLUR)
      self.save_comp()
      p = path.join(self.papka, self.new_papka, self.file_name)
      self.showImage(p)







def filter_pic(save):
   graphyx = ['.png' , '.jpg' , '.jpeg', '.gif']
   result = []
   for file_name in save:
      _,ext = path.splitext(file_name)
      if ext in graphyx:
         result.append(file_name)
   return result



def open_papka():
   global papka
   papka = QFileDialog.getExistingDirectory()
   current.papka = papka
   try:
      save = listdir(papka)
   except:
      save = []
   pictures = filter_pic(save)
   spisok1.clear()
   spisok1.addItems(pictures)
      
   

def showChosenImage():
   if spisok1.selectedItems():
       key = spisok1.selectedItems()[0].text()
       current.loadImage(key)
       current.showImage(current.file_path)




# with Image.open('original.jpg') as original:
#     print('Размер:' , original.size)
#     print('Формат:' , original.format)
#     print('Тип:' , original.mode)
#     pic_gray = original.convert('L')
#     pic_gray.save('gray.jpg')
#     pic_blured = original.filter(ImageFilter.BLUR)
#     pic_blured.save('blures.jpg')
#     pic_up = original.transpose(Image.ROTATE_180)
#     a1 = pic_up.convert('L')
#     a1.save('a1.jpg')
#     pic_up.save('up.jpg')
#     mirrow = original.transpose(Image.FLIP_LEFT_RIGHT)
#     mirrow.save('mirrow.jpg')
#     pic_contrast = ImageEnhance.Contrast(original).enhance(-1)
#     pic_contrast.save('contrast.jpg')













current = ImageProcessor()
button6.clicked.connect(current.gray)
button1.clicked.connect(open_papka)
button2.clicked.connect(current.left)
button3.clicked.connect(current.right)
button4.clicked.connect(current.mirror)
button5.clicked.connect(current.sharp)
button7.clicked.connect(current.contrast)
button8.clicked.connect(current.negative)
button9.clicked.connect(current.blur)

spisok1.itemClicked.connect(showChosenImage)
# button2.clicked.connect(deleted)
# button3.clicked.connect(save)


window.show()
app.exec()