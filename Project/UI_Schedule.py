from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import database_feature as daf
import json
from datetime import datetime
import pandas as pd

class Ui_schedule_window(QMainWindow):
    def __init__(self, cnx, parent=None):
        super(Ui_schedule_window, self).__init__(parent)
        self.cnx = cnx

    def setupUi(self):
        self.setObjectName("schedule_window")
        self.resize(1000, 1150)
        self.setMaximumSize(QtCore.QSize(1000, 1150))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 110, 93, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fpt_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 550, 951, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 921, 211))
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
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setGeometry(QtCore.QRect(150, 90, 194, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(520, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(610, 90, 194, 31))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
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
        self.label_6.setGeometry(QtCore.QRect(40, 170, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 40, 671, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.doc_combobox = QtWidgets.QComboBox(self.tab_2)
        self.doc_combobox.setGeometry(QtCore.QRect(180, 180, 250, 31))
        self.doc_combobox.setObjectName("doc_combobox")
        self.patient_combobox = QtWidgets.QComboBox(self.tab_2)
        self.patient_combobox.setGeometry(QtCore.QRect(180, 270, 250, 31))
        self.patient_combobox.setObjectName("patient_combobox")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(180, 120, 241, 31))
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 871, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 160, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.dataId_hospital_comboBox(self.doc_combobox, 'doctor')
        self.dataId_hospital_comboBox(self.patient_combobox, 'patient')
        self.init_data()
        self.pushButton_3.clicked.connect(self.search_btn)
        self.pushButton_4.clicked.connect(self.add_schedule)
        self.pushButton.clicked.connect(self.import_btn)
        self.pushButton_2.clicked.connect(self.export_btn)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("schedule_window", "Schedule Manage"))
        self.pushButton.setText(_translate("schedule_window", "Import"))
        self.groupBox.setTitle(_translate("schedule_window", "Search Schedule"))
        self.label_2.setText(_translate("schedule_window", "Name:"))
        self.pushButton_3.setText(_translate("schedule_window", "Search schedule"))
        self.label_3.setText(_translate("schedule_window", "Date from:"))
        self.label_8.setText(_translate("schedule_window", "Date to:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("schedule_window", "Search"))
        self.label_4.setText(_translate("schedule_window", "Name:"))
        self.label_5.setText(_translate("schedule_window", "Date:"))
        self.label_6.setText(_translate("schedule_window", "Doctor ID:"))
        self.label_7.setText(_translate("schedule_window", "Patient ID:"))
        self.pushButton_4.setText(_translate("schedule_window", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("schedule_window", "Add new"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("schedule_window", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("schedule_window", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("schedule_window", "Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("schedule_window", "Doctor"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("schedule_window", "Patient"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("schedule_window", "Result"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("schedule_window", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("schedule_window", "Delete"))
        self.pushButton_2.setText(_translate("schedule_window", "Export"))
        self.label.setText(_translate("schedule_window", "Schedules"))

    def dataId_hospital_comboBox(self, comboBox, table):
        data = daf.show_table(self.cnx.cursor(), table)
        search = []
        for i in range(len(data)):
            search.append(str(data[i][0]))

        comboBox.setEditable(True)
        comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        comboBox.addItems(search)

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
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(str(results[i][5])))
            self.edit = QtWidgets.QPushButton(self)
            self.edit.clicked.connect(self.edit_btn)
            self.edit.setText('Edit')
            self.tableWidget.setCellWidget(i, 6, self.edit)
            self.delete = QtWidgets.QPushButton(self)
            self.delete.clicked.connect(self.delete_btn)
            self.delete.setText('Delete')
            self.tableWidget.setCellWidget(i, 7, self.delete)

    def init_data(self):
        cursor = self.cnx.cursor()
        results = daf.show_table(cursor, 'schedule')
        if results:
            self.data(results)

    def edit_btn(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id = table_model.data(table_model.index(index.row(), 0))
        name = table_model.data(table_model.index(index.row(), 1))
        date = table_model.data(table_model.index(index.row(), 2))
        docId = table_model.data(table_model.index(index.row(), 3))
        patientId = table_model.data(table_model.index(index.row(), 4))
        result = table_model.data(table_model.index(index.row(), 5))
        elements = daf.get_id(self.cnx.cursor(), 'schedule', id)
        if elements:
            values = (name, date, docId, patientId, result)
            labels = ('name', 'date', 'doctor_id', 'patient_id', 'result')
            daf.update_by_id(self.cnx, 'schedule', labels, values, id)

    def delete_btn(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id = table_model.data(table_model.index(index.row(), 0))
        name = table_model.data(table_model.index(index.row(), 1))
        button_reply = QMessageBox.question(self, 'Confirmation',
                                            'You want to delete schedule {}?'.format(name),
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            if daf.delete_by_id(self.cnx, 'schedule', id):
                QMessageBox.information(self, 'Success', 'Deleted', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Error', 'Error', QMessageBox.Close)

        self.init_data()

    def search_btn(self):
        name = self.lineEdit.text()
        dateFrom = self.dateTimeEdit.dateTime().toPyDateTime()
        dateTo = self.dateTimeEdit_2.dateTime().toPyDateTime()
        dateFrom = datetime(dateFrom.year, dateFrom.day, dateFrom.month, dateFrom.hour, dateFrom.minute)
        dateTo = datetime(dateTo.year, dateTo.day, dateTo.month, dateTo.hour, dateTo.minute)
        if dateTo < dateFrom:
            QMessageBox.information(self, 'Error', 'Date from must be lower Date to', QMessageBox.Close)
            return
        results = daf.search_schedule(self.cnx.cursor(), name, dateFrom, dateTo)
        print(results)
        if results:
            self.data(results)
        else:
            self.data([])

    def add_schedule(self):
        name = self.lineEdit_2.text()
        date = self.dateTimeEdit_3.dateTime().toPyDateTime()
        date = datetime(date.year, date.day, date.month, date.hour, date.minute)
        docID = self.doc_combobox.currentText()
        patientID = self.patient_combobox.currentText()
        if not daf.check_foreign_id(self.cnx.cursor(), 'doctor', docID):
            QMessageBox.information(self, 'Error', 'Doctor ID not valid', QMessageBox.Close)
            return
        if not daf.check_foreign_id(self.cnx.cursor(), 'patient', patientID):
            QMessageBox.information(self, 'Error', 'Patient ID not valid', QMessageBox.Close)
            return
        labels = ('name', 'date', 'doctor_id', 'patient_id')
        values = (name, date, docID, patientID)
        if daf.insert_data(self.cnx, 'schedule', labels, values):
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
                        "INSERT INTO schedule (id, name, date,doctor_id, patient_id, result) VALUES (%s, %s, %s, %s, %s, %s)",
                        (df.iloc[i]['ID'], df.iloc[i]['Name'], df.iloc[i]['Date'], df.iloc[i]['Doctor ID'],
                         df.iloc[i]['Patient ID'],
                         df.iloc[i]['Result']))
                    self.cnx.commit()
                rows = c.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
            except Exception as e:
                QMessageBox.information(self, "Error", f"Error: {e}")
                QMessageBox.information(self, "Hint",
                                        "Your data must follow form: ID, Name, Date,Doctor ID, Patient ID, Result")
        else:
            QMessageBox.information(self, "Error", "File not found")
        self.init_data()
    def export_btn(self):
        cursor = self.cnx.cursor()
        try:
            results = daf.show_table(cursor, 'schedule')
            if results:
                daf.export_data('Schedule', results, ['id', 'name', 'date', 'doctor_id', 'patient_id', 'result'])
        except:
            print('Error')


if __name__ == "__main__":
    with open('database_config.json') as f:
        config = json.load(f)
    cnx = daf.connect_sql(config)
    daf.connect_database(cnx, config)
    app = QtWidgets.QApplication(sys.argv)
    schedule_ui = Ui_schedule_window(cnx)
    schedule_ui.setupUi()
    schedule_ui.show()
    sys.exit(app.exec_())
