#include <QPushButton>
#include <QEvent>
#include <QPainter>
#include <QPainterPath>
#include <QColor>
#include <QPen>
#include <QWidget>

class BaseSignalButton : public QPushButton {
    Q_OBJECT

public:
    explicit BaseSignalButton(QWidget *parent = nullptr) : QPushButton(parent) {
        is_hovering = false;
        is_clicked = false;
        installEventFilter(this);
    }

protected:
    bool eventFilter(QObject *obj, QEvent *event) override {
        if (obj == this) {
            if (event->type() == QEvent::HoverEnter) {
                is_hovering = true;
            } else if (event->type() == QEvent::HoverLeave) {
                is_hovering = false;
            } else if (event->type() == QEvent::MouseButtonRelease) {
                is_clicked = true;
            }
        }
        return QPushButton::eventFilter(obj, event);
    }

    bool is_hovering;
    bool is_clicked;
};


class BaseParamsButton : public BaseSignalButton {
    Q_OBJECT

public:
    explicit BaseParamsButton(QWidget *parent = nullptr) : BaseSignalButton(parent) {
        font_color = QColor();
        border_color = QColor();
        background_color = QColor();
        text_flag = Qt::AlignLeft | Qt::AlignVCenter;
        border_radius = 0;
    }

    void setParams(QColor font_color = QColor(), QColor border_color = QColor(),
                   QColor background_color = QColor(), int border_radius = 0,
                   Qt::Alignment text_flag = Qt::AlignLeft | Qt::AlignVCenter) {
        this->font_color = font_color;
        this->border_color = border_color;
        this->background_color = background_color;
        this->border_radius = border_radius;
        this->text_flag = text_flag;
    }

protected:
    QColor font_color;
    QColor border_color;
    QColor background_color;
    Qt::Alignment text_flag;
    int border_radius;
};


class BaseButton : public BaseParamsButton {
    Q_OBJECT

public:
    explicit BaseButton(QWidget *parent = nullptr) : BaseParamsButton(parent) {}

protected:
    void paintEvent(QPaintEvent *event) override {
        QPainter painter(this);
        painter.setPen(Qt::NoPen);
        painter.setRenderHint(QPainter::Antialiasing);

        QPainterPath path;
        path.addRoundedRect(this->rect(), border_radius, border_radius);
        painter.setClipPath(path);

        drawBackground(&painter);
        drawIcon(&painter);
        drawText(&painter);
    }

    void drawIcon(QPainter *painter) {
        painter->save();
        if (!icon().isNull()) {
            QPixmap pixmap = icon().pixmap(height() * 0.7);
            painter->drawPixmap(height() * 0.15, height() * 0.15, pixmap);
        }
        painter->restore();
    }

    void drawText(QPainter *painter) {
        painter->save();
        if (!text().isEmpty()) {
            painter->setFont(font());
            painter->setPen(QPen(font_color));
            if (!icon().isNull()) {
                text_flag = Qt::AlignLeft | Qt::AlignVCenter;
                painter->drawText(rect().adjusted(height(), 0, 0, -2), text_flag, text());
            } else {
                text_flag = Qt::AlignVCenter;
                painter->drawText(rect().adjusted(5, 5, -5, -5), text_flag, text());
            }
        }
        painter->restore();
    }

    virtual void drawBackground(QPainter *painter) {
        painter->save();
        painter->setBrush(background_color);
        painter->drawRect(this->rect());
        painter->restore();
    }
};



class BaseHoveringButton : public BaseButton {
    Q_OBJECT

public:
    explicit BaseHoveringButton(QWidget *parent = nullptr) : BaseButton(parent) {}

    void setParams(QColor font_color = QColor(), QColor border_color = QColor(),
                   QColor background_color = QColor(), int border_radius = 0,
                   Qt::Alignment text_flag = Qt::AlignLeft | Qt::AlignVCenter,
                   QColor hovering_color = QColor(255, 255, 255)) {
        BaseButton::setParams(font_color, border_color, background_color, border_radius, text_flag);
        this->hovering_color = hovering_color;
    }

protected:
    void drawBackground(QPainter *painter) override {
        BaseButton::drawBackground(painter);
        painter->save();
        if (is_hovering) {
            painter->setBrush(hovering_color);
        } else {
            painter->setBrush(background_color);
        }
        painter->drawRect(this->rect());
        painter->restore();
    }

    QColor hovering_color;
};



class BaseClickedButton : public BaseButton {
    Q_OBJECT

public:
    explicit BaseClickedButton(QWidget *parent = nullptr) : BaseButton(parent) {}

protected:
    void drawBackground(QPainter *painter) override {
        BaseButton::drawBackground(painter);
        painter->save();
        if (is_clicked) {
            QPen pen;
            pen.setColor(border_color);
            pen.setWidth(4);
            painter->setPen(pen);
            painter->drawLine(0, border_radius, 0, height() - border_radius);
        }
        painter->restore();
    }
};




class BaseClickedHoveringButton : public BaseButton {
    Q_OBJECT

public:
    explicit BaseClickedHoveringButton(QWidget *parent = nullptr) : BaseButton(parent) {}

    void setParams(QColor font_color = QColor(), QColor border_color = QColor(),
                   QColor background_color = QColor(), int border_radius = 0,
                   Qt::Alignment text_flag = Qt::AlignLeft | Qt::AlignVCenter,
                   QColor hovering_color = QColor(255, 255, 255)) {
        this->hovering_color = hovering_color;
        BaseButton::setParams(font_color, border_color, background_color, border_radius, text_flag);
    }

protected:
    void drawBackground(QPainter *painter) override {
        painter->save();

        if (is_hovering) {
            painter->setBrush(hovering_color);
        } else {
            painter->setBrush(background_color);
        }

        painter->drawRect(this->rect());

        if (is_clicked) {
            QPen pen;
            pen.setColor(border_color);
            pen.setWidth(3);
            painter->setPen(pen);
            painter->drawLine(0, border_radius, 0, height() - border_radius);
        }
        painter->restore();
    }

    QColor hovering_color;
};