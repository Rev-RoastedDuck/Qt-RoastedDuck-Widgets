#define ANIMATIONWIDGETBASE_H
#ifndef ANIMATIONWIDGETBASE_H
#include <QWidget>
#include <QPropertyAnimation>
#include <QPushButton>
#include <QLineEdit>
#include <utility>

template <typename T>
class AnimationWidgetBase : public T {
    Q_PROPERTY(Float animParam READ getAnimParam WRITE setAnimParam)
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
    float _animParam;
    int minAnimParam;
    int maxAnimParam;
};

template <typename T>
AnimationWidgetBase<T>::AnimationWidgetBase(QWidget *parent)
    : T(parent), anim(new QPropertyAnimation(this, "animParam")), animMsecs(200), _animParam(0) {}

template <typename T>
void AnimationWidgetBase<T>::animInit() {
    this->anim->setDuration(animMsecs);
    this->connect(this->anim, &QPropertyAnimation::valueChanged, this, [this](const QVariant &value) {
        onAnimParamChangeSignal(value.toInt());
    });
}

template <typename T>
void AnimationWidgetBase<T>::animForwardRun() {
    this->anim->stop();
    std::tie(minAnimParam, maxAnimParam) = getAnimRange();
    this->anim->setStartValue(this->getAnimParam());
    this->anim->setEndValue(maxAnimParam);
    this->anim->start();
}

template <typename T>
void AnimationWidgetBase<T>::animBackwardRun() {
    this->anim->stop();
    std::tie(minAnimParam, maxAnimParam) = getAnimRange();
    this->anim->setStartValue(this->getAnimParam());
    this->anim->setEndValue(minAnimParam);
    this->anim->start();
}

template <typename T>
float AnimationWidgetBase<T>::getAnimParam() const {
    return _animParam;
}

template <typename T>
void AnimationWidgetBase<T>::setAnimParam(float v) {
        _animParam = v;
        qDebug() << "value:" << _animParam << "\r\n";
        emit animParamChangeSignal(static_cast<int>(v));
        this->update();
}

template <typename T>
void AnimationWidgetBase<T>::showEvent(QShowEvent *event) {
    T::showEvent(event);
    animInit();
}

#endif // ANIMATIONWIDGETBASE_H
