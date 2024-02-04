from typing import TypedDict, Any, List

from PySide6.QtCore import QRect, QPropertyAnimation, QSize, QTimer, Qt, Signal, QPoint, QEvent, QEasingCurve, Property
from PySide6.QtGui import QShowEvent, QIcon, QColor, QPainterPath, QPainter, QBrush, QPen, QTextOption, QEnterEvent, \
    QMouseEvent, QFont
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect, QPushButton, QHBoxLayout

from ..LineEdit.SimpleLineEdit import SimpleLineEdit_1
from ...layout.RVBoxLayout import VBoxLayoutManager
from ....common.icon.raw_icon import icon as icon


class ComboBoxItem(TypedDict):
    text: str
    icon: QIcon
    data: Any


class ComboBoxItemWidget(QWidget):
    def __init__(self, parent=None, index: int = 0, text: str = "", icon: QIcon = QIcon(), icon_size: QSize = QSize()):
        super().__init__(parent)

        self.isHover = False
        self.isPressed = False

        self.text = text
        self.icon = icon
        self.index = index
        self.icon_size = icon_size

        self.color_font = QColor(0, 0, 0)
        self.hover_color = QColor(0, 0, 0, 35)
        self.border_color = QColor(0, 129, 140)
        self.background_color = QColor(255, 255, 255)

        self.curr_index = 0
        self.border_radius = 3

    def setParams(self, border_radius: int = 3,
                  color_font: QColor = QColor(0, 0, 0),
                  hover_color: QColor = QColor(0, 0, 0, 35),
                  border_color: QColor = QColor(0, 129, 140),
                  background_color: QColor = QColor(255, 255, 255),
                  ):
        self.border_radius = border_radius

        self.color_font = color_font
        self.hover_color = hover_color
        self.border_color = border_color
        self.background_color = background_color

    def paintEvent(self, event):
        super().paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.__drawBackground(painter)
        self.__drawText(painter)

    def __getLeftRect(self) -> QRect:
        left_rect_size = QSize(self.icon_size.width(), self.height())
        left_rect = QRect(QPoint(0, 0), left_rect_size)
        return left_rect

    def __drawText(self, painter: QPainter):
        painter.save()
        left_rect = self.__getLeftRect()
        text_rect = QRect(left_rect.width(), 0, self.width() - left_rect.width(), self.height()).adjusted(8, 0, 0, 0)

        pen = QPen()
        pen.setColor(self.color_font)
        painter.setPen(pen)

        painter.setFont(self.font())
        textOption = QTextOption(Qt.AlignLeft | Qt.AlignVCenter)
        painter.drawText(text_rect, self.text, textOption)

        painter.restore()

    def __drawBackground(self, painter: QPainter):
        painter.save()
        if self.isHover:
            painter.setBrush(self.hover_color)
            painter.drawRect(self.rect())
        else:
            painter.setBrush(self.background_color)
            painter.drawRect(self.rect())

        if self.curr_index == self.index:
            pen = QPen()
            pen.setWidth(2)
            pen.setColor(self.border_color)
            painter.setPen(pen)
            painter.drawLine(QPoint(2, 5), QPoint(2, self.height() - 5))
        painter.restore()

    def enterEvent(self, event: QEnterEvent) -> None:
        self.isHover = True
        self.update()

    def leaveEvent(self, event: QEvent) -> None:
        self.isHover = False
        self.update()

    def setCurrIndex(self, index: int):
        self.curr_index = index
        self.update()


class ComboBoxEditer(SimpleLineEdit_1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParams(anim_start_color=QColor(255, 255, 255),
                       anim_finish_color=QColor(255, 255, 255),
                       font_color=QColor(10, 10, 10))


class ComboBoxPopWidget(QWidget):
    pop_hide_signal = Signal()
    pop_show_signal = Signal()

    trigger_signal = Signal(int)
    update_curr_index_signal = Signal(int)

    def __init__(self, parent=None, curren_index: int = 0, item_spacing: int = 0):
        super().__init__(parent)

        self.border_radius = 5
        self.is_show_status = False
        self.spacing = item_spacing
        self.items: List[ComboBoxItem] = []
        self.currentIndex: int = curren_index
        self.color_background = QColor(255, 255, 255)

        self.pop_hide_signal.connect(self.hide)
        self.pop_show_signal.connect(self.show)

        self.__ui_config()

    def __ui_config(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(2, 2)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(20, 20, 20, 30))
        self.setGraphicsEffect(shadow)

        self.geometryManager = VBoxLayoutManager(self, self.spacing,
                                                 (self.spacing, self.spacing, self.spacing, self.spacing))

    def paintEvent(self, event):
        super().paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.__drawBackground(painter)

    def __drawBackground(self, painter: QPainter):
        painter.save()
        painter.setBrush(self.color_background)
        painter.drawRect(self.rect())
        painter.restore()

    def __animShow(self):
        self.anim_show = QPropertyAnimation(self, b'geometry')
        self.anim_show.setEasingCurve(QEasingCurve.OutQuad)
        self.anim_show.setStartValue(QRect(self.pos(), QSize(self.width(), 0)))
        self.anim_show.setEndValue(QRect(self.pos(), QSize(self.width(), self.height())))
        self.anim_show.setDuration(200)
        self.anim_show.start()

    def mousePressEvent(self, e: QMouseEvent):
        super().mousePressEvent(e)
        w = self.childAt(e.position().toPoint())
        if isinstance(w, ComboBoxItemWidget):
            self.trigger_signal.emit(w.index)
            self.update_curr_index_signal.emit(w.index)

    def leaveEvent(self, event) -> None:
        self.pop_hide_signal.emit()

    def showEvent(self, event: QShowEvent) -> None:
        self.geometryManager.calculateCenterePositions()
        QTimer.singleShot(1, lambda: self.__animShow())
        super().showEvent(event)

    def hide(self) -> None:
        super().hide()
        self.deleteLater()


class ComboBoxWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pop_widget = None
        self.items_params = ()

        self.item_spacing = 3
        self.item_height = 25
        self.border_radius = 5
        self.background_color = QColor(255, 255, 255)

        self.count: int = 0
        self._curr_index: int = 0
        self._curr_text: str = ""
        self.placeholder_text: str = ""
        self.items: List[ComboBoxItem] = []

        self.__ui_init()
        self.topLevelWidget().installEventFilter(self)

    def setParams(self, border_radius: int = 5,
                  background_color: QColor = QColor(255, 255, 255)
                  ):
        self.border_radius = border_radius
        self.background_color = background_color

    def setItemParams(self, border_radius: int = 3,
                      item_spacing=3,
                      item_height=25,
                      color_font: QColor = QColor(0, 0, 0),
                      color_hover: QColor = QColor(0, 0, 0, 35),
                      color_border: QColor = QColor(0, 129, 140),
                      color_background: QColor = QColor(255, 255, 255),
                      ):
        self.items_params = (border_radius, color_font, color_hover, color_border, color_background)
        self.item_spacing = item_spacing
        self.item_height = item_height

    def __ui_init(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(2, 2)
        shadow.setBlurRadius(10)
        shadow.setColor(QColor(20, 20, 20, 30))
        self.setGraphicsEffect(shadow)

        icon = QIcon()
        icon.addFile(":/icon/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.button = QPushButton(self)
        self.button.setIcon(icon)
        self.button.clicked.connect(self.__pop_widget_show)
        self.button.setStyleSheet("QPushButton { border: none; }")

        self.editer = ComboBoxEditer(self)
        self.editer.setEnabled(False)
        self.editer.setMouseTracking(True)

        self.hbox = QHBoxLayout(self)
        self.hbox.setSpacing(0)
        self.hbox.setContentsMargins(3, 1, 3, 1)
        self.hbox.addWidget(self.editer)
        self.hbox.addWidget(self.button)

    def __getItemSize(self):
        return QSize(self.width() - 8, self.item_height)

    def __pop_widget_show(self):
        if self.pop_widget or not len(self.items):
            return
        pos = self.mapTo(self.topLevelWidget(), QPoint(0, 0))

        x = pos.x()
        w = self.width()
        y = pos.y() + self.height() + 5
        h = len(self.items) * (self.__getItemSize().height() + self.item_spacing) + self.item_spacing

        self.pop_widget = ComboBoxPopWidget(self.topLevelWidget(), self._curr_index, self.item_spacing)
        self.pop_widget.setGeometry(x, y, w, h)
        self.__addItemsToPopWidget(self.pop_widget)
        self.pop_widget.pop_hide_signal.connect(self.__popWidgetDel)
        self.pop_widget.trigger_signal.connect(self.__onTriggerSignal)

        self.pop_widget.pop_show_signal.emit()

    def __addItemsToPopWidget(self, pop_widget: ComboBoxPopWidget):
        for index in range(len(self.items)):
            item_widget = ComboBoxItemWidget(pop_widget, index=index, text=self.items[index]["text"],
                                             icon=self.items[index]["icon"], icon_size=QSize(0, 0))
            item_widget.setParams(*self.items_params)
            item_widget.curr_index = self._curr_index
            item_widget.resize(self.__getItemSize())
            pop_widget.geometryManager.addWidget(item_widget)
            pop_widget.update_curr_index_signal.connect(item_widget.setCurrIndex)

    def __popWidgetDel(self):
        self.pop_widget = None

    def __onTriggerSignal(self, index: int):
        self._curr_index = index
        self._curr_text = self.items[index]["text"]
        self.editer.setText(self.items[index]["text"])

    def __drawBackground(self, painter: QPainter):
        painter.save()
        brush = QBrush(self.background_color)
        painter.setBrush(brush)
        painter.drawRect(self.rect())
        painter.restore()

    def paintEvent(self, event) -> None:
        super().paintEvent(event)

        path = QPainterPath()
        path.addRoundedRect(self.rect(), self.border_radius, self.border_radius)

        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setClipPath(path)
        painter.setRenderHint(QPainter.Antialiasing)

        self.__drawBackground(painter)


    def itemText(self, index: int) -> str:
        return self.items[index]["text"]

    def itemData(self, index: int) -> Any:
        return self.items[index]["data"]

    def itemIcon(self, index: int) -> QIcon:
        return self.items[index]["icon"]

    def addItem(self, icon: QIcon, text: str, data) -> None:
        item: ComboBoxItem = {"text": text, "icon": icon, "data": data}
        self.items.append(item)

    def addItems(self, items: List[str]) -> None:
        for item in items:
            item_temp: ComboBoxItem = {"text": item, "icon": QIcon(), "data": 0}
            self.items.append(item_temp)
        if not self._curr_text and len(self.items):
            self.editer.setText(self.items[0]["text"])

    def clear(self):
        self.items.clear()

    def showEvent(self, event) -> None:
        super(ComboBoxWidget, self).showEvent(event)
        if len(self.items):
            self.__onTriggerSignal(0)

        h = self.height()
        self.button.resize(h+2, h)
        self.editer.resize(self.width()-h-2, h)

    def setFont(self, font: QFont) -> None:
        self.editer.setFont(font)
        self.button.setFont(font)

    def setItemHeight(self, h: int):
        self.item_height = h

    def curr_text(self):
        return self._curr_text

    def curr_index(self):
        return self._curr_index

    def eventFilter(self, obj, event:QEvent):
        if self.pop_widget:
            if (not obj == self.pop_widget) and event.type() == QEvent.MouseButtonRelease:
                self.pop_widget.pop_hide_signal.emit()
        return super().eventFilter(obj, event)
