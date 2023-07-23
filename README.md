# QT-组件 QT-material-widgets
🎨 Qt widgets-based implementation of the Material Design specification.😊

## 内容列表
- [组件列表](#组件列表)
    - [滑动侧边栏](#滑动侧边栏)
- [联系方式](#联系方式)

# 滑动侧边栏
## 1.custom_btn.py
### 功能
- 按钮颜色动画
- 图标与文字分离
### 说明
1. 你可以在初始化的时候，为按钮添加文字和图标
2. 如果你需要修改，按钮样式，你需要到MyFrame.ui()中修改样式表。当然，你也可以在实例化之后，设置样式表。
   - 注意:QFrame和QPushBUtton的背景颜色要一致，同时也要修改MyFrame._color_1的颜色。
   - 当然，如果你觉得麻烦，那就别改🤣。或者写一个方法，在初始化的时候，提取样式表的颜色，然后再配置到MyFrame._color_1。
3. 在MyFrame.lableAnimation(),你可以修改动按钮的变化颜色。

## 2.main.py
### 功能
- 功能栏向两中间伸缩
- 收缩后，按钮会显示出圆角，而不是左圆右方
- 伸缩后，按钮的文字会消失
### 说明
- 在main.config_init(),可以修改变化后的伸缩栏宽度和按钮宽度，以达到更加美观的效果😌


# 联系方式
- Email:2731491939@qq.com
- CsdnBlog:Rev_RoastDuck
