/*
 * Qt-RoastedDuck - Widgets
 * ======================
 * Qt widgets - based implementation of the Material Design specification.
 * 
 * Repository at https ://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets.
 * 
 * Demo are available at https ://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/Demo.
 * 
 * Examples are available at https ://github.com/Rev-RoastedDuck/Qt-RoastedDuck-Widgets/tree/main/examples.
 * 
 * Information:
 * WeChat: Roast_71.
 * csdnBlog : https ://blog.csdn.net/m0_72760466?type=blog.
 * 
 * 	: copyright : (c)2023 by Rev - RoastedDuck.
 * 	: license : GPLv3, see LICENSE for more details.
*/

#include "SwitchButton.h"

/******************************************************************************/
/*---------------------------- SwitchButton Base -----------------------------*/
/******************************************************************************/
SwitchButtonBase::SwitchButtonBase(QWidget *parent)
    : QToolButton(parent), _indicatorX(0.0f)
{
    setCheckable(true);
    animaInit();
}

void SwitchButtonBase::mouseReleaseEvent(QMouseEvent *event)
{
    QToolButton::mouseReleaseEvent(event);
    if (isChecked())
        slideAni->setEndValue(end);
    else
        slideAni->setEndValue(start);
    slideAni->start();
}

void SwitchButtonBase::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    painter.setRenderHint(QPainter::Antialiasing);
    paintBackground(painter);
    paintIndicator(painter);
}

void SwitchButtonBase::resizeEvent(QResizeEvent *event)
{
    QToolButton::resizeEvent(event);
    animaParamsInit();
}

float SwitchButtonBase::indicatorX() const
{
    return _indicatorX;
}

void SwitchButtonBase::setIndicatorX(float x)
{
    _indicatorX = x;
    update();
    emit indicatorXChanged();
}

void SwitchButtonBase::animaInit()
{
    slideAni = new QPropertyAnimation(this, "indicatorX");
    slideAni->setDuration(200);
}

void SwitchButtonBase::animaParamsInit()
{
    start = height() / 2;
    end = width() - 2 - start;
    _indicatorX = start;
}


/******************************************************************************/
/*------------------------------ SwitchButton --------------------------------*/
/******************************************************************************/
/** \addtogroup SwitchButton_1
 * \{ */
SwitchButton_1::SwitchButton_1(QWidget *parent)
    : SwitchButtonBase(parent)
{
    indicator_color = QColor(255, 255, 255);
    background_color = QColor(188, 188, 188);
    checked_background_color = QColor(0, 89, 89);
    checked_indicator_color = QColor(255, 255, 255);
}

void SwitchButton_1::setParams(const QColor &indicatorColor,
                               const QColor &backgroundColor,
                               const QColor &checkedBackgroundColor,
                               const QColor &checkedIndicatorColor)
{
    indicator_color = indicatorColor;
    background_color = backgroundColor;
    checked_background_color = checkedBackgroundColor;
    checked_indicator_color = checkedIndicatorColor;
}

void SwitchButton_1::paintBackground(QPainter &painter)
{
    painter.save();
    int r = height() / 2;
    QRect rect(1, 1, width() - 2, height() - 1);

    if (!isChecked())
        painter.setBrush(background_color);
    else
        painter.setBrush(checked_background_color);

    painter.setPen(Qt::NoPen);
    painter.drawRoundedRect(rect, r, r);
    painter.restore();
}

void SwitchButton_1::paintIndicator(QPainter &painter)
{
    painter.save();
    int r = height() / 3;
    QPoint point(static_cast<int>(_indicatorX), 0);

    painter.translate(0, height() / 2);
    painter.setPen(Qt::NoPen);

    if (isChecked())
        painter.setBrush(checked_indicator_color);
    else
        painter.setBrush(indicator_color);

    painter.drawEllipse(point, r, r);
    painter.restore();
}
/** \} */


/** \addtogroup SwitchButton_2
 * \{ */
SwitchButton_2::SwitchButton_2(QWidget *parent)
    : SwitchButtonBase(parent)
{
    indicator_color = QColor(181, 181, 181);
    background_color = QColor(181, 181, 181);
    checked_background_color = QColor(0, 89, 89);
    checked_indicator_color = QColor(0, 89, 89);
}

void SwitchButton_2::setParams(const QColor &indicatorColor,
                               const QColor &backgroundColor,
                               const QColor &checkedBackgroundColor,
                               const QColor &checkedIndicatorColor)
{
    indicator_color = indicatorColor;
    background_color = backgroundColor;
    checked_background_color = checkedBackgroundColor;
    checked_indicator_color = checkedIndicatorColor;
}

void SwitchButton_2::paintBackground(QPainter &painter)
{
    painter.save();
    int r = height() / 2;
    QRect rect(1, 1, width() - 2, height() - 2);

    QPen pen;
    pen.setWidth(3);
    if (isChecked())
    {
        pen.setColor(checked_background_color);
        painter.setPen(pen);
    }
    else
    {
        pen.setColor(background_color);
        painter.setPen(pen);
    }

    painter.drawRoundedRect(rect, r, r);
    painter.restore();
}

void SwitchButton_2::paintIndicator(QPainter &painter)
{
    painter.save();
    int r = height() / 3;
    QPoint point(static_cast<int>(_indicatorX), 0);

    painter.translate(0, height() / 2);

    if (isChecked())
        painter.setBrush(checked_indicator_color);
    else
        painter.setBrush(indicator_color);

    painter.setPen(Qt::NoPen);
    painter.drawEllipse(point, r, r);
    painter.restore();
}

/** \} */



/** \addtogroup SwitchButton_3
 * \{ */
SwitchButton_3::SwitchButton_3(QWidget *parent)
    : SwitchButtonBase(parent)
{
    indicator_color = QColor(255, 255, 255);
    background_color = QColor(204, 204, 204);
    checked_background_color = QColor(0, 89, 89);
    checked_indicator_color = QColor(255, 255, 255);
}

void SwitchButton_3::setParams(const QColor &indicatorColor,
                               const QColor &backgroundColor,
                               const QColor &checkedBackgroundColor,
                               const QColor &checkedIndicatorColor)
{
    indicator_color = indicatorColor;
    background_color = backgroundColor;
    checked_background_color = checkedBackgroundColor;
    checked_indicator_color = checkedIndicatorColor;
}

void SwitchButton_3::paintBackground(QPainter &painter)
{
    painter.save();

    int w = width() - width() / 3;
    int h = height() - height() / 3;
    QRect rect(-w / 2, -h / 2, w, h);
    int r = h / 2;

    painter.translate(width() / 2, height() / 2);

    if (isChecked())
        painter.setBrush(checked_background_color);
    else
        painter.setBrush(background_color);

    painter.setPen(Qt::NoPen);
    painter.drawRoundedRect(rect, r, r);
    painter.restore();
}

void SwitchButton_3::paintIndicator(QPainter &painter)
{
    painter.save();
    int r = (height() - height() / 3) / 2 + height() / 9;
    QPoint point(static_cast<int>(_indicatorX), 0);

    painter.translate(0, height() / 2);

    if (isChecked())
        painter.setBrush(checked_indicator_color);
    else
        painter.setBrush(indicator_color);

    painter.setPen(Qt::NoPen);
    painter.drawEllipse(point, r, r);
    painter.restore();
}


/** \} */

/** \addtogroup SwitchButton_4
 * \{ */
SwitchButton_4::SwitchButton_4(QWidget *parent)
    : SwitchButtonBase(parent), isHover(false)
{
    indicator_color = QColor(255, 255, 255);
    background_color = QColor(204, 204, 204);
    checked_background_color = QColor(153, 0, 51, 200);
    checked_indicator_color = QColor(255, 255, 255);
}

void SwitchButton_4::setParams(const QColor &indicatorColor,
                               const QColor &backgroundColor,
                               const QColor &checkedBackgroundColor,
                               const QColor &checkedIndicatorColor)
{
    indicator_color = indicatorColor;
    background_color = backgroundColor;
    checked_background_color = checkedBackgroundColor;
    checked_indicator_color = checkedIndicatorColor;
}

void SwitchButton_4::paintBackground(QPainter &painter)
{
    painter.save();

    int w = width() - width() / 2;
    int h = height() - height() / 2;
    int r = h / 2;

    painter.translate(width() / 2, height() / 2);

    QRect rect(-w / 2, -h / 2, w, h);

    painter.setPen(Qt::NoPen);
    if (isChecked())
        painter.setBrush(checked_background_color);
    else
        painter.setBrush(background_color);

    painter.drawRoundedRect(rect, r, r);
    painter.restore();
}

void SwitchButton_4::paintIndicator(QPainter &painter)
{
    painter.save();
    int r = (height() - height() / 2) / 2 + height() / 9;
    QPoint point(static_cast<int>(_indicatorX), 0);

    painter.translate(0, height() / 2);
    painter.setPen(Qt::NoPen);

    if (isChecked())
    {
        if (isHover)
        {
            QColor c = checked_indicator_color;
            painter.setBrush(QColor(c.red(), c.green(), c.blue(), 100));
            painter.drawEllipse(point, r + 5, r + 5);
        }
        painter.setBrush(checked_indicator_color);
    }
    else
    {
        if (isHover)
        {
            QColor c = indicator_color;
            painter.setBrush(QColor(c.red(), c.green(), c.blue(), 100));
            painter.drawEllipse(point, r + 5, r + 5);
        }
        painter.setBrush(indicator_color);
    }

    painter.drawEllipse(point, r, r);
    painter.restore();
}

void SwitchButton_4::enterEvent(QEnterEvent *event)
{
    SwitchButtonBase::enterEvent(event);
    isHover = true;
}

void SwitchButton_4::leaveEvent(QEvent *event)
{
    SwitchButtonBase::leaveEvent(event);
    isHover = false;
}

void SwitchButton_4::animaParamsInit()
{
    SwitchButtonBase::animaParamsInit();
    isHover = false;
}

/** \} */



/** \addtogroup SwitchButton_5
 * \{ */
SwitchButton_5::SwitchButton_5(QWidget *parent)
    : SwitchButtonBase(parent)
{
    indicator_color = QColor(255, 255, 255);
    background_color = QColor(204, 204, 204);
    checked_background_color = QColor(153, 0, 51, 200);
}

void SwitchButton_5::setParams(const QColor &indicatorColor,
                               const QColor &backgroundColor,
                               const QColor &checkedBackgroundColor)
{
    indicator_color = indicatorColor;
    background_color = backgroundColor;
    checked_background_color = checkedBackgroundColor;
}

void SwitchButton_5::animaParamsInit()
{
    var = height() / 8;
    int h = height() - var * 2;
    start = var;
    end = width() - h - var;
    _indicatorX = var;
}

void SwitchButton_5::paintBackground(QPainter &painter)
{
    painter.save();

    if (isChecked())
        painter.setBrush(checked_background_color);
    else
        painter.setBrush(background_color);

    painter.setPen(Qt::NoPen);
    painter.drawRoundedRect(rect(), 5, 5);
    painter.restore();
}

void SwitchButton_5::paintIndicator(QPainter &painter)
{
    painter.save();
    int h = height() - var * 2;
    QRect rect(static_cast<int>(_indicatorX), -h / 2, h, h);

    painter.translate(0, height() / 2);
    painter.setPen(Qt::NoPen);
    painter.setBrush(indicator_color);

    painter.drawRoundedRect(rect, 5, 5);
    painter.restore();
}
/** \} */