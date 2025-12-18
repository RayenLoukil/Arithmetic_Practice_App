from PyQt5.QtWidgets import *
from PyQt5.uic import *
from random import *
from pickle import dump,load

nph="evaluation.dat"
f = open(nph,"wb")
f.close
enr = dict(id=str , exp=str , rep=str , valid=str)

def verifid(id):
    '''cette fonction permet de vérifier si l’identifiant saisi
        par l’élève est formé par 8 chiffres '''
    return (id.isdecimal() and len(id)==8 )

def oper(ch):
    if ch.find("+")!=-1:
        return "+"
    elif ch.find("-")!=-1:
        return "-"
    else:
        return "*"
    
def evaluer(ch):
    op=oper(ch)
    s=int(ch[:ch.find(op)])
    p=int(ch[:ch.find(op)])
    ch = ch[ch.find(op)+1:]
    ch=ch+op
    while ch!="":
        if op== "+": 
            s=s+int(ch[:ch.find(op)])
        elif op=="-":
            s=s-int(ch[:ch.find(op)])
        else:
            p=p*int(ch[:ch.find(op)])
        ch = ch[ch.find(op)+1:]
        
    if op=="*" : return str(p)
    else : return str(s)


def valide():
    id=w.id.text()
    gen=w.gen.text()
    sais=w.sais.text()
    if not verifid(id) :
        QMessageBox.critical(w,'Erreur',"Veuillez saisir un identifiant valide composé de 8 chiffres")
    elif sais=="":
        QMessageBox.critical(w,'Erreur',"Veuillez saisir un reponse")
    else:
        if sais == evaluer(gen):
            w.verif.setText("reponse correcte")
            valid="vrai"
        else:
            w.verif.setText("reponse eronne")
            valid="faux"
        
        f = open(nph,"ab")
        e = dict(enr)
        e['id'] = id
        e['exp'] = gen
        e['rep'] = sais
        e['valid'] = valid
        dump(e,f)
        f.close
    
def generer():
    '''cette fonction permet de générer aléatoirement une expression arithmétique à partir du
        fichier "Expressions.txt".'''
    
    f = open("Expressions.txt","r")
    n = randint(1,20) #20 représente le nombre d'expressions contenues dans le fichier Expressions.txt
    for i in range (n) :
        e = f.readline()   
    f.close()
    return e
    
def afficher ():
    '''ce module permet d'afficher dans le label labExp une expression générée aléatoirement dans le cas
         où l'identifiant saisi est valide'''
    id = w.id.text()
    if not verifid(id) :
        QMessageBox.critical(w,'Erreur',"Veuillez saisir un identifiant valide composé de 8 chiffres")
    else :
        e = generer()
        w.gen.setText(e)



#Programme principal
app=QApplication([])
w = loadUi ("Interface_Evaluation.ui")
w.show()
w.bt1.clicked.connect(afficher)
w.bt2.clicked.connect(valide)
app.exec()
