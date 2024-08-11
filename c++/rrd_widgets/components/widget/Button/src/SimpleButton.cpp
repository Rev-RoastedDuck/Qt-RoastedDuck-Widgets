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

#include "SimpleButton.h"

/******************************************************************************/
/*---------------------------- SimpleButton Base -----------------------------*/
/******************************************************************************/

/** \addtogroup SimpleButtonBase
 * \{ */
SimpleButtonBase::SimpleButtonBase(QWidget *parent)
    : AnimationWidgetBase(parent), border_radius(0), full_color(Qt::white), font_color(Qt::black) {}

void SimpleButtonBase::setParams(const QString &text, const QColor &full_color, const QColor &font_anim_start_color, const QColor &font_anim_finish_color, int border_radius) {
    setText(text);
    this->full_color = full_color;
    this->border_radius = border_radius;
    this->font_anim_start_color = font_anim_start_color;
    this->font_anim_finish_color = font_anim_finish_color;
    this->font_color = this->font_anim_start_color;
}

void SimpleButtonBase::__drawText(QPainter &painter) {
    painter.save();
    painter.setFont(this->font());
    painter.setPen(this->font_color);

    if (!this->text().isEmpty()) {
        painter.drawText(this->rect(), Qt::AlignCenter, this->text());
    }
    painter.restore();
}

void SimpleButtonBase::drawBorder(QPainter &painter) {
    // Override in derived classes
}

void SimpleButtonBase::drawForeground(QPainter &painter) {
    // Override in derived classes
}

void SimpleButtonBase::paintEvent(QPaintEvent *event) {
    QPainter painter(this);
    painter.setPen(Qt::NoPen);
    painter.setRenderHint(QPainter::Antialiasing);

    QPainterPath path;
    path.addRoundedRect(this->rect(), this->border_radius, this->border_radius);
    painter.setClipPath(path);

    this->drawBorder(painter);
    this->drawForeground(painter);
    this->__drawText(painter);
}
/** \} */

/** \addtogroup SimpleButton14Base
 * \{ */
SimpleButton14Base::SimpleButton14Base(QWidget *parent)
    : SimpleButtonBase(parent), is_enter(false) {}

void SimpleButton14Base::drawBorder(QPainter &painter) {
    painter.save();
    QPen pen;
    pen.setWidth(2);
    pen.setColor(this->full_color);

    painter.setPen(pen);
    painter.drawRoundedRect(this->rect(), this->border_radius, this->border_radius);
    painter.restore();
}

void SimpleButton14Base::enterEvent(QEnterEvent *event) {
    this->is_enter = true;
    this->font_color = this->font_anim_finish_color;
    this->animForwardRun();
}

void SimpleButton14Base::leaveEvent(QEvent *event) {
    this->is_enter = false;
    this->font_color = this->font_anim_start_color;
    this->animBackwardRun();
}

/** \} */

/******************************************************************************/
/*------------------------------- SimpleButton -------------------------------*/
/******************************************************************************/

/** \addtogroup SimpleButton_1
 * \{ */
SimpleButton_1::SimpleButton_1(QWidget *parent)
    : SimpleButton14Base(parent), radius(0) {}

void SimpleButton_1::drawForeground(QPainter &painter) {
    painter.save();
    QBrush brush(this->full_color);
    painter.setBrush(brush);

    painter.drawEllipse(QPointF(0, 0), this->radius, this->radius);
    painter.drawEllipse(QPointF(this->width(), this->height()), this->radius, this->radius);
    painter.restore();
}

void SimpleButton_1::onAnimParamChangeSignal(int v) {
    this->radius = v;
}

std::pair<int, int> SimpleButton_1::getAnimRange() const {
    int min = 0;
    int max = std::sqrt(std::pow(this->width(), 2) + std::pow(this->height(), 2));
    return {min, max};
}
/** \} */

/** \addtogroup SimpleButton_2
 * \{ */
SimpleButton_2::SimpleButton_2(QWidget *parent)
    : SimpleButton14Base(parent), rect_width(0) {}

void SimpleButton_2::drawForeground(QPainter &painter) {
    painter.save();
    QBrush brush(this->full_color);
    painter.setBrush(brush);

    painter.translate(this->width() / 2,this->height() / 2);
    painter.rotate(45);
    painter.drawRect(QRectF(-this->rect_width / 2, - this->width() / 2,this->rect_width,this->width()));
    
    
    painter.restore();
}

void SimpleButton_2::onAnimParamChangeSignal(int v) {
    this->rect_width = v;
}

std::pair<int, int> SimpleButton_2::getAnimRange() const {
    int min = 0;
    int max = std::sqrt(std::pow(this->width(), 2) + std::pow(this->height(), 2));
    return {min, max};
}
/** \} */

/** \addtogroup SimpleButton_3
 * \{ */
SimpleButton_3::SimpleButton_3(QWidget *parent)
    : SimpleButton14Base(parent), radius(0), radius_delta_xy(15) {}

void SimpleButton_3::drawForeground(QPainter &painter) {
    painter.save();
    painter.setBrush(QBrush(this->full_color));
    painter.translate(this->width() / 2, this->height() * 1.5);

    int radius_x = this->radius;
    int radius_y = this->radius - this->radius_delta_xy;
    painter.drawEllipse(QPoint(0, 0), radius_x, radius_y);
    painter.restore();
}

void SimpleButton_3::onAnimParamChangeSignal(int v) {
    this->radius = v;
}

std::pair<int, int> SimpleButton_3::getAnimRange() const {
    int min = 0;
    int max = std::sqrt(std::pow(this->width(), 2) + std::pow(this->height(), 2));
    return {min, max};
}
/** \} */

/** \addtogroup SimpleButton_4
 * \{ */
SimpleButton_4::SimpleButton_4(QWidget *parent)
    : SimpleButton14Base(parent), rect_width(0) {}

void SimpleButton_4::drawForeground(QPainter &painter) {
    painter.save();
    QBrush brush(this->full_color);
    painter.setBrush(brush);

    if (this->is_enter) {
        painter.drawRect(QRectF(0, 0, this->rect_width, this->height()));
    } else {
        painter.translate(this->width(), this->height());
        painter.rotate(180);
        painter.drawRect(QRectF(0, 0, this->rect_width, this->height()));
    }

    painter.restore();
}

void SimpleButton_4::onAnimParamChangeSignal(int v) {
    this->rect_width = v;
}

std::pair<int, int> SimpleButton_4::getAnimRange() const {
    int min = 0;
    int max = this->width();
    return {min, max};
}
/** \} */

/** \addtogroup SimpleButton_5
 * \{ */

SimpleButton_5::SimpleButton_5(QWidget *parent)
    : SimpleButtonBase(parent), anima_hight(0), is_enter(false){}

void SimpleButton_5::setParams( const QColor &color,
                                const int border_radius,
                                const QString &first_text,
                                const QString &second_text,
                                const QColor &first_background_color, 
                                const QColor &second_background_color){
    this->font_color = color;
    this->border_radius = border_radius;
    this->first_text = first_text;
    this->second_text = second_text;
    this->first_background_color = first_background_color;
    this->second_background_color = second_background_color;
}

void SimpleButton_5::drawForeground(QPainter &painter){
    painter.translate(0, -anima_hight);

    painter.save();
    QBrush brush(first_background_color);
    painter.setBrush(brush);
    painter.drawRect(QRectF(0, 0, width(), height()));
    __drawText(painter);
    painter.restore();

    painter.save();
    brush.setColor(second_background_color);
    painter.setBrush(brush);
    painter.drawRect(QRectF(0, height(), width(), height()));
    __drawText(painter);
    painter.restore();

}

void SimpleButton_5::onAnimParamChangeSignal(int v){
    this->anima_hight = v;
}

std::pair<int, int> SimpleButton_5::getAnimRange() const{
    return {0, this->height()};
}

void SimpleButton_5::leaveEvent(QEvent *event){
    is_enter = false;
    animBackwardRun();

}

void SimpleButton_5::mouseReleaseEvent(QMouseEvent *event){
    SimpleButtonBase::mouseReleaseEvent(event);
    is_enter = true;
    this->animForwardRun();
    QTimer::singleShot(1000, this, &SimpleButton_5::__animFin);

}

void SimpleButton_5::__animFin(void){
    is_enter = false;
    this->animBackwardRun();


}

void SimpleButton_5::__drawText(QPainter &painter){
    painter.save();
    painter.setFont(font());
    painter.setPen(font_color);

    if (!is_enter) {
        painter.drawText(0, 0, width(), height(), Qt::AlignCenter, first_text);
    } else {
        painter.drawText(0, height(), width(), height(), Qt::AlignCenter, second_text);
    }
    painter.restore();

}

/** \} */


/** \addtogroup SimpleButton_6
 * \{ */
SimpleButton_6::SimpleButton_6(QWidget *parent)
    : SimpleButtonBase(parent), anima_width(0), is_enter(false){}

void SimpleButton_6::setParams( const QColor &color,
                                const int border_radius,
                                const QString &first_text,
                                const QString &second_text,
                                const QColor &first_background_color, 
                                const QColor &second_background_color){
    this->font_color = color;
    this->border_radius = border_radius;
    this->first_text = first_text;
    this->second_text = second_text;
    this->first_background_color = first_background_color;
    this->second_background_color = second_background_color;
}

void SimpleButton_6::drawForeground(QPainter &painter){
    painter.translate(anima_width,0);

    painter.save();
    QBrush brush(first_background_color);
    painter.setBrush(brush);
    painter.drawRect(QRectF(0, 0, width(), height()));
    __drawText(painter);
    painter.restore();

    painter.save();
    brush.setColor(second_background_color);
    painter.setBrush(brush);
    painter.drawRect(QRectF(-width(), 0, width(), height()));
    __drawText(painter);
    painter.restore();

}

void SimpleButton_6::onAnimParamChangeSignal(int v){
    this->anima_width = v;
}

std::pair<int, int> SimpleButton_6::getAnimRange() const{
    return {0, this->width()};
}

void SimpleButton_6::leaveEvent(QEvent *event){
    is_enter = false;
    animBackwardRun();

}

void SimpleButton_6::mouseReleaseEvent(QMouseEvent *event){
    SimpleButtonBase::mouseReleaseEvent(event);
    is_enter = true;
    this->animForwardRun();
    QTimer::singleShot(1000, this, &SimpleButton_6::__animFin);

}

void SimpleButton_6::__animFin(void){
    is_enter = false;
    this->animBackwardRun();
}

void SimpleButton_6::__drawText(QPainter &painter){
    painter.save();
    painter.setFont(font());
    painter.setPen(font_color);

    if (!is_enter) {
        painter.drawText(0, 0, width(), height(), Qt::AlignCenter, first_text);
    } else {
        painter.drawText(-width(), 0, width(), height(), Qt::AlignCenter, second_text);
    }
    painter.restore();

}

/** \} */