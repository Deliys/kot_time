import os
import time
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
import subprocess
def change_file_creation_time(file_path, timestamp):

	dateTime = datetime.datetime.fromtimestamp(timestamp)

	# Получите год из datetime
	year = dateTime.year

	os.system('date {}-{}-{}'.format(dateTime.day,dateTime.month,dateTime.year))
	os.system('time {}:{}:{}'.format(dateTime.hour,dateTime.minute,23))

	source_file = file_path
	destination_folder = "export"

	# проверяем, существует ли указанный файл
	if os.path.isfile(source_file):
		print("export/"+source_file.split('/')[-1])
		if os.path.isfile("export/"+source_file.split('/')[-1]):
			os.system('del {}'.format("export/"+source_file.split('/')[-1]))
		
		# создаем указанную директорию, если ее нет
		os.makedirs(destination_folder, exist_ok=True)
		# копируем файл в указанную директорию
		shutil.copy(source_file, destination_folder)
		print("Файл успешно скопирован в папку", destination_folder)
	else:
		print("Указанный файл не существует")
	# Установить время синхронизации с сервером времени в Интернете time.windows.com
	subprocess.run(['w32tm', '/config', '/manualpeerlist:time.windows.com', '/syncfromflags:manual', '/update'], shell=True)

	# Запустить процесс синхронизации времени
	subprocess.run(['w32tm', '/resync'], shell=True)
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(229, 199)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 231, 201))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
		self.dateTimeEdit.setObjectName("dateTimeEdit")
		self.verticalLayout_2.addWidget(self.dateTimeEdit)
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.verticalLayout_2.addWidget(self.pushButton)
		self.verticalLayout.addLayout(self.verticalLayout_2)
		self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.verticalLayout.addWidget(self.label_2)
		self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
		self.textEdit.setObjectName("textEdit")
		self.verticalLayout.addWidget(self.textEdit)
		self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.on_button_clicked)  # подключение обработчика нажатия
		self.verticalLayout_2.addWidget(self.pushButton)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	def on_button_clicked(self):
		# обработчик нажатия на кнопку
		for file_path in self.textEdit.toPlainText().splitlines():
			file_path =str(file_path).split("file:///")[1]  # получаем путь к файлу из textEdit
			timestamp = int(time.mktime(self.dateTimeEdit.dateTime().toPyDateTime().timetuple()))  # преобразуем время в Unix-формат
			change_file_creation_time(file_path, timestamp)  # вызываем функцию, которая изменит время создания файла
			
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "KOT TIME"))
		self.pushButton.setText(_translate("MainWindow", "изменить время создания"))
		self.label_2.setText(_translate("MainWindow", "Перетени сюда файл"))
		self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())