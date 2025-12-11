init python:
    class User:
        def __init__(self, key):
            self.key = key
            self.typeColor = "#ffffff"
            self.whatColor = "#ffffff"
            self.reasonColor = "#ffffff"
    user = User("---")
    def getSpeaker():
        curS = store._last_say_who
        if (curS is None):
            return ["", "#fffafa"]
        if (curS.startswith("oleg")):
            return ["Олег", "#1058e8"]
        if (curS.startswith("kirill")):
            return ["Кирилл", "#fffafa"]
        if (curS.startswith("danil")):
            return ["Данил", "#0dbf28"]
        if (curS.startswith("villager")):
            return ["Житель", "#ede611"]
        if (curS.startswith("eldrin")):
            return ["Элдрин", "#db0928"]
        if (curS.startswith("kirill")):
            return ["Король", "#f0731a"]
        else:
            return ["", "#fffafa"]
    def getAvatar():
        curS = getattr(store, '_last_say_who')
        if (curS is None):
            return "placeHolder.png"
        if (curS.startswith("kirill")):
            return "kirillAv.png"
        else:
            return "placeHolder.png"
    def ShowKey(user=user):
        user.typeColor = "#ffffff"
        user.whatColor = "#ffffff"
        user.reasonColor = "#ffffff"
        renpy.notify(user.key)

    def ChangeKey(index, num, colorkey, user=user):
        user.key = user.key[:index] + str(num) + user.key[index+1:]
        if colorkey==1:
            user.typeColor = "#14d91d"
        elif colorkey==2:
            user.whatColor = "#14d91d"
        elif colorkey==3:
            user.reasonColor = "#14d91d"

screen entropy():
    vbox:
        xpos 110 yalign 45
        button:
            action Notify("Осталось багов")
            text "{size=80}{color=#e07612}{font=Handjet-ExtraBold.ttf}[entropy]{/font}{/color}{/size}" style "button_text"
    vbox:
        xalign 0 yalign 0
        imagebutton:
            idle "bugs"
            hover "bugsHover.png"

            action Show("chooseBugType", key="___")

screen chooseBugType(key):
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Тип ошибки":
            text_idle_color user.typeColor
            text_hover_color "#0b08a1"

            action Show("BugType")

        textbutton "Предмет ошибки":
            text_idle_color user.whatColor
            text_hover_color "#0b08a1"

            action Show("BugWhat")

        textbutton "Причины ошибки":
            text_idle_color user.reasonColor
            text_hover_color "#0b08a1"

            action Show("BugReason")

        textbutton "Отправить репорт":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ShowKey)
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"

            action Hide("chooseBugType")

screen BugWhat():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Персонаж":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 1, 2)
        textbutton "Предмет":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 2, 2)
        textbutton "Интерфейс":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 3, 2)
        textbutton "Звуки и музыка":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 4, 2)
        textbutton "Диалоги и сценарий":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 5, 2)
        textbutton "Графическое оформление":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 6, 2)
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Hide("BugWhat")

screen BugType():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Функциональная         ":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 1, 1)
        textbutton "Совместимость":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 2, 1)
        textbutton "Баланс":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 3, 1)
        textbutton "Локализация":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 4, 1)
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Hide("BugType")

screen BugReason():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Характеристики":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 1, 3)
        textbutton "Алгоритмы отображения":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 2, 3)
        textbutton "Алгоритмы поведения":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 3, 3)
        textbutton "Недочеты звука":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 4, 3)
        textbutton "Отсутсвие оптимизации":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 5, 3)
        textbutton "Отсутсвие перевода":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 6, 3)
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Hide("BugReason")

screen AvatarFrame():
    frame:
        xpos 30 ypos 726
        background "avatarFrame.png"
        vbox:
            xpos 25 ypos 97
            $ av = getAvatar()
            add "[av]"

screen NameFrame():
    frame:
        xpos 310 ypos 726
        background "nameFrame.png"
        vbox:
            xpos 45 ypos 30
            $ curSpeaker = getSpeaker()
            $ color = curSpeaker[1]
            $ curSpeaker = curSpeaker[0]
            text "{color=[color]}[curSpeaker]{/color}"
