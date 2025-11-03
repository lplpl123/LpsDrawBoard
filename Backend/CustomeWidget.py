from PyQt5.Qt import *
from PyQt5.QtCore import Qt, pyqtSignal


class MyWindow(QWidget):
    clicked = pyqtSignal()


    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.drag:
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if self.drag and event.button() == Qt.LeftButton:
            self.drag = False


class MyQLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
                            QWidget{
                            font-family: "微软雅黑";}
                            """)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:  # 判断左键按下
            self.clicked.emit()


class MyColorWindow(QColorDialog):
    def __init__(self, parent=None):
        super(MyColorWindow, self).__init__(parent)

    def closeEvent(self, a0):
        self.hide()


class DrawLable(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    def __init__(self, parent):
        super(DrawLable, self).__init__(parent)
        self.pixmap = QPixmap(250, 400)  # 考虑边框的间距 减去px
        self.pixmap.fill(Qt.white)
        self.setStyleSheet("border: 2px solid red")
        self.Color = Qt.blue  # pen color: defult:blue
        self.penwidth = 4  # pen width : default:4

    def paintEvent(self, event):
        # super().paintEvent(event)

        painter = QPainter(self.pixmap)
        painter.setPen(QPen(self.Color, self.penwidth, Qt.SolidLine))
        painter.drawLine(self.x0, self.y0, self.x1, self.y1)

        Label_painter = QPainter(self)
        Label_painter.drawPixmap(2, 2, self.pixmap)

    def mousePressEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()
        self.flag = True

    def mouseMoveEvent(self, event):
        if self.flag:
            self.x0 = self.x1
            self.y0 = self.y1
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        self.flag = False




