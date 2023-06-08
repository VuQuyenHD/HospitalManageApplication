from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import database_feature as daf
import pandas as pd
import json
import check_features as cf


class Ui_patient_window(QMainWindow):
    def __init__(self, cnx, parent=None):
        super(Ui_patient_window, self).__init__(parent)
        self.cnx = cnx

    def setupUi(self):
        self.setObjectName("patient_window")
        self.resize(1000, 1100)
        self.setMaximumSize(QtCore.QSize(1000, 1100))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 110, 93, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("fpt_image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 871, 431))
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 500, 951, 541))
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
        self.label_5.setGeometry(QtCore.QRect(40, 70, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 40, 671, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 90, 671, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 200, 671, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 360, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(180, 280, 250, 31))
        self.comboBox.setObjectName("combobox")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 150, 671, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(40, 130, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 0, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 60, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.dataId_hospital_comboBox(self.comboBox)
        self.init_data()
        self.pushButton_3.clicked.connect(self.search_btn)
        self.pushButton_4.clicked.connect(self.add_patient)
        self.pushButton.clicked.connect(self.import_btn)
        self.pushButton_2.clicked.connect(self.export_btn)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("patient_window", "Patient Manage"))
        self.pushButton_2.setText(_translate("patient_window", "Export"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("patient_window", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("patient_window", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("patient_window", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("patient_window", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("patient_window", "Address"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("patient_window", "Hospital"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("patient_window", "Edit"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("patient_window", "Delete"))
        self.groupBox.setTitle(_translate("patient_window", "Search patients"))
        self.label_2.setText(_translate("patient_window", "Name:"))
        self.pushButton_3.setText(_translate("patient_window", "Search patient"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("patient_window", "Search"))
        self.label_4.setText(_translate("patient_window", "Name:"))
        self.label_5.setText(_translate("patient_window", "Phone:"))
        self.label_6.setText(_translate("patient_window", "Address:"))
        self.pushButton_4.setText(_translate("patient_window", "Add"))
        self.label_8.setText(_translate("patient_window", "Hospital ID:"))
        self.label_9.setText(_translate("patient_window", "Email:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("patient_window", "Add new"))
        self.label.setText(_translate("patient_window", "Patients"))
        self.pushButton.setText(_translate("patient_window", "Import"))

    def delete_btn(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id = table_model.data(table_model.index(index.row(), 0))
        name = table_model.data(table_model.index(index.row(), 1))
        button_reply = QMessageBox.question(self, 'Confirmation message',
                                            'You want to delete doctor {}?'.format(name),
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if button_reply == QMessageBox.Yes:
            if daf.delete_by_id(self.cnx, 'patient', id):
                QMessageBox.information(self, 'Success', 'Delete successfull', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Error', 'There\'s some error', QMessageBox.Close)

        self.init_data()

    def edit_btn(self):
        button = self.sender()
        index = self.tableWidget.indexAt(button.pos())
        table_model = self.tableWidget.model()
        id = table_model.data(table_model.index(index.row(), 0))
        name = table_model.data(table_model.index(index.row(), 1))
        phone = table_model.data(table_model.index(index.row(), 2))
        if not cf.check_phone(phone):
            QMessageBox.information(self, 'Error', 'Phone is not valid', QMessageBox.Close)
            return
        email = table_model.data(table_model.index(index.row(), 3))
        if not cf.check_email(email):
            QMessageBox.information(self, 'Error', 'Email is not valid', QMessageBox.Close)
            return
        address = table_model.data(table_model.index(index.row(), 4))
        hosID = table_model.data(table_model.index(index.row(), 5))
        if not daf.check_foreign_id(self.cnx.cursor(), 'hospital', hosID):
            QMessageBox.information(self, 'Error', 'Hospital ID is not valid', QMessageBox.Close)
            return
        ele = daf.get_id(self.cnx.cursor(), 'patient', id)
        if ele:
            values = (name, phone, email, address, hosID)
            labels = ('name', 'phone', 'email', 'address', 'hospital_id')
            daf.update_by_id(self.cnx, 'patient', labels, values, id)
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
        results = daf.show_table(cursor, 'patient')
        if results:
            self.data(results)

    def dataId_hospital_comboBox(self, comboBox):
        data = daf.show_table(self.cnx.cursor(), 'hospital')
        search = []
        for i in range(len(data)):
            search.append(str(data[i][0]))

        comboBox.setEditable(True)
        comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        comboBox.addItems(search)

    def search_btn(self):
        name = self.lineEdit.text()
        results = daf.search_name(self.cnx.cursor(), 'patient', name)
        if results:
            self.data(results)
        else:
            self.data([])
        self.lineEdit.clear()

    def add_patient(self):
        name = self.lineEdit_2.text()
        phone = self.lineEdit_3.text()
        if not cf.check_phone(phone):
            QMessageBox.information(self, 'Error', 'Phone is not valid', QMessageBox.Close)
            return
        email = self.lineEdit_7.text()
        if not cf.check_email(email):
            QMessageBox.information(self, 'Error', 'Email is not valid', QMessageBox.Close)
            return
        address = self.lineEdit_4.text()
        hosID = self.comboBox.currentText()
        if not daf.check_foreign_id(self.cnx.cursor(), 'hospital', hosID):
            QMessageBox.information(self, 'Error', 'Hospital ID is not valid', QMessageBox.Close)
            return
        labels = ('name', 'phone', 'email', 'address', 'hospital_id')
        values = (name, phone, email, address, hosID)
        if daf.insert_data(self.cnx, 'patient', labels, values):
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
                        "INSERT INTO patient (id, name, phone,email, address, hospital_id) VALUES (%s, %s, %s, %s, %s, %s)",
                        (df.iloc[i]['ID'], df.iloc[i]['Name'], df.iloc[i]['Phone'], df.iloc[i]['Email'],
                         df.iloc[i]['Address'],
                         df.iloc[i]['Hospital_id']))
                    self.cnx.commit()
                rows = c.fetchall()
                self.tableWidget.setRowCount(len(rows))
                for i, row in enumerate(rows):
                    for j, value in enumerate(row):
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
            except Exception as e:
                QMessageBox.information(self, "Error", f"Error: {e}")
                QMessageBox.information(self, "Hint",
                                        "Your data must follow form: ID, Name, Phone,Email, Address, Hospital_id")
        else:
            QMessageBox.information(self, "Error", "File not found")
        self.init_data()
    def export_btn(self):
        cursor = self.cnx.cursor()
        try:
            results = daf.show_table(cursor, 'patient')
            if results:
                daf.export_data('Patient', results, ['id', 'name', 'phone', 'email', 'address', 'hospitalID'])
                QMessageBox.information(self, " ", "Exported")
        except:
            QMessageBox.information(self, "Error", "Can not export file")


if __name__ == "__main__":
    with open('database_config.json') as f:
        config = json.load(f)
    cnx = daf.connect_sql(config)
    daf.connect_database(cnx, config)
    app = QtWidgets.QApplication(sys.argv)
    patient_ui = Ui_patient_window(cnx)
    patient_ui.setupUi()
    patient_ui.show()
    sys.exit(app.exec_())
