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
#include "ButtonAnimationBase.h"

AnimationWidgetBase::AnimationWidgetBase(QWidget *parent)
    : QPushButton(parent), anim(new QPropertyAnimation(this, "animParam")), animMsecs(200), animParam(0) {}

void AnimationWidgetBase::animInit() {
    anim->setDuration(animMsecs);
    connect(anim, &QPropertyAnimation::valueChanged, this, [this](const QVariant &value) {
        onAnimParamChangeSignal(value.toInt());
    });
}

void AnimationWidgetBase::animForwardRun() {
    anim->stop();
    auto range = getAnimRange();
    minAnimParam = range.first;
    maxAnimParam = range.second;
    anim->setEndValue(maxAnimParam);
    anim->start();
}

void AnimationWidgetBase::animBackwardRun() {
    anim->stop();
    auto range = getAnimRange();
    minAnimParam = range.first;
    maxAnimParam = range.second;
    anim->setEndValue(minAnimParam);
    anim->start();
}

float AnimationWidgetBase::getAnimParam() const {
    return animParam;
}

void AnimationWidgetBase::setAnimParam(float v) {
    animParam = v;
    emit animParamChangeSignal(static_cast<int>(v));
    update();
}

void AnimationWidgetBase::showEvent(QShowEvent *event) {
    QWidget::showEvent(event);
    animInit();
}
