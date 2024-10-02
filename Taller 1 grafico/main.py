import sys
import subprocess,platform,os;
import itertools
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from vPrincipal import Ui_Wprincipal
from punto1 import Ui_Punto1
from punto2 import Ui_Punto2
from punto3 import Ui_punto3
sys.path.append(os.path.abspath("./Files/img"))
import imgVM_rc

def concatenacionRecu(listas, index=0):
    # Caso base: Si ya hemos recorrido todas las listas, retornar una lista vacía como base
    if index == len(listas):
        return ['']
    
    # Obtener la lista resultante del siguiente nivel de recursividad
    listaRecorrer = concatenacionRecu(listas, index + 1)
    
    # Resultado para esta etapa
    resultado = []
    
    # Añadir los elementos individuales primero
    if index == 0:
        for lista in listas:
            resultado.extend(lista)
    
    # Generar combinaciones cruzadas
    for elemento1 in listas[index]:
        for elemento2 in listaRecorrer:
            # Concatenar los elementos y agregarlos al resultado
            resultado.append(elemento1 + elemento2)
    
    return resultado

def cerraduraKleene(lista, max_length):
    # Caso base: La lista vacía está siempre incluida
    resultado = ['ε']
    
    # Generar combinaciones de longitud 1 hasta max_length
    def concatenacionRecu(listas, longitud_actual):
        # Caso base: si la longitud actual supera el máximo permitido
        if longitud_actual == 0:
            return ['']
        
        # Obtener el resultado de la combinación recursiva
        listaRecorrer = concatenacionRecu(listas, longitud_actual - 1)
        
        # Generar nuevas combinaciones concatenando con elementos de la lista
        resultado = []
        for elemento1 in listas:
            for elemento2 in listaRecorrer:
                resultado.append(elemento1 + elemento2)
        return resultado
    
    # Para todas las longitudes desde 1 hasta max_length, agregar las combinaciones al resultado
    for longitud in range(1, max_length + 1):
        resultado.extend(concatenacionRecu(lista, longitud))
    
    return resultado

def productoCruz(lista1,lista2):
    productoX = []

    for estado, transicion in itertools.product(lista1, lista2):
        
        if estado!=">1300":
        
            nuevo_estado = estado + transicion
            
            if nuevo_estado <= 1300 and nuevo_estado>0:
                productoX.append((estado, transicion, nuevo_estado))

            if nuevo_estado > 1300 and nuevo_estado:
                productoX.append((estado, transicion, ">1300"))
           
            
    return productoX
        
def generarDefVM():
        s = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300,">1300"]
        sigma= [+100,-100,+200,-200,+500,-500];
        delta = productoCruz(s,sigma);
        i = [0];
        f = [1300];
        defVm = [s,sigma,delta,i,f]
        return defVm

    

class Mydialog(QDialog):
    def __init__(self):
        super().__init__();
        self.ui = Ui_Wprincipal();
        self.ui.setupUi(self);
        self.ui.BtnAbrirPdf.clicked.connect(self.abrirPdf)
        self.ui.BtnPrimerPunto.clicked.connect(self.abrirPunto1);
        self.ui.Btn2Punto.clicked.connect(self.abrirPunto2);
        self.ui.BtnVM.clicked.connect(self.abrirPunto3);
        
        
    def abrirPunto1(self):
        self.punto1 = QDialog(self);
        self.ui2=Ui_Punto1();
        self.ui2.setupUi(self.punto1);
        self.ui2.BtnGenerar.clicked.connect(self.generarConca)
        self.ui2.txtl1.setText("x,y,z")
        self.ui2.txtl2.setText("0,1")
        self.ui2.txtl3.setText("a,b")
        self.punto1.exec_();
        
    def abrirPunto2(self):
        self.punto2 = QDialog(self);
        self.ui3=Ui_Punto2();
        self.ui3.setupUi(self.punto2);
        self.ui3.BtnGenerarTablaV.clicked.connect(self.generarTabla)
        self.punto2.exec_();
    
    def abrirPunto3(self):
        self.punto3 = QDialog(self);
        self.ui4=Ui_punto3();
        self.ui4.setupUi(self.punto3);
        self.ui4.txtDefVM.setPlainText(str(generarDefVM()))
        self.ui4.btn500mas.clicked.connect(lambda: self.sumarDinero(500))
        self.ui4.btn500menos.clicked.connect(lambda:self.sumarDinero(-500))
        self.ui4.btn200mas.clicked.connect(lambda: self.sumarDinero(200))
        self.ui4.btn200menos.clicked.connect(lambda:self.sumarDinero(-200))
        self.ui4.btn100mas.clicked.connect(lambda: self.sumarDinero(100))
        self.ui4.btn100menos.clicked.connect(lambda: self.sumarDinero(-100))
        self.ui4.txtCantidadTotal.setText("0");
        self.punto3.exec_();
        
    def generarConca(self):
        L1 = self.ui2.txtl1.text();
        L2 = self.ui2.txtl2.text();
        L3 = self.ui2.txtl3.text();
        L1Lista = L1.split(',');
        L2Lista = L2.split(",");
        L3Lista = L3.split(",");
        listasA=[L1Lista,L2Lista];
        listasB=[L3Lista,L1Lista];
        listasC=[L1Lista,L2Lista,L3Lista];
        A = concatenacionRecu(listasA);
        B = concatenacionRecu(listasB);
        C = concatenacionRecu(listasC);
        self.ui2.lbALineEdit.setText(str(A));
        self.ui2.lbBLineEdit.setText(str(B));
        self.ui2.lbCLineEdit.setText(str(C));
        D= cerraduraKleene(L1Lista,len(L1Lista))
        self.ui2.lbCLineEdit_2.setPlainText(str(D))
        listasE=[L2Lista,L3Lista]
        e= concatenacionRecu(listasE)
        print(e)
        print(len(e))
        e2=cerraduraKleene(e[4:],len(e))
        self.ui2.lbCLineEdit_3.setPlainText(str(e2))
        
    def generarTabla(self):
        
        variables= [True,False];
        
        model1 = QStandardItemModel()
        model1.setHorizontalHeaderLabels(["p","q","(p Λ q)","¬(p Λ q)"])
        for p in variables:
            for q in variables:
                resultado1 = not(p and q);
                row = [
                    QStandardItem(str(p)),
                    QStandardItem(str(q)),
                    QStandardItem(str(p and q)),
                    QStandardItem(str(resultado1))
                ]
                model1.appendRow(row)
        self.ui3.TbMorgan1.setModel(model1);
        
        self.ui3.TbMorgan1.resizeColumnsToContents();
        self.ui3.TbMorgan1.resizeRowsToContents();
        
        model2 = QStandardItemModel()
        model2.setHorizontalHeaderLabels(["p","q","(¬p)","(¬q)","(¬p)∨(¬q)"])
        for p in variables:
            for q in variables:
                resultado1 = not(p) or not(q);
                row = [
                    QStandardItem(str(p)),
                    QStandardItem(str(q)),
                    QStandardItem(str(not(p))),
                    QStandardItem(str(not(q))),
                    QStandardItem(str(resultado1)),
                ]
                model2.appendRow(row)
        self.ui3.TbMorgan2.setModel(model2);
        self.ui3.TbMorgan2.resizeColumnsToContents();
        self.ui3.TbMorgan2.resizeRowsToContents();
        
        model3 = QStandardItemModel()
        model3.setHorizontalHeaderLabels(["p","q","(p ∨ q)","¬ (p ∨ q"])
        for p in variables:
            for q in variables:
                resultado1 = not(p or q);
                row = [
                    QStandardItem(str(p)),
                    QStandardItem(str(q)),
                    QStandardItem(str(p and q)),
                    QStandardItem(str(resultado1))
                ]
                model3.appendRow(row)
        self.ui3.TbMorgan3.setModel(model3);
        self.ui3.TbMorgan3.resizeColumnsToContents();
        self.ui3.TbMorgan3.resizeRowsToContents();
        
        model4 = QStandardItemModel()
        model4.setHorizontalHeaderLabels(["p","q","(¬p)","(¬q)","(¬p)Λ(¬q)"])
        for p in variables:
            for q in variables:
                resultado1 = not(p) and not(q);
                row = [
                    QStandardItem(str(p)),
                    QStandardItem(str(q)),
                    QStandardItem(str(not(p))),
                    QStandardItem(str(not(q))),
                    QStandardItem(str(resultado1)),
                ]
                model4.appendRow(row)
        self.ui3.TbMorgan4.setModel(model4);
        self.ui3.TbMorgan4.resizeColumnsToContents();
        self.ui3.TbMorgan4.resizeRowsToContents();
        
        
    def abrirPdf(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(current_dir, 'Files', 'Taller1.pdf')
        print(pdf_path)

        # Intentar abrir el archivo
        try:
            os.startfile(pdf_path)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {pdf_path}")
            
    def darVueltas(self):
        cantidadActual= int(self.ui4.txtCantidadTotal.text())
        mond500=0
        mond200=0
        mond100=0
        diferencia = cantidadActual - 1300;
        while(diferencia>0):
        
            if diferencia>=500:
                    diferencia-=500;
                    mond500+=1
                    
            if diferencia>=200:
                    diferencia-=200;
                    mond200+=1
                    
            if diferencia>=100:
                    diferencia-=100;
                    mond100+=1
            else:
                break
        
        
        self.ui4.lbMon500Dev.setText(str(mond500));
        self.ui4.lbMon200Dev.setText(str(mond200));
        self.ui4.lbMon100Dev.setText(str(mond100));
        
        cantidadT = (mond500*500) + (mond200*200) + (mond100 * 100)
        self.ui4.txtTotalDev.setText(str(cantidadT))
        
    def sumarDinero(self,cantidad):
        match cantidad:
            case 500:
                cantidadActual= int(self.ui4.lbCmoneda500.text());
                self.ui4.lbCmoneda500.setText(str(cantidadActual+1))
            case -500:
                cantidadActual= int(self.ui4.lbCmoneda500.text());
                if cantidadActual>0:
                    self.ui4.lbCmoneda500.setText(str(cantidadActual-1))
                
            case 200:
                cantidadActual= int(self.ui4.lbCmoneda200.text());
                self.ui4.lbCmoneda200.setText(str(cantidadActual+1))
            case -200:
                cantidadActual= int(self.ui4.lbCmoneda200.text());
                if cantidadActual>0:
                    self.ui4.lbCmoneda200.setText(str(cantidadActual-1))
                
            case 100:
                cantidadActual= int(self.ui4.lbCmoneda100.text());
                self.ui4.lbCmoneda100.setText(str(cantidadActual+1))
            case -100:
                cantidadActual= int(self.ui4.lbCmoneda100.text());
                if cantidadActual>0:
                    self.ui4.lbCmoneda100.setText(str(cantidadActual-1))
        
        cantidad500 = self.ui4.lbCmoneda500.text();
        cantidad200 = self.ui4.lbCmoneda200.text();
        cantidad100= self.ui4.lbCmoneda100.text();
        
        cantidadtotal=(int(cantidad500)*500)+(int(cantidad200)*200)+(int(cantidad100)*100)
        self.ui4.txtCantidadTotal.setText(str(cantidadtotal))
        if cantidadtotal > 1300:
            self.darVueltas();
        else:
            self.ui4.txtTotalDev.setText("0")
            self.ui4.lbMon500Dev.setText("0");
            self.ui4.lbMon200Dev.setText("0");
            self.ui4.lbMon100Dev.setText("0");
        
    
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv);
    dialog = Mydialog();
    dialog.show();
    sys.exit(app.exec_())
    
