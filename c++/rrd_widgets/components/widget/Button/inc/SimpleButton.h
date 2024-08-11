
#ifndef RRD_WIDGETS_COMPONENTS_WIDGET_BUTTON_SIMPLEBUTTON_H_
#define RRD_WIDGETS_COMPONENTS_WIDGET_BUTTON_SIMPLEBUTTON_H_

#include <QColor>
#include <QPainter>
#include <QPushButton>
#include <QWidget>
#include <QPainterPath>
#include <QTimer>
#include "ButtonAnimationBase.h"

/******************************************************************************/
/*---------------------------- SimpleButton Base -----------------------------*/
/******************************************************************************/
class SimpleButtonBase : public AnimationWidgetBase {
    Q_OBJECT

public:
    explicit SimpleButtonBase(QWidget *parent = nullptr);
    void setParams(const QString &text,
                    const QColor &full_color,
                    const QColor &font_anim_start_color, 
                    const QColor &font_anim_finish_color, 
                    int border_radius = 5);

protected:
    int border_radius;
    QColor full_color;
    QColor font_color;
    QColor font_anim_start_color;
    QColor font_anim_finish_color;
    
    virtual void drawBorder(QPainter &painter);
    virtual void drawForeground(QPainter &painter);

    void paintEvent(QPaintEvent *event) override;

private:
    void __drawText(QPainter &painter);
};


class SimpleButton14Base : public SimpleButtonBase {
    Q_OBJECT

public:
    explicit SimpleButton14Base(QWidget *parent = nullptr);

protected:
    bool is_enter;

    void drawBorder(QPainter &painter) override;
    void leaveEvent(QEvent *event) override;
    void enterEvent(QEnterEvent  *event) override; 
};

/******************************************************************************/
/*------------------------------- SimpleButton -------------------------------*/
/******************************************************************************/
class SimpleButton_1 : public SimpleButton14Base {
    Q_OBJECT

public:
    explicit SimpleButton_1(QWidget *parent = nullptr);

private:
    qreal radius;
    QColor full_color;
    void onAnimParamChangeSignal(int v) override;
    void drawForeground(QPainter &painter) override;
    std::pair<int, int> getAnimRange() const override;
};


class SimpleButton_2 : public SimpleButton14Base {
    Q_OBJECT
    
public:
    explicit SimpleButton_2(QWidget *parent = nullptr);

private:
    int rect_width;
    void onAnimParamChangeSignal(int v) override;
    void drawForeground(QPainter &painter) override;
    std::pair<int, int> getAnimRange() const override;
};

class SimpleButton_3 : public SimpleButton14Base {
    Q_OBJECT
    
public:
    explicit SimpleButton_3(QWidget *parent = nullptr);

private:
    int radius;
    int radius_delta_xy;
    void onAnimParamChangeSignal(int v) override;
    void drawForeground(QPainter &painter) override;
    std::pair<int, int> getAnimRange() const override;
};

class SimpleButton_4 : public SimpleButton14Base {
    Q_OBJECT
    
public:
    explicit SimpleButton_4(QWidget *parent = nullptr);

private:
    int rect_width;
    void onAnimParamChangeSignal(int v) override;
    void drawForeground(QPainter &painter) override;
    std::pair<int, int> getAnimRange() const override;
};

class SimpleButton_5 : public SimpleButtonBase{
    Q_OBJECT

public:
    explicit SimpleButton_5(QWidget *parent = nullptr);
    void setParams( const QColor &color = QColor(),
                    const int border_radius = 5,
                    const QString &first_text = QString(),
                    const QString &second_text = QString(),
                    const QColor &first_background_color = QColor(), 
                    const QColor &second_background_color = QColor());
private:
    bool is_enter;
    int anima_hight;
    QString first_text;
    QString second_text;
    QColor first_background_color;
    QColor second_background_color;
    
    void drawForeground(QPainter &painter) override;

    void onAnimParamChangeSignal(int v) override;
    std::pair<int, int> getAnimRange() const override;
    
    void leaveEvent(QEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

    void __animFin(void);
    void __drawText(QPainter &painter);

};

class SimpleButton_6 : public SimpleButtonBase{
    Q_OBJECT

public:
    explicit SimpleButton_6(QWidget *parent = nullptr);
    void setParams( const QColor &color = QColor(),
                    const int border_radius = 5,
                    const QString &first_text = QString(),
                    const QString &second_text = QString(),
                    const QColor &first_background_color = QColor(), 
                    const QColor &second_background_color = QColor());
private:
    bool is_enter;
    int anima_width;
    QString first_text;
    QString second_text;
    QColor first_background_color;
    QColor second_background_color;
    
    void drawForeground(QPainter &painter) override;

    void onAnimParamChangeSignal(int v) override;
    std::pair<int, int> getAnimRange() const override;
    
    void leaveEvent(QEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

    void __animFin(void);
    void __drawText(QPainter &painter);

};
#endif
