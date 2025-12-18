from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import load

nph="evaluation.dat"

    

def consulter():
    op = w.sel.currentText()
    
    w.tab.setRowCount(0)
    f = open(nph,"rb")
    
    l=0
    s=0
    eof = False
    
    while not(eof):
        try:
            e = load(f)
            if e['exp'].find(op)!=-1:
                w.tab.insertRow(l)
                w.tab.setItem(l , 0 ,  QTableWidgetItem(e['id']))
                w.tab.setItem(l , 1 ,  QTableWidgetItem(e['exp']))
                w.tab.setItem(l , 2 ,  QTableWidgetItem(e['rep']))
                if e['valid']=="vrai":
                    w.tab.setItem(l , 3 ,  QTableWidgetItem("reponse correcte"))
                    s=s+1
                if e['valid']=="faux":
                    w.tab.setItem(l , 3 ,  QTableWidgetItem("reponse eronne"))
        except:
            eof=True
    w.nb.setText("nb des reponses correcte pour op '"+op+"' est: "+str(s))    
    f.close

# Programme principal à compléter
app=QApplication([])
w = loadUi ("Interface_Consultation.ui")
w.show()
w.bt1.clicked.connect(consulter)
app.exec()
