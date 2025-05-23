import sys
import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from cad_paciente import Ui_MainWindow
from cad_consultas import Ui_MainWindow as Ui_Consultas
from contr_dietas import Ui_MainWindow as Ui_ContrDietas
from rela_graf import Ui_MainWindow as Ui_Graficos
from contr_finan import Ui_MainWindow as Ui_Financeiro


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.cadPaciente)
        self.ui.pushButton_3.clicked.connect(self.filtrar)
        self.ui.pushButton_4.clicked.connect(self.pagConsulta)

        self.db_connection = mysql.connector.connect(
            host = "localhost",
            database = "SistemaNutri",
            user = "root",
            password = "",
        )
        self.cursor = self.db_connection.cursor()

    def pagConsulta(self):
        self.tela_consultas = TelaConsultas()
        self.tela_consultas.show()
        self.close()

    def pagContrDietas(self):
        self.tela_consultas = TelaContrDietas()
        self.tela_consultas.show()
        self.close()

    def cadPaciente(self):
        nome = self.ui.lineEdit.text()
        idade = self.ui.lineEdit_2.text()
        sexo = self.ui.lineEdit_3.text()
        peso = self.ui.lineEdit_4.text()
        altura = self.ui.lineEdit_5.text()
        histMedi = self.ui.textEdit.toPlainText()
        alergias = self.ui.lineEdit_7.text()
        imc = self.ui.lineEdit_8.text()

        if nome and idade and sexo and peso and altura and histMedi and alergias and imc:
            try:
                query = "INSERT INTO cad_pacientes(nome, idade, sexo, peso, altura, histmedi, alergias, imc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (nome, idade, sexo, peso, altura, histMedi, alergias, imc)
                self.cursor.execute(query, values)

                self.db_connection.commit()

                QMessageBox.information(self, "Sucesso", "Paciente cadastrado com sucesso!")

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Erro", f"Erro ao cadastrar o paciente {err}")

        else:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")

    def closeEvent(self, event):
        self.cursor.close()
        self.db_connection.close()
        event.accept()

    def filtrar(self):
        idade = self.ui.lineEdit_6.text()
        peso = self.ui.lineEdit_9.text()
        imc = self.ui.lineEdit_10.text()

        if idade and peso and imc:
            try:
                query = "SELECT * FROM cad_pacientes WHERE idade= %s AND peso= %s AND imc= %s"
                self.cursor.execute(query, (idade, peso, imc))
                resultado = self.cursor.fetchone()

                self.ui.textEdit_2.setPlainText(f"Nome: {resultado[1]}")

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Erro", f"Erro ao filtrar o paciente {err}")
        
        else:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")

class TelaConsultas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Consultas()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.agendar)
        self.ui.pushButton_4.clicked.connect(self.pagContrDietas)

        self.db_connection = mysql.connector.connect(
            host = "localhost",
            database = "SistemaNutri",
            user = "root",
            password = "",
        )
        self.cursor = self.db_connection.cursor()

    def pagContrDietas(self):
        self.tela_contrDietas = TelaContrDietas()
        self.tela_contrDietas.show()
        self.close()

    def agendar(self):
        nome = self.ui.lineEdit.text()
        data = self.ui.lineEdit_2.text()
        hora = self.ui.lineEdit_3.text()
        anotacao = self.ui.textEdit.toPlainText()

        if nome and data and hora and anotacao:
            try:
                query = "INSERT INTO cad_consultas(nome, data_consulta, hora, anot) VALUES (%s, %s, %s, %s)"
                values =  (nome, data, hora, anotacao)
                self.cursor.execute(query, values)
                self.db_connection.commit()

                QMessageBox.information(self, "Sucesso", "Consulta cadastrada com sucesso!")

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Erro", f"Erro ao cadastrar consulta {err}")

        else:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")

class TelaContrDietas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ContrDietas()
        self.ui.setupUi(self)

        self.db_connection = mysql.connector.connect(
            host = "localhost",
            database = "SistemaNutri",
            user = "root",
            password = "",
        )
        self.cursor = self.db_connection.cursor()

        self.ui.pushButton.clicked.connect(self.cadastrPlano)
        self.ui.pushButton_4.clicked.connect(self.pag_finan)

    def pag_finan(self):
        self.tela_grafics = TelaFinanceiro()
        self.tela_grafics.show()
        self.close()

    def cadastrPlano(self):
        paciente = self.ui.lineEdit.text()
        plano = self.ui.textEdit.toPlainText()
        hist = self.ui.textEdit_2.toPlainText()

        if paciente and plano:
            try:
                query = "INSERT INTO contr_dietas(paciente, planoAlimen) VALUES (%s, %s)"
                values = (paciente, plano)
                self.cursor.execute(query, values)
                self.db_connection.commit()

                QMessageBox.information(self, "Sucesso", "Plano alimentar cadastrado com sucesso!")

            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Erro", f"Erro ao cadastrar plano alimentar {err}")

            paciente = self.ui.lineEdit.clear()

        else:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos!")

        self.ui.textEdit_2.setPlainText(f"Histórico: {plano}")

#class TelaGraficos(QMainWindow):
    #def __init__(self):
        #super().__init__()
        #self.ui = Ui_Graficos()
        #self.ui.setupUi(self)

        #self.ui.pushButton.clicked.connect(self.gerar1)
        #self.ui.pushButton_2.clicked.connect(self.gerar2)

        #self.db_connection = mysql.connector.connect(
            #host = "localhost",
            #database = "SistemaNutri",
            #user = "root",
            #password = "",
        #)
        #self.cursor = self.db_connection.cursor()

    #def gerar1(self):
        #paciente = self.ui.lineEdit.text()

class TelaFinanceiro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Financeiro()
        self.ui.setupUi(self)





        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())