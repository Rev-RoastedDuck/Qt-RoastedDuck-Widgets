"""
Qt-RoastedDuck-Widgets
======================
Qt widgets-based implementation of the Material Design specification.

Repository at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets.

Demo are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/Demo.

Examples are available at https://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/examples.

Information:
    WeChat: Roast_71.
    csdnBlog: https://blog.csdn.net/m0_72760466?type=blog.

:copyright: (c) 2023 by Rev-RoastedDuck.
:license: GPLv3, see LICENSE for more details.
"""

from PySide6.QtWidgets import QWidget

class VBoxLayoutManager():
    def __init__(self, parent: QWidget, spacing, margins):
        self.widgets = []
        self.parent = parent
        self.spacing = spacing
        self.margins = margins

    def addWidget(self, widget):
        self.widgets.append(widget)

    def calculatePositions(self):
        """ 左对齐显示 """
        x = self.margins[1]
        y = self.margins[0]
        for widget in self.widgets:
            widget.move(x, y)
            y += widget.height() + self.spacing

    def calculateCenterePositions(self):
        """ 居中显示 """
        y = self.margins[0]
        for widget in self.widgets:
            x = (self.parent.width() - widget.width()) // 2
            widget.move(x, y)
            y += widget.height() + self.spacing

    def getContentsMargins(self):
        return self.margins