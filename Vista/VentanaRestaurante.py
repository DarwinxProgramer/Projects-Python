# Form implementation generated from reading ui file 'VentanaRestaurante.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 711)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbTitulo = QtWidgets.QLabel(parent=Form)
        self.lbTitulo.setGeometry(QtCore.QRect(670, 10, 171, 31))
        self.lbTitulo.setObjectName("lbTitulo")
        self.lblFondo = QtWidgets.QLabel(parent=Form)
        self.lblFondo.setGeometry(QtCore.QRect(0, 0, 431, 781))
        self.lblFondo.setText("")
        self.lblFondo.setPixmap(QtGui.QPixmap("Vista/Imagenes/mantenimiento.jpg"))
        self.lblFondo.setScaledContents(True)
        self.lblFondo.setObjectName("lblFondo")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(460, 90, 261, 21))
        self.label_2.setObjectName("label_2")
        self.txtBuscarmesa = QtWidgets.QLineEdit(parent=Form)
        self.txtBuscarmesa.setGeometry(QtCore.QRect(730, 90, 271, 22))
        self.txtBuscarmesa.setObjectName("txtBuscarmesa")
        self.btnBuscar = QtWidgets.QPushButton(parent=Form)
        self.btnBuscar.setGeometry(QtCore.QRect(1020, 90, 51, 21))
        self.btnBuscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Vista/Imagenes/buscar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setObjectName("btnBuscar")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(460, 160, 141, 21))
        self.label_7.setObjectName("label_7")
        self.txtnumerodemesa = QtWidgets.QLineEdit(parent=Form)
        self.txtnumerodemesa.setGeometry(QtCore.QRect(620, 160, 231, 22))
        self.txtnumerodemesa.setObjectName("txtnumerodemesa")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(460, 210, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(460, 260, 121, 21))
        self.label_4.setObjectName("label_4")
        self.cbx_capacidad = QtWidgets.QComboBox(parent=Form)
        self.cbx_capacidad.setGeometry(QtCore.QRect(620, 210, 231, 22))
        self.cbx_capacidad.setObjectName("cbx_capacidad")
        self.cbx_capacidad.addItem("")
        self.cbx_capacidad.addItem("")
        self.cbx_capacidad.addItem("")
        self.cbx_capacidad.addItem("")
        self.cbx_capacidad.addItem("")
        self.cbx_disponibilidad = QtWidgets.QComboBox(parent=Form)
        self.cbx_disponibilidad.setGeometry(QtCore.QRect(620, 260, 231, 22))
        self.cbx_disponibilidad.setObjectName("cbx_disponibilidad")
        self.cbx_disponibilidad.addItem("")
        self.btnGuardar = QtWidgets.QPushButton(parent=Form)
        self.btnGuardar.setGeometry(QtCore.QRect(510, 340, 91, 28))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnModificar = QtWidgets.QPushButton(parent=Form)
        self.btnModificar.setGeometry(QtCore.QRect(630, 340, 91, 28))
        self.btnModificar.setObjectName("btnModificar")
        self.btnCancelar = QtWidgets.QPushButton(parent=Form)
        self.btnCancelar.setGeometry(QtCore.QRect(870, 340, 91, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnEliminar = QtWidgets.QPushButton(parent=Form)
        self.btnEliminar.setGeometry(QtCore.QRect(750, 340, 91, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.tableMesas = QtWidgets.QTableWidget(parent=Form)
        self.tableMesas.setGeometry(QtCore.QRect(510, 390, 491, 192))
        self.tableMesas.setObjectName("tableMesas")
        self.tableMesas.setColumnCount(3)
        self.tableMesas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMesas.setHorizontalHeaderItem(2, item)
        self.btnRegresar = QtWidgets.QPushButton(parent=Form)
        self.btnRegresar.setGeometry(QtCore.QRect(1030, 630, 81, 61))
        self.btnRegresar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Vista/Imagenes/atras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRegresar.setIcon(icon1)
        self.btnRegresar.setIconSize(QtCore.QSize(50, 50))
        self.btnRegresar.setObjectName("btnRegresar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbTitulo.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">Restaurante</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Ingrese el numero de mesa:</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Numero de mesa:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Capacidad:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Disponibilidad:</span></p></body></html>"))
        self.cbx_capacidad.setItemText(0, _translate("Form", "1"))
        self.cbx_capacidad.setItemText(1, _translate("Form", "2"))
        self.cbx_capacidad.setItemText(2, _translate("Form", "4"))
        self.cbx_capacidad.setItemText(3, _translate("Form", "6"))
        self.cbx_capacidad.setItemText(4, _translate("Form", "8"))
        self.cbx_disponibilidad.setItemText(0, _translate("Form", "Disponible"))
        self.btnGuardar.setText(_translate("Form", "Guardar"))
        self.btnModificar.setText(_translate("Form", "Modificar"))
        self.btnCancelar.setText(_translate("Form", "Cancelar"))
        self.btnEliminar.setText(_translate("Form", "Eliminar"))
        item = self.tableMesas.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Numero"))
        item = self.tableMesas.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Capacidad"))
        item = self.tableMesas.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Disponibilidad"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
