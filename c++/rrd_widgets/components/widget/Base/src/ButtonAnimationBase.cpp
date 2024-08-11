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
