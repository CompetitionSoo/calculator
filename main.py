# ch 4.2.1 main.py
import sys # 시스템 제어 관련 모듈

# 위젯이란 : GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import QApplication, QWidget

# 나는 계산기 유형을 직접 정의한다. 이때 Qwidget에 기반을 둔다
class Calculator(QWidget) :

    def __init__(self) :
        super().__init__() # 뭔가에 기반을 들 경우 써줘야하는 코드
        self.inituI()

    def inituI(self) :
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show()

# 클래스를 정의했으니, 여기에서 실행하겠다... 라는 실행부!
# if__name__=="__main__" : 이 모듈이 직접 실행되는 경우
if __name__=="__main__" :
    app = QApplication(sys.argv) # Qt 프로그램 실행코드
    view = Calculator()  # 내가만든 계산기 GUI 생성코드
    sys.exit(app.exec_()) # 계산기 종료시 시스템 종료 명령
