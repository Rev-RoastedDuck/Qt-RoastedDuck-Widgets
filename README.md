# QT-组件 QT-material-widgets
🎨 基于Qt小部件的实现😊

🎨 Qt widgets-based implementation of the Material Design specification.😊

## 内容列表
- [组件列表](#组件列表)
    - [滑动侧边栏](#滑动侧边栏)
    - [波纹按钮](#波纹按钮)
    - [流光按钮](#流光按钮)
    - [流光展示卡片](#流光展示卡片)
    - [发散按钮容器](#发散按钮容器)
    - [轮播图](#轮播图)
    - [ExpInput](#ExpInput)
    - [SimpleInput](#SimpleInput)
    - [SimpleButton](#SimpleButton)
    - [SwitchButton](#SwitchButton)
    - [Slider](#Slider)
- [联系方式](#联系方式)
- [声明](#声明)

<hr/>

# 滑动侧边栏
## 效果
![滑动侧边栏](./Demo/ScalableMenuBar.gif)
## 说明
1. 你可以在初始化的时候，为按钮添加文字和图标
2. 如果你需要修改，按钮样式，你需要到MyFrame.ui()中修改样式表。当然，你也可以在实例化之后，设置样式表
   - 注意:QFrame和QPushBUtton的背景颜色要一致，同时也要修改MyFrame._color_1的颜色
   - 当然，如果你觉得麻烦，那就别改🤣。或者写一个方法，在初始化的时候，提取样式表的颜色，然后再配置到MyFrame._color_1
3. 在MyFrame.lableAnimation(),你可以修改动按钮的变化颜色
4. 在main.config_init(),可以修改变化后的伸缩栏宽度和按钮宽度，以达到更加美观的效果😌

<hr/>

# 波纹按钮
## 效果
![波纹按钮](./Demo/WavyButton.gif)
## 说明
1. **styleSheet参数说明**📃
   - R-font-color: 配置按钮字体颜色
   - R-full-color: 配置按钮的填充颜色
2. 方法说明📃
   - RWavyButton.setIcon(): 设置按钮图标
   - RWavyButton.setFont(): 配置字体大小
   - RWavyButton.setText(): 设置按钮文字内容
3. ~~同样的，在配置完样式后，需要调用RWavyButton.setStyleSheetConfig()来使之生效~~
### 示例
```python
    # 按钮样式配置
    btn = RWavyButton(w)
    btn.setGeometry(QRect(290, 280, 110, 35))
    btn.setStyleSheet(u"#RWavyButton{"
                       "    background-color: rgb(46, 22, 177);"
                       "	border-radius:10px;"               # 设置圆角
                       "    R-full-color:rgb(255, 89, 0);"     # 设置填充颜色
                       "    R-font-color:rgb(255, 255, 255);"  # 设置字体颜色
                      "}"
                      )

    # 设置字体
    font = QFont()
    font.setPointSize(10)
    btn.setFont(font)

    # 填写文字内容
    btn.setText(" 会变色喔")

    # 设置图标
    icon = QIcon()
    icon.addFile(u":/\u56fe\u6807/\u56fe\u6807/\u4fdd\u5b58.png", QSize(24,24), QIcon.Normal, QIcon.Off)
    btn.setIcon(icon)

    # btn.setStyleSheetConfig()
```


<hr/>

# 流光按钮
## 效果
![流光按钮](./Demo/StreamerButton.gif)
## 说明
1. ~~**styleSheet参数说明**📃~~
   ~~- color:字体颜色~~
  ~~- Rborder-width:边框大小~~
2. ~~在初始化之后，你需要设置按钮的geometry参数~~
3. RPushButton.createGradient()中，你可以修改流光的颜色🎊
4. ~~你可以在RPushButton.animationConfig()种修改定时时间，来控制流光的速度~~
5. ~~**在styleSheet(样式表)，你可以通过设置Rborder-width，来配置按钮边框的宽度(流光的宽度)**~~
6. ~~配置完之后，需要调用RPushButton.setStyleSheetConfig()，使配置生效❗~~
7. ~~这个代码是经过优化的，可以直接调用，直接配置样式表和geometry就可以啦~~


<hr/>


# 流光展示卡片
## 效果
![流光展示卡片](./Demo/DynamicBorderFrame.gif)
## 说明
1. ~~老样子，你可以在styleSheet修改样式，之后需要调用DynamicBorderFrame.setStyleSheetConfig()使样式生效~~
2. **styleSheet参数说明**📃
   - Rcolor_1:流光的颜色1
   - Rcolor_2:流光的颜色2
   - border-radius:卡片圆角大小
   - Rborder-width:卡片的边框宽度
   - background-color:外层背景颜色
   - inside-background-color:里层背景颜色

<hr/>

# 发散按钮容器
## 效果
![发散按钮容器](./Demo/ExpandBox.gif)
## 说明
1. 参数说明📃
   - RExpandBox.locatorBoxSize: 定位组件的尺寸
   - RExpandBox.expandBoxWidgetSize: 伸缩组件的尺寸
   - RExpandBox.locatorBoxWidgetWidth: 定位按钮的宽度
   - RExpandBox.animationDuration: 每个按钮的动画的时间
   - RExpandBox.locatorBoxWidgetSpacing: 定位按钮间的间隔
   - RExpandBox.expandBoxWidgetWidth: 伸缩组件内按钮的宽度
   - RExpandBox.expandBoxWidgetSpacing: 伸缩组件内按钮的间隔
2. 方法说明📃
   - RExpandBox.addWidget()：添加组件
   - RExpandBox.setConfig()：使配置生效
4. ~~配置完RExpandBox后，需要调用RExpandBox.setConfig()使配置生效❗~~
5. styleShell中按钮的圆角大小需要为按钮宽度的二分之一倍❗

<hr/>

# 轮播图
## 效果
![轮播图](./Demo/SlideshowWidget.gif)
## 说明
1. 参数说明📃
   - SlideshowWidget.timer_interval: 图片展示时间
   - SlideshowWidget.animation_time: 动画过度时间
   - SlideshowWidget.lr_widget_size: 两侧图片的尺寸
   - SlideshowWidget.middel_widget_size: 中间图片的尺寸
2. 方法说明📃
   - `SlideshowWidget.addPixmap()`:添加待显示的图片
4. `SlideshowWidget.animation_time`和`SlideshowWidget.timer_interval`需要到`SlideshowWidget.__animationParmas()`内自行配置❗


<hr/>

# ExpInput
## 效果
![输入框_1](./Demo/Input_1.gif)
## 说明
1. 参数说明📃
   - editer_height: 输入框的高度
2. 方法说明📃
   - RInput.setParams(): 配置必要的参数
   - RInput.setFontToEditer(): 配置输入框的字体样式
   - RInput.setTextToPlaceholder(): 配置提示框的字体样式
3. 在配置组件高度和输入框高度的时候，记得给提示框留下充足的显示空间❗


<hr/>


# SimpleInput
## 效果
![SimpleInput](./Demo/Input_2.gif)
## 说明
1. ~~代码量不多，参数自行调整，如果再封装就显得很复杂了(bushi💦~~



<hr/>

# SimpleButton
## 效果
![SimpleButton](./Demo/SimpleButton.gif)
![SimpleButton](./Demo/SimpleButton_group_2.gif)
## 说明
1. 方法📃
   - SimpleButton_X.setParams(): 配置必要的参数
<hr/>

# SwitchButton
## 效果
![SwitchButton](./Demo/SwitchButton.gif)
## 说明
1. 方法📃
   - setParams(): 配置必要的参数
       - indicator_color:指示器的颜色
       - background_color:组件背景颜色
       - checked_indicator_color:点击后的指示器颜色
       - checked_background_color:点击后的背景颜色
<hr/>

# Slider
## 效果
![Slider](./Demo/Silder.gif)
## 说明📃
1. 该控件使用了不同的接口实现，分别是QPainter.drawLine()和Qpainter.drawRect()
2. 该控件的参数设置接口还未实现，但是你可以在Slider.__paramsConfig()内部修改组件参数
3. 参数列表
   - color_groove_sub:被handle滑动槽的颜色
   - color_groove_add:未被handle滑动槽的颜色
   - color_handle_inside:handle(圆形内部的颜色)
   - color_handle_outside:handle(圆形外部的颜色)
   - width_line:滑动槽的宽度
   - radius_handle:handle的半径大小



# 联系方式
- Email:2731491939@qq.com
- WeChat:Roast_71
- csdnBlog:Rev_RoastDuck

# 许可证
QT-material-widgets 使用GPLv3许可证.
