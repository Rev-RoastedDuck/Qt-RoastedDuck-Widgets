#ifndef RRD_WIDGETS_COMPONENTS_WIDGET_BUTTON_SWITCHBUTTON_H
#define RRD_WIDGETS_COMPONENTS_WIDGET_BUTTON_SWITCHBUTTON_H

#include <QToolButton>
#include <QPropertyAnimation>
#include <QPainter>

class SwitchButtonBase : public QToolButton
{
    Q_OBJECT
    Q_PROPERTY(float indicatorX READ indicatorX WRITE setIndicatorX NOTIFY indicatorXChanged)

public:
    explicit SwitchButtonBase(QWidget *parent = nullptr);

protected:
    void mouseReleaseEvent(QMouseEvent *event) override;
    void paintEvent(QPaintEvent *event) override;
    void resizeEvent(QResizeEvent *event) override;

    float indicatorX() const;
    void setIndicatorX(float x);

    virtual void paintBackground(QPainter &painter) = 0;
    virtual void paintIndicator(QPainter &painter) = 0;

    virtual void animaParamsInit();

signals:
    void indicatorXChanged();

private:
    void animaInit();
    

protected:
    QPropertyAnimation *slideAni;
    float _indicatorX;
    float start, end;
};

class SwitchButton_1 : public SwitchButtonBase
{
    Q_OBJECT

public:
    explicit SwitchButton_1(QWidget *parent = nullptr);

    void setParams(const QColor &indicatorColor = QColor(255, 255, 255),
                   const QColor &backgroundColor = QColor(188, 188, 188),
                   const QColor &checkedBackgroundColor = QColor(0, 89, 89),
                   const QColor &checkedIndicatorColor = QColor(255, 255, 255));

protected:
    void paintBackground(QPainter &painter) override;
    void paintIndicator(QPainter &painter) override;

private:
    QColor indicator_color;
    QColor background_color;
    QColor checked_background_color;
    QColor checked_indicator_color;
};

class SwitchButton_2 : public SwitchButtonBase
{
    Q_OBJECT

public:
    explicit SwitchButton_2(QWidget *parent = nullptr);

    void setParams(const QColor &indicatorColor = QColor(181, 181, 181),
                   const QColor &backgroundColor = QColor(181, 181, 181),
                   const QColor &checkedBackgroundColor = QColor(255, 167, 38),
                   const QColor &checkedIndicatorColor = QColor(255, 167, 38));

protected:
    void paintBackground(QPainter &painter) override;
    void paintIndicator(QPainter &painter) override;

private:
    QColor indicator_color;
    QColor background_color;
    QColor checked_background_color;
    QColor checked_indicator_color;
};

class SwitchButton_3 : public SwitchButtonBase
{
    Q_OBJECT

public:
    explicit SwitchButton_3(QWidget *parent = nullptr);

    void setParams(const QColor &indicatorColor = QColor(255, 255, 255),
                   const QColor &backgroundColor = QColor(204, 204, 204),
                   const QColor &checkedBackgroundColor = QColor(51, 102, 153, 200),
                   const QColor &checkedIndicatorColor = QColor(51, 102, 153));

protected:
    void paintBackground(QPainter &painter) override;
    void paintIndicator(QPainter &painter) override;

private:
    QColor indicator_color;
    QColor background_color;
    QColor checked_background_color;
    QColor checked_indicator_color;
};


class SwitchButton_4 : public SwitchButtonBase
{
    Q_OBJECT

public:
    explicit SwitchButton_4(QWidget *parent = nullptr);

    void setParams(const QColor &indicatorColor = QColor(255, 255, 255),
                   const QColor &backgroundColor = QColor(204, 204, 204),
                   const QColor &checkedBackgroundColor = QColor(153, 0, 51, 200),
                   const QColor &checkedIndicatorColor = QColor(153, 0, 51));

protected:
    void paintBackground(QPainter &painter) override;
    void paintIndicator(QPainter &painter) override;
    void enterEvent(QEnterEvent *event) override;
    void leaveEvent(QEvent *event) override;
    void animaParamsInit() override;

private:
    QColor indicator_color;
    QColor background_color;
    QColor checked_background_color;
    QColor checked_indicator_color;
    bool isHover;
};

class SwitchButton_5 : public SwitchButtonBase
{
    Q_OBJECT

public:
    explicit SwitchButton_5(QWidget *parent = nullptr);

    void setParams(const QColor &indicatorColor = QColor(255, 255, 255),
                   const QColor &backgroundColor = QColor(204, 204, 204),
                   const QColor &checkedBackgroundColor = QColor(153, 0, 51, 200));

protected:
    void paintBackground(QPainter &painter) override;
    void paintIndicator(QPainter &painter) override;
    void animaParamsInit() override;

private:
    QColor indicator_color;
    QColor background_color;
    QColor checked_background_color;
    int var;
};

#endif
