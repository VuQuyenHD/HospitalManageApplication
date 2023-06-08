from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from UI_Doctors import Ui_doctor_window
from UI_Patients import Ui_patient_window
from UI_Schedule import Ui_schedule_window
import database_feature as daf
import check_features as cf
import sys
import json
import os
import pandas as pd


class Ui_hospital_window(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_hospital_window, self).__init__(parent)
        if cf.check_file_open('database_config.json'):
                with open('database_config.json') as f:
                    config = json.load(f)
                    f.close()
                self.cnx = daf.connect_sql(config)
                daf.connect_database(self.cnx, config)


    def setupUi(self):
        self.setObjectName("hospital_window")
        self.resize(1000, 1100)
        self.setMaximumSize(QtCore.QSize(1000, 1100))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, -10, 211, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fpt_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 880, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 80, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 140, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 510, 951, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 921, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 21, 751, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(40, 100, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(40, 170, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 40, 671, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 110, 671, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 180, 671, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 270, 671, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionConfig = QtWidgets.QAction(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfig.setIcon(icon)
        self.actionConfig.setObjectName("actionConfig")
        self.actionDoctor = QtWidgets.QAction(self)
        self.actionDoctor.setIcon(icon)
        self.actionDoctor.setObjectName("actionDoctor")
        self.actionPatient = QtWidgets.QAction(self)
        self.actionPatient.setIcon(icon)
        self.actionPatient.setObjectName("actionPatient")
        self.actionScheduel = QtWidgets.QAction(self)
        self.actionScheduel.setIcon(icon)
        self.actionScheduel.setObjectName("actionScheduel")
        self.menuSetting.addAction(self.actionConfig)
        self.menuProgram.addAction(self.actionDoctor)
        self.menuProgram.addAction(self.actionPatient)
        self.menuProgram.addAction(self.actionScheduel)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())
        self.init_data()
        self.actionConfig.triggered.connect(self.config)
        self.pushButton_3.clicked.connect(self.search_btn)
        self.pushButton_4.clicked.connect(self.add_hospital)
        self.pushButton.clicked.connect(self.import_btn)
        self.pushButton_2.clicked.connect(self.export_btn)
        self.actionDoctor.triggered.connect(self.doctor_connect)
        self.actionPatient.triggered.connect(self.patient_connect)
        self.actionScheduel.triggered.connect(self.schedule_connect)
        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("hospital_window", "Hospital Manage"))
        self.label.setText(_translate("hospital_window", "Hospitals"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("hospital_window", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("hospital_window", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("hospital_window", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("hospital_window", "Address"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("hospital_window", "Description"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("hospital_window", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("hospital_window", "Delete"))
        self.pushButton.setText(_translate("hospital_window", "Import"))
        self.pushButton_2.setText(_translate("hospital_window", "Export"))
        self.groupBox.setTitle(_translate("hospital_window", "Search doctor"))
        self.label_2.setText(_translate("hospital_window", "Name:"))
        self.pushButton_3.setText(_translate("hospital_window", "Search hospital"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("hospital_window", "Search"))
        self.label_4.setText(_translate("hospital_window", "Name:"))
        self.label_5.setText(_translate("hospital_window", "Phone:"))
        self.label_6.setText(_translate("hospital_window", "Address:"))
        self.label_7.setText(_translate("hospital_window", "Desciption:"))
        self.pushButton_4.setText(_translate("hospital_window", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("hospital_window", "Add new"))
        self.menuSetting.setTitle(_translate("hospital_window", "Setting"))
        self.menuProgram.setTitle(_translate("hospital_window", "Program"))
        self.actionConfig.setText(_translate("hospital_window", "Config"))
        self.actionDoctor.setText(_translate("hospital_window", "Doctor"))
        self.actionPatient.setText(_translate("hospital_window", "Patient"))
        self.actionScheduel.setText(_translate("hospital_window", "Schedule"))


    def config(self):
        filename = 'database_config.json'
        if cf.check_file_open(filename):
            os.system('notepad.exe {}'.format(filename))
            with open(filename) as f:
                config = json.load(f)
                f.close()
            self.cnx = daf.connect_sql(config)
            daf.connect_database(self.cnx, config)
            self.init_data()
        else:
            QMessageBox.information(self, 'Error', 'Error', QMessageBox.Close)


    def init_data(self):
        cursor = self.cnx.cursor()
        results = daf.show_table(cursor, 'hospital')
        if results:
            self.data(results)


    def doctor_connect(self):
        self.doctor = Ui_doctor_window(cnx=self.cnx)
        self.doctor.setupUi()
        self.doctor.show()


    def patient_connect(self):
        self.patient = Ui_patient_window(cnx=self.cnx)
        self.patient.setupUi()
        self.patient.show()


    def schedule_connect(self):
        self.schedule = Ui_schedule_window(cnx=self.cnx)
        self.schedule.setupUi()
        self.schedule.show()


    def delete_btn(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id = table_model.data(table_model.index(index.row(), 0))
        name = table_model.data(table_model.index(index.row(), 1))
        warning_btn = QMessageBox.question(self, 'Confirmation message',
                                           'You want to delete hospital {}?'.format(name),
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if warning_btn == QMessageBox.Yes:
            if daf.delete_by_id(self.cnx, 'hospital', id):
                QMessageBox.information(self, 'Delete', 'Deleted', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Error', 'I be error')

        self.init_data()


    def edit_btn(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id = table_model.data(table_model.index(index.row(), 0))
        name = table_model.data(table_model.index(index.row(), 1))
        phone = table_model.data(table_model.index(index.row(), 2))
        address = table_model.data(table_model.index(index.row(), 3))
        description = table_model.data(table_model.index(index.row(), 4))
        ele = daf.get_id(self.cnx.cursor(), 'hospital', id)
        if ele:
            values = (name, phone, address, description)
            labels = ('name', 'phone', 'address', 'description')
            daf.update_by_id(self.cnx, 'hospital', labels, values, id)
        self.init_data()


    def data(self, results):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for i in range(len(results)):
            self.tableWidget.insertRow(i)
            item = QtWidgets.QTableWidgetItem(str(results[i][0]))
            item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
            self.tableWidget.setItem(i, 0, item)
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(results[i][1])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(results[i][2])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(results[i][3])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(results[i][4])))
            self.edit = QtWidgets.QPushButton(self)
            self.edit.clicked.connect(self.edit_btn)
            self.edit.setText('Edit')
            self.tableWidget.setCellWidget(i, 5, self.edit)
            self.delete = QtWidgets.QPushButton(self)
            self.delete.clicked.connect(self.delete_btn)
            self.delete.setText('Delete')
            self.tableWidget.setCellWidget(i, 6, self.delete)


    def search_btn(self):
        name = self.lineEdit.text()
        results = daf.search_name(self.cnx.cursor(), 'hospital', name)
        if results:
            self.data(results)
        else:
            self.data([])
        self.lineEdit.clear()


    def add_hospital(self):
        name = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        description = self.lineEdit_5.text()
        labels = ('name', 'phone', 'address', 'description')
        values = (name, phone, address, description)
        if daf.insert_data(self.cnx, 'hospital', labels, values):
            result = daf.retrive(self.cnx.cursor(), 'doctor', 1)
            if result:
                self.data(result)
        self.init_data()


    def import_btn(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File", "", "Excel Files (*.xlsx)")

        if fileName:
            try:
                # Read data from file using pandas
                df = pd.read_excel(fileName)

                df = df.astype(str)
                c = self.cnx.cursor()
                for i in range(len(df)):
                    c.execute(
                        "INSERT INTO hospital (id, name, phone, address, description) VALUES (%s, %s, %s, %s, %s)",
                        (df.iloc[i]['ID'], df.iloc[i]['Name'], df.iloc[i]['Phone'], df.iloc[i]['Address'],
                         df.iloc[i]['Description']))
                    self.cnx.commit()
                c.execute("SElECT * FROM hospital")
                rows = c.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
            except Exception as e:
                QMessageBox.information(self, "Error", f"Error: {e}")
                QMessageBox.information(self, "Hint",
                                        "Your data must follow form: ID, Name, Phone, Address, Description")
        else:
            QMessageBox.information(self, "Error", "File not found")
        self.init_data()


    def export_btn(self):
        cursor = self.cnx.cursor()
        try:
            results = daf.show_table(cursor, 'hospital')
            if results:
                daf.export_data('Hospital', results, ['id', 'name', 'phone', 'address', 'description'])
        except:
            print('Error')


if __name__ == "__main__":
    with open('database_config.json') as f:
        config = json.load(f)
        f.close()
    dirname = 'Output'
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_hospital_window()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
