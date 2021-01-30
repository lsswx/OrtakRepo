#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#deneme3

from PyQt5.QtWidgets import * 
import sys 


class Window(QDialog): 
    def __init__(self): 
        super(Window, self).__init__() 
        self.setWindowTitle("Python") 
        self.setGeometry(100, 100, 300, 400) 
        self.formGroupBox = QGroupBox("Form 1") 
        self.ageSpinBar = QSpinBox()  
        self.degreeComboBox = QComboBox() 
        self.degreeComboBox.addItems(["Elektrik-elektronik", "Data-sicence",  "BIOMEDICAL-ENGINEERING" , ]) 
        self.nameLineEdit = QLineEdit() 
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        self.buttonBox.rejected.connect(self.reject)  
        mainLayout = QVBoxLayout() 
        mainLayout.addWidget(self.formGroupBox) 
        mainLayout.addWidget(self.buttonBox) 
        self.setLayout(mainLayout) 
        self.close() 
  
    def createForm(self): 
  
        layout = QFormLayout() 
  
        layout.addRow(QLabel("Kullanıcı adı "), self.nameLineEdit) 
  
        layout.addRow(QLabel("Tercih edilen iş "), self.degreeComboBox) 
  
        layout.addRow(QLabel("Yaş"), self.ageSpinBar) 
  
        self.formGroupBox.setLayout(layout) 
    

def mclick():
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")
        
            
            
    
if __name__ == '__main__': 
  
    app = QApplication(sys.argv) 
    window = Window() 
    btn.clicked.connect(mclick)
    window.show() 
    sys.exit(app.exec()) 


# In[ ]:





# In[ ]:




