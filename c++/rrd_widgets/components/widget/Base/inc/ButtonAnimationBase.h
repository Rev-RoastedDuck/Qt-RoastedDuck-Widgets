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
#ifndef ANIMATIONBUTTONBASE_H
#define ANIMATIONBUTTONBASE_H

#include <QWidget>
#include <QPushButton>
#include <QPropertyAnimation>
#include <QParallelAnimationGroup>
#include <QSignalMapper>

class AnimationWidgetBase : public QPushButton {
    Q_OBJECT
    Q_PROPERTY(float animParam READ getAnimParam WRITE setAnimParam NOTIFY animParamChangeSignal)

public:
    explicit AnimationWidgetBase(QWidget *parent = nullptr);

    virtual std::pair<int, int> getAnimRange() const = 0;
    virtual void onAnimParamChangeSignal(int v) = 0;

    float getAnimParam() const;
    void setAnimParam(float v);

    void animForwardRun();
    void animBackwardRun();

protected:
    void showEvent(QShowEvent *event) override;

signals:
    void animParamChangeSignal(int v);

private:
    void animInit();

    QPropertyAnimation *anim;
    int animMsecs;
    float animParam;
    int minAnimParam;
    int maxAnimParam;
};

#endif // ANIMATIONWIDGETBASE_H
