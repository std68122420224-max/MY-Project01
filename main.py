import sys
from PyQt6 import uic 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from name import Juice
from dao import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

        self.tbJuice.setColumnWidth(0, 50)
        self.tbJuice.setColumnWidth(1, 400)
        self.tbJuice.setColumnWidth(2, 200)

        self.showJuices()

        #event
        self.btnAdd.clicked.connect(self.insertJuice)
        self.tbJuice.cellClicked.connect(self.selectebRow)
        self.btnUpdate.clicked.connect(self.updateJuice)
        self.btnDelete.clicked.connect(self.deleteJuice)
        self.btnClear.clicked.connect(self.clearData)
        self.btnSearch.clicked.connect(self.searchJuice)

    def searchJuice(self):
        search = self.txtSearch.text()
        juices = select_by_name(search)
        self.txtSearch.setText('')
        if len(juices)>0:
            self.tbJuice.setRowCount(len(juices))
            row = 0
            for juice in juices:
                self.tbJuice.setItem(row, 0, QTableWidgetItem(str(juice.id)))
                self.tbJuice.setItem(row, 1, QTableWidgetItem(str(juice.name)))
                self.tbJuice.setItem(row, 2, QTableWidgetItem(str(juice.price)))

                row += 1
        else:
            self.tbJuice.removeRow(0)

    def showJuices(self):
        juices = select()
        if len(juices)>0:
            self.tbJuice.setRowCount(len(juices))
            row = 0
            for juice in juices:
                self.tbJuice.setItem(row, 0, QTableWidgetItem(str(juice.id)))
                self.tbJuice.setItem(row, 1, QTableWidgetItem(str(juice.name)))
                self.tbJuice.setItem(row, 2, QTableWidgetItem(str(juice.price)))

                row += 1
        else:
            self.tbJuice.removeRow(0)

    def clearData(self):
        self.txtId.setText('')
        self.txtName.setText('')
        self.txtPrice.setText('')

        self.tbJuice.clearSelection()

        self.txtName.setEnabled(True)
        self.txtPrice.setEnabled(True)

        self.btnAdd.setEnabled(True)
        self.btnUpdate.setEnabled(False)
        self.btnDelete.setEnabled(False)
        self.showJuices()

    def insertJuice(self):
        name = self.txtName.text()
        price = int(self.txtPrice.text())

        juice = Juice(id=0, name=name, price=price)
        row = insert(juice=juice)
        if row>0:
            QMessageBox.information(self, 'information', 'Insert juice successful')
        else:
            QMessageBox.warning(self, 'Warning', 'Unable to insert!')

        self.clearData()
        self.showJuices()


    def selectebRow(self):
        row = self.tbJuice.currentRow()
        id = self.tbJuice.item(row, 0).text()
        name = self.tbJuice.item(row, 1).text()
        price = self.tbJuice.item(row, 2).text()

        self.txtId.setText(id)
        self.txtName.setText(name)
        self.txtPrice.setText(price)

        self.txtName.setEnabled(False)

        self.btnAdd.setEnabled(False)
        self.btnUpdate.setEnabled(True)
        self.btnDelete.setEnabled(True)


    def updateJuice(self):
        id = int(self.txtId.text())
        name = self.txtName.text()
        price = int(self.txtPrice.text())

        juice = Juice(id=id, name=name, price=price)
        row = update(juice=juice)
        if row>0:
            QMessageBox.information(self, 'information', 'Update juice successful')
        else:
            QMessageBox.warning(self, 'Warning', 'Unable to Update!')

        self.clearData()
        self.showJuices()

    def deleteJuice(self):
        id = int(self.txtId.text())
        row = delete(id)
        if row>0:
            QMessageBox.information(self, 'information', 'Delete juice successful')
        else:
            QMessageBox.warning(self, 'Warning', 'Unable to Delete!')

        self.clearData()
        self.showJuices()

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()