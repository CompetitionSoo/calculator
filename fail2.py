
# ch 4.2.3 main.py
import sys # 시스템 제어 관련 모듈

# 위젯이란 : GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox,)

from PyQt5.QtGui import QIcon # Icon을 추가하기 위한 라이브러리
# 나는 계산기 유형을 직접 정의한다. 이때 Qwidget에 기반을 둔다
class Calculator(QWidget) :

    def __init__(self) :
        super().__init__() # 뭔가에 기반을 들 경우 써줘야하는 코드
        self.initUI()

    def initUI(self) :

        self.te1 = QApplication()
        self.te1.setReadOnly(True)
           
        self.btn1=QPushButton('Message', self)

        self.btn1.clicked.connect(self.activateMessage) # 버튼 클릭시 핸들러 함수 연결

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 추가
        vbox.addWidget(self.btn1) # 버튼위치
        vbox.addStretch(1)
        
        self.setLayout(vbox) # 설정 적용

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

        def activateMessage(self) :
            #QMessageBox.information(self,"information" , "Button clicked!")
            self.te1.appendPlainText("Button clickied!")

# 클래스를 정의했으니, 여기에서 실행하겠다... 라는 실행부!
# if__name__=='__main__' : 이 모듈이 직접 실행되는 경우
if __name__=='__main__' :
    app = QApplication(sys.argv) # Qt 프로그램 실행코드
    view = Calculator()  # 내가만든 계산기 GUI 생성코드
    sys.exit(app.exec_()) # 계산기 종료시 시스템 종료 명령
