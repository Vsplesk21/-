from PyQt5.QtWidgets import * 
 
app = QApplication([]) 
app.setStyleSheet(""" 
    QWidget{     
             
            
            background-color: #66ff00;     
            border-style: outset;     
            font-family: Roboto;     
            border-width: 2px;     
            border-radius: 13px;     
            border-color: black;     
            font: bold 12px;     
            min-width: 2em;     
            padding: 6px; 
        } 
    """) 
 
 
 
 
lobbi = QWidget() 
lobbi.resize(1200,800) 
lobbi.setWindowTitle("Доганялки") 
 
shopbtn = QPushButton("Магазин") 
playbtn = QPushButton("Грати") 
 
 
 
 
shopline = QVBoxLayout() 
playline = QVBoxLayout() 
lobbiline = QHBoxLayout() 
playline.addWidget(playbtn) 
shopline.addWidget(shopbtn) 
 
 
lobbiline.addLayout(shopline) 
lobbiline.addLayout(playline) 
lobbi.setLayout(lobbiline) 
lobbi.show() 
app.exec_()