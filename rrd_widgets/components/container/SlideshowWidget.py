from PySide6.QtCore import QTimer, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QRect, QSize, QEvent, \
    QPoint, QRegularExpression, Qt, Signal
from PySide6.QtGui import QPixmap, QIcon, QPainterPath, QPainter, QResizeEvent
from PySide6.QtWidgets import  QPushButton, QLabel, QWidget, QSizePolicy, QButtonGroup, QHBoxLayout
from ...common import icon_slider_show as icon

class PixmapLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super(PixmapLabel, self).__init__(*args, **kwargs)
        self.pixmap_backup = None


    def setStyleSheet(self, styleSheet: str) -> None:
        super(QLabel, self).setStyleSheet(styleSheet)

        radius_match = QRegularExpression(r"border-radius:(?P<border_radius>\d+)px")
        radius_result = radius_match.match(styleSheet)
        if radius_result.hasMatch():
            self.border_radius = int(radius_result.captured("border_radius"))

    def __revPixmap(self, pixmap: QPixmap) -> QPixmap:
        cropped_pixmap = self.__crop_image_with_ratio(pixmap, self.width(), self.height())
        scaled_pixmap = self.__scale_pixmap(cropped_pixmap, self.width(), self.height())

        rounded_pixmap = QPixmap(scaled_pixmap.size())
        rounded_pixmap.fill(Qt.transparent)

        rounded_rect = QPainterPath()
        rounded_rect.addRoundedRect(rounded_pixmap.rect(), self.border_radius, self.border_radius)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setClipPath(rounded_rect)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()

        return rounded_pixmap

    def resizeEvent(self, event: QResizeEvent) -> None:
        """label缩小时，即时调整图片大小"""
        super(PixmapLabel, self).resizeEvent(event)
        if self.pixmap_backup is not None:
            pixmap = self.pixmap_backup
            pixmap = self.__revPixmap(pixmap)
            pixmap = self.__scale_pixmap(pixmap, self.width(), self.height())

            super(PixmapLabel, self).setPixmap(pixmap)

    def setPixmap(self, pixmap: QPixmap, fun_count: int = 0) -> None:
        """设置图片"""
        if self.pixmap() is not None:
            self.pixmap_backup = pixmap
        pixmap = self.__revPixmap(pixmap)
        super(PixmapLabel, self).setPixmap(pixmap)

    def __scale_pixmap(self, pixmap: QPixmap, width: int, height: int) -> QPixmap:
        """缩放图片"""
        original_width = pixmap.width()
        original_height = pixmap.height()

        scale_factor = max(width / original_width, height / original_height)

        scaled_pixmap = pixmap.scaled(original_width * scale_factor, original_height * scale_factor)

        return scaled_pixmap

    def __crop_image_with_ratio(self, pixmap: QPixmap, width: int, height: int) -> QPixmap:
        """切割图片"""
        target_ratio = width / height
        original_width = pixmap.width()
        original_height = pixmap.height()

        if original_width / original_height > target_ratio:
            new_width = int(original_height * target_ratio)
            x = int((original_width - new_width) / 2)
            y = 0
            new_height = original_height
        else:
            new_height = int(original_width / target_ratio)
            x = 0
            y = int((original_height - new_height) / 2)
            new_width = original_width

        cropped_pixmap = pixmap.copy(x, y, new_width, new_height)

        return cropped_pixmap

class ClickedButton(QPushButton):
    """按钮被点击后会变色"""
    def __init__(self,parent=None):
        super(ClickedButton, self).__init__(parent)

    def mousePressEvent(self, e) -> None:
        super(ClickedButton, self).mousePressEvent(e)
        self.setStyleSheet("QPushButton{\n"
                           "	border-radius:18px;\n"
                           "	background-color:rgba(204,51,51,200);\n"
                           "}\n")
    def mouseReleaseEvent(self, e) -> None:
        super(ClickedButton, self).mouseReleaseEvent(e)
        self.setStyleSheet("QPushButton{\n"
                           "	border-radius:18px;\n"
                           "	background-color: rgba(0, 0, 0, 100);\n"
                           "}\n")

class HoveredButton(QPushButton):
    """鼠标悬浮，携带id，发送信号"""
    hovered_signal = Signal(int)

    def __init__(self, id:int) -> None:
        super(HoveredButton, self).__init__()
        self.id = id

    def enterEvent(self, event) -> None:
        self.hovered_signal.emit(self.id)

class SliderNav(QWidget):
    """图片导航栏，鼠标悬浮导航栏的红点，会切换图片(通过发送信号实现)"""
    changePixmap_signal = Signal(int)
    changeColor_signal = Signal(int)

    def __init__(self, parent, button_num):
        super().__init__(parent)
        self.button_num = button_num
        self.button_size = 6

        self.ui()
        self.__signalConnect()
        self.__highlightButton()

    def ui(self):
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.button_group = QButtonGroup(self)
        layout = QHBoxLayout(self)
        layout.setSpacing(10)

        for id in range(self.button_num):
            button = HoveredButton(id)
            button.setFixedSize(self.button_size, self.button_size)
            button.hovered_signal.connect(self.buttonHoverEvent)
            button.setStyleSheet(
                f"QPushButton{{border-radius:{self.button_size // 2}px;background-color:rgba(0,0,0,50);}}QPushButton:hover{{border-radius:{self.button_size // 2}px;background-color:rgba(255,0,0,255)}}")
            self.button_group.addButton(button, id)
            layout.addWidget(button)

    def __signalConnect(self):
        self.changeColor_signal.connect(self.changeColor)

    def buttonHoverEvent(self,id:int) -> None:
        self.changePixmap_signal.emit(id)

    def changeColor(self, button_id: int):
        for id in range(self.button_num):
            button = self.button_group.button(id)
            button.setStyleSheet(
                f"QPushButton{{border-radius:{self.button_size // 2}px;background-color:rgba(0,0,0,50);}}")

        button = self.button_group.button(button_id)
        button.setStyleSheet(
            f"QPushButton{{border-radius:{self.button_size // 2}px;background-color:rgba(255,0,0,255);}}")

    def __highlightButton(self):
        """m默认让中间的按钮高亮"""
        self.changeColor_signal.emit(1)

class SlideShowWidget(QWidget):
    def __init__(self, parent, middel_widget_size: QSize, lr_widget_size: QSize, *args, **kwargs):
        super(SlideShowWidget, self).__init__(parent, *args, **kwargs)
        self.middel_widget_size = middel_widget_size
        self.lr_widget_size = lr_widget_size
        self.imageList: list[QPixmap] = []

    def uiInit(self) -> None:
        self.setObjectName("frame")
        self.setStyleSheet(u"#frame{\n"
                           "	background-color: rgba(255, 25, 25,0);\n"
                           "}\n"
                           "QPushButton{\n"
                           "	border-radius:18px;\n"
                           "	background-color: rgba(0, 0, 0, 50);\n"
                           "}\n"
                           )

        self.label_1 = PixmapLabel(self)
        self.label_1.setObjectName(u"label_2")
        self.label_1.resize(self.lr_widget_size)
        self.label_1.setStyleSheet("#label_2{\n"
                                   "	border-radius:13px;\n"
                                   "	background-color: rgba(255, 255, 0,0);\n"
                                   "\n"
                                   "}"
                                   )

        self.label_3 = PixmapLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.resize(self.lr_widget_size)
        self.label_3.setStyleSheet("#label_3{\n"
                                   "	border-radius:13px;\n"
                                   "	background-color: rgba(255, 255, 0,0);\n"
                                   "\n"
                                   "}"
                                   )

        self.label_2 = PixmapLabel(self)
        self.label_2.setObjectName(u"label")
        self.label_2.setGeometry(QRect(210, 0, 500, 200))
        self.label_2.resize(self.middel_widget_size)
        self.label_2.setStyleSheet("#label{\n"
                                   "	border-radius:13px;\n"
                                   "	background-color: rgba(255, 255, 0,0);\n"
                                   "\n"
                                   "}"
                                   )

        if True:
            self.pushButton_l = ClickedButton(self)
            self.pushButton_l.setObjectName(u"pushButton_l")
            self.pushButton_l.setGeometry(QRect(82, 80, 36, 36))
            icon = QIcon()
            icon.addFile(u":/icon/icon_png/\u540e\u9000 (1).png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton_l.setIcon(icon)
            self.pushButton_l.setIconSize(QSize(18, 18))
            self.pushButton_l.clicked.connect(lambda: self.__animationStartButton(is_forward=False))

            self.pushButton_r = ClickedButton(self)
            self.pushButton_r.setObjectName(u"pushButton_r")
            self.pushButton_r.setGeometry(QRect(803, 80, 36, 36))
            icon1 = QIcon()
            icon1.addFile(u":/icon/icon_png/\u524d\u8fdb (1).png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton_r.setIcon(icon1)
            self.pushButton_r.setIconSize(QSize(18, 18))
            self.pushButton_r.clicked.connect(lambda: self.__animationStartButton(is_forward=True))

            self.pushButton_l.hide()
            self.pushButton_r.hide()

        # 导航栏
        self.nav = SliderNav(self, len(self.imageList))
        self.nav.changePixmap_signal.connect(self.toggleImageHoverEvent)
        self.button_group = self.nav.button_group

    def __animationParmas(self) -> None:
        self.mLabelListIndex = 1  # 标记中间的label
        self.imageListIndex_m = 1  # 指示中间的图片在imageList的位置
        self.animation_triggered = False  # 用于触发__onAnimationValueChanged()
        self.labelList = [self.label_1, self.label_2, self.label_3]
        self.posList = []

        self.animation_time = 450  # 动画时间
        self.timer_interval = 2000  # 动画间隔时间

        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(self.timer_interval)
        self.timer.timeout.connect(lambda: self.__animationStart(is_forward=True))

    def __animationCreat(self, is_forward: bool) -> None:
        self.animation_ground = QParallelAnimationGroup()

        animation_1 = QPropertyAnimation(self.label_1, b"geometry")
        animation_1.setEasingCurve(QEasingCurve.OutQuad)
        animation_1.setDuration(self.animation_time)
        animation_1.setEndValue(self.posList[0])

        animation_2 = QPropertyAnimation(self.label_2, b"geometry")
        animation_2.setEasingCurve(QEasingCurve.OutQuad)
        animation_2.setDuration(self.animation_time)
        animation_2.setEndValue(self.posList[1])

        animation_3 = QPropertyAnimation(self.label_3, b"geometry")
        animation_3.setEasingCurve(QEasingCurve.OutQuad)
        animation_3.setDuration(self.animation_time)
        animation_3.setEndValue(self.posList[2])

        self.animation_ground.addAnimation(animation_1)
        self.animation_ground.addAnimation(animation_2)
        self.animation_ground.addAnimation(animation_3)

        animation_3.valueChanged.connect(
            lambda: self.__onAnimationValueChanged(is_forward=is_forward))  # 运行至1/2的时候，切换图片
        self.animation_ground.start()

    def __animationStartPre(self, is_forward: bool) -> None:
        """让中间图片顶层显示"""
        label_count = len(self.labelList)
        image_count = len(self.imageList)
        if is_forward:
            # 更新label的位置
            self.posList = [self.posList[-1]] + self.posList[:-1]
            # 更新中间Label对应的下标
            self.mLabelListIndex = (self.mLabelListIndex + 1) % label_count
            # 更新导航栏
            self.nav.changeColor_signal.emit((self.imageListIndex_m + 1) % image_count)
        elif not is_forward:
            self.posList = self.posList[1:] + [self.posList[0]]
            self.mLabelListIndex = (self.mLabelListIndex - 1) % label_count
            self.nav.changeColor_signal.emit((self.imageListIndex_m - 1) % image_count)
        self.labelList[self.mLabelListIndex].raise_()

    def __animationStart(self, is_forward: bool) -> None:
        self.animation_triggered = False
        self.__animationStartPre(is_forward=is_forward)
        self.__animationCreat(is_forward=is_forward)

    def __onAnimationValueChanged(self, is_forward: bool) -> None:
        """动画执行1/2时，切换图片，每动画只执行一次"""
        if not self.animation_triggered:
            progress = self.animation_ground.currentTime() / self.animation_ground.duration()
            if progress >= 0.5:
                self.__updatePixmap(is_forward)
                self.animation_triggered = True

    def __setPossion(self) -> None:
        """设置各个组件的位置"""
        # 中间frame居中显示
        label_2_x = (self.width() - self.label_2.width()) // 2
        label_2_y = (self.height() - self.label_2.height()) // 2

        # 两侧label，各占中间label的 1/3
        offset = self.label_2.width() // 3

        label_1_x = label_2_x - self.label_1.width() + offset
        label_1_y = (self.height() - self.label_1.height()) // 2

        label_3_x = label_2_x + self.label_2.width() - offset
        label_3_y = (self.height() - self.label_3.height()) // 2

        self.label_1.move(QPoint(label_1_x, label_1_y))
        self.label_2.move(QPoint(label_2_x, label_2_y))
        self.label_3.move(QPoint(label_3_x, label_3_y))

        # 按钮位于左右label外侧
        button_l_x = label_1_x
        button_l_y = (self.height() - self.pushButton_l.height()) // 2

        button_r_x = label_3_x + self.label_3.width() - self.pushButton_r.width()
        button_r_y = (self.height() - self.pushButton_r.height()) // 2

        self.pushButton_l.move(QPoint(button_l_x, button_l_y))
        self.pushButton_r.move(QPoint(button_r_x, button_r_y))

        # 导航栏
        nav_x = (self.width() - self.nav.width()) // 2
        nav_y = self.height() - self.nav.height()

        self.nav.move(nav_x, nav_y)

        self.posList = [self.label_1.geometry(), self.label_2.geometry(), self.label_3.geometry()]

    def addPixmap(self, pixmap: QPixmap) -> None:
        """添加图片"""
        self.imageList.append(pixmap)

    def setGeometry(self, *args) -> None:
        super(SlideShowWidget, self).setGeometry(*args)
        self.uiInit()
        self.__animationParmas()
        self.__pixmapInit()
        QTimer.singleShot(0, lambda: self.__setPossion())

    def enterEvent(self, event: QEvent) -> None:
        """鼠标悬停，停止切图，显示按钮"""
        super(SlideShowWidget, self).enterEvent(event)
        self.__buttonStatusChange(True)
        self.timer.stop()

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开，开始切图，隐藏按钮"""
        super(SlideShowWidget, self).leaveEvent(event)
        self.__buttonStatusChange(False)
        self.timer.start()

    def __buttonStatusChange(self, need_show: bool) -> None:
        """切换按钮显示状态"""
        if need_show:
            self.pushButton_r.raise_()
            self.pushButton_l.raise_()
            self.pushButton_l.show()
            self.pushButton_r.show()
        elif not need_show:
            self.pushButton_l.hide()
            self.pushButton_r.hide()

    def __pixmapInit(self) -> None:
        """初始化时，设置图片"""
        if self.label_2.pixmap().isNull():
            for index in range(3):
                self.labelList[index].setPixmap(self.imageList[index])

    def __updatePixmap(self, is_forward: bool = True) -> None:
        """更新label的图片"""
        image_count = len(self.imageList)
        label_count = len(self.labelList)

        if is_forward:
            self.imageListIndex_m = (self.imageListIndex_m + 1) % (image_count)
            self.labelList[(self.mLabelListIndex + 1) % label_count].setPixmap(self.imageList[(self.imageListIndex_m + 1) % image_count])
        else:
            self.imageListIndex_m = (self.imageListIndex_m - 1) % (image_count)
            self.labelList[(self.mLabelListIndex - 1) % label_count].setPixmap(self.imageList[(self.imageListIndex_m - 1) % image_count])

    def __animationStartButton(self, is_forward: bool) -> None:
        """按钮触发切换图片"""
        if is_forward:
            self.__animationStart(is_forward=is_forward)
        elif not is_forward:
            self.__animationStart(is_forward=is_forward)
        # 保持按钮位于最顶层
        self.pushButton_r.raise_()
        self.pushButton_l.raise_()

        # def toggleImageHoverEvent(self,id):
        """悬浮时，切换图片"""
        # print("---",id)

        # image_count = len(self.imageList)
        # self.imageListIndex_f = (id + 1) % image_count  # 最前面的图片位置 双指针定位
        # self.imageListIndex_r = (id - 1) % image_count  # 最后面的图片位置
        #
        # self.__animationForwardStartPre()
        # self.__animationInit(is_forward=True)
        # self.__setPixmap(id)
        # pass

    def toggleImageHoverEvent(self,id):
        pass