from PyQt5.QtWidgets import * 
import sys 


class Window(QDialog): 
    def __init__(self): 
        super(Window, self).__init__() 
        self.setWindowTitle("Python") 
        self.setGeometry(100, 100, 300, 400)         
        self.createForm1()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.rejected.connect(self.reject)  

        # Bu satırın altındaki kod ile createForm2 isminde ki fonksiyonu ok e basıldığında çağırdım
        self.buttonBox.accepted.connect(self.createForm2)

        mainLayout = QVBoxLayout() 
        mainLayout.addWidget(self.formGroupBox) 
        mainLayout.addWidget(self.buttonBox) 
        self.setLayout(mainLayout) 
        
  
    def createForm1(self): 
        self.formGroupBox = QGroupBox("Form 1") 
        self.ageSpinBar = QSpinBox()  
        self.degreeComboBox = QComboBox() 
        self.degreeComboBox.addItems(["Elektrik-elektronik", "Data-sicence",  "BIOMEDICAL-ENGINEERING" , ]) 
        self.nameLineEdit = QLineEdit()   
        layout = QFormLayout() 
  
        layout.addRow(QLabel("Kullanıcı adı "), self.nameLineEdit) 
  
        layout.addRow(QLabel("Tercih edilen iş "), self.degreeComboBox) 
  
        layout.addRow(QLabel("Yaş"), self.ageSpinBar) 
  
        self.formGroupBox.setLayout(layout) 
        
    # Bu fonksiyon ile yeni bir satır ekledim sen bunu farklı şekilde işler yaptırabilirsin mesela yeni bir pencere açtırmak gibi
    def createForm2(self): 
        self.formGroupBox2 = QGroupBox("Form 2") 
        self.nameLineEdit = QLineEdit()   
        layout = self.formGroupBox.layout() 
  
        layout.addRow(QLabel("Yeni Kullanıcı adı "), self.nameLineEdit) 
            

if __name__ == '__main__': 
  
    app = QApplication(sys.argv) 
    window = Window() 
    window.show() 
    sys.exit(app.exec()) 