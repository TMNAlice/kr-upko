# activate pqt5
# py.test -s guitest.py
from PyQt5 import QtCore
from maingui import AStarWindow
import pytest
import pytestqt


def test_gui(qtbot):
    window = AStarWindow()
    window.show()
    qtbot.addWidget(window)
    qtbot.keyClick(window.spinBoxHeight, QtCore.Qt.Key_Delete)
    qtbot.keyClick(window.spinBoxHeight, "4")
    qtbot.wait(500)
    qtbot.keyClick(window.spinBoxWidth, QtCore.Qt.Key_Delete)
    qtbot.keyClick(window.spinBoxWidth, "4")
    qtbot.wait(500)
    qtbot.keyClicks(window.plainTextEditStart, "(1, 1)")
    qtbot.wait(500)
    qtbot.keyClicks(window.plainTextEditGoal, "(3, 1)")
    qtbot.wait(500)
    weights = "{(0, 0): 2, (0, 1): 3, (0, 2): 1, (0, 3): 6, (1, 0): 7, (1, 1): 8, (1, 2): 5, (1, 3): 2, (2, 0): 3, (2, 1): 4, (2, 2): 3, (2, 3): 2, (3, 0): 1, (3, 1): 2, (3, 2): 3, (3, 3): 4}"
    qtbot.keyClicks(window.plainTextEditWeights, weights)
    qtbot.wait(500)
    qtbot.keyClicks(window.plainTextEditWalls,
                    "[(0, 1), (1, 2), (2, 2), (3, 2)]")
    qtbot.wait(500)
    qtbot.mouseClick(window.pushButton, QtCore.Qt.LeftButton)
    assert window.plainTextEditPath.toPlainText() == '[(1, 1), (2, 1), (3, 1)]'
    qtbot.wait(500)
    window.plainTextEditStart.clear()
    window.plainTextEditGoal.clear()
    qtbot.keyClicks(window.plainTextEditStart, "(0, 0)")
    qtbot.wait(500)
    qtbot.keyClicks(window.plainTextEditGoal, "(2, 3)")
    qtbot.wait(500)
    qtbot.mouseClick(window.pushButton, QtCore.Qt.LeftButton)
    assert window.plainTextEditPath.toPlainText() == 'no way'
    qtbot.wait(500)
    qtbot.mouseClick(window.pushButton_2, QtCore.Qt.LeftButton)
    assert window.plainTextEditPath.toPlainText() == ''
    qtbot.wait(500)
