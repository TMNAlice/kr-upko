from PyQt5 import QtWidgets
import sys
from ast import literal_eval
from graph_a_star import GraphWithWeights
from lab5_ui import Ui_MainWindow


class AStarWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.a_star_caller)
        self.pushButton_2.clicked.connect(self.clr)

    def a_star_caller(self):
        self.plainTextEditPath.clear()
        for widget in self.widget.children():
            if isinstance(widget, QtWidgets.QPlainTextEdit):
                if not widget.toPlainText():
                    self.plainTextEditPath.setPlainText("check values")
                    return
        if not self.plainTextEditWeights.toPlainText():
            self.plainTextEditPath.setPlainText("check values")
            return
        if not self.plainTextEditWalls.toPlainText():
            self.plainTextEditPath.setPlainText("check values")
            return
        h = int(self.spinBoxHeight.text())
        w = int(self.spinBoxWidth.text())
        start = literal_eval(self.plainTextEditStart.toPlainText())
        goal = literal_eval(self.plainTextEditGoal.toPlainText())
        weights = literal_eval(self.plainTextEditWeights.toPlainText())
        walls = literal_eval(self.plainTextEditWalls.toPlainText())
        graph = GraphWithWeights(w, h, weights, walls)
        path = graph.a_star(start, goal)
        self.plainTextEditPath.setPlainText(str(path))

    def clr(self):
        for widget in self.centralwidget.children():
            if isinstance(widget, QtWidgets.QPlainTextEdit):
                widget.clear()
        for widget in self.widget.children():
            if isinstance(widget, QtWidgets.QPlainTextEdit):
                widget.clear()
        self.spinBoxHeight.setValue(1)
        self.spinBoxWidth.setValue(1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AStarWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
