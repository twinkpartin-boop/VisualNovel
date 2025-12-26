init python:
    class User:
        def __init__(self, key):
            self.key = key
            self.typeColor = "#ffffff"
            self.whatColor = "#ffffff"
            self.reasonColor = "#ffffff"
            self.curSpeakerYFrame = 250
            self.entropy = 19
            self.realEntropy = 19
            # Ключ бага: (код, был ли проверен, правильно ли проверен)
#             self.bugs = {"TreeSkin": ["262", False, False]}
    user = User("---")
    def getSpeaker():
        curS = store._last_say_who
        if (curS is None):
            return ["", "#fffafa"]
        if (curS.startswith("oleg")):
            return ["Олег", "#80f2ff"]
        if (curS.startswith("kirill")):
            return ["Кирилл", "#fffafa"]
        if (curS.startswith("danil")):
            return ["Данил", "#0dbf28"]
        if (curS.startswith("villager")):
            return ["Житель", "#ede611"]
        if (curS.startswith("eldrin")):
            return ["Элдрин", "#db0928"]
        if (curS.startswith("king")):
            return ["Король", "#f0731a"]
        else:
            return ["", "#fffafa"]
    def getAvatar():
        curS = getattr(store, '_last_say_who')
        if (curS is None):
            return "placeHolder.png"
        if (curS.startswith("kirill")):
            user.curSpeakerYFrame = 250
            return "kirillAv.png"
        if (curS.startswith("danil")):
            user.curSpeakerYFrame = 251
            return "danilAV.png"
        if (curS.startswith("oleg_matrix")):
            user.curSpeakerYFrame = 311
            return "oleg_matrixAV.png"
        if (curS.startswith("oleg")):
            user.curSpeakerYFrame = 311
            return "olegAV.png"
        if (curS.startswith("villager")):
            user.curSpeakerYFrame = 252
            return "villagerAV.png"
        if (curS.startswith("eldrin")):
            user.curSpeakerYFrame = 255
            return "eldrinAV.png"
        if (curS.startswith("king")):
            user.curSpeakerYFrame = 307
            return "kingAV.png"
        else:
            return "placeHolder.png"
    def ShowKey(bugKey):
        user.typeColor = "#ffffff"
        user.whatColor = "#ffffff"
        user.reasonColor = "#ffffff"
        renpy.notify(f"отправленный ключ ошибки -> {user.key}")
        return CheckKey(bugKey)

    def ChangeKey(index, num, colorkey, key):
        user.key = user.key[:index] + str(num) + user.key[index+1:]
        if colorkey==1:
            user.typeColor = "#14d91d"
        elif colorkey==2:
            user.whatColor = "#14d91d"
        elif colorkey==3:
            user.reasonColor = "#14d91d"
        renpy.notify(f"Выбрано: {key}")
    def GetCheatsButtons():
        global speed
        global power
        res = ["", "", "", ""]
        if speed:
            res[0] = "On.png"
            res[1] = "OnHover.png"
        else:
            res[0] = "Off.png"
            res[1] = "OffHover.png"
        if power:
            res[2] = "On.png"
            res[3] = "OnHover.png"
        else:
            res[2] = "Off.png"
            res[3] = "OffHover.png"
        return res
    def ChangeStat(choice):
        global speed
        global power
        if choice == 1:
            speed = not speed
        else:
            power = not power
define narrator = Character(None, what_xalign=0.5, what_text_align=0.5)
default frameH = 374
screen entropy(bugKey="---"):
    vbox:
        xpos 110 yalign 45
        button:
            action Notify("Осталось багов")
            text "{size=80}{color=#e07612}{font=Handjet-ExtraBold.ttf}[entropy]{/font}{/color}{/size}" style "button_text"
    vbox:
        xalign 0 yalign 0
        imagebutton:
            idle "bugs.png"
            hover "bugsHover.png"

            action Show("chooseBugType", bugKey=bugKey)

screen chooseBugType(bugKey="---"):
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
            action Function(ShowKey, bugKey)
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"

            action Hide("chooseBugType")

screen BugWhat():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "НПС (неиграбельный персонаж)":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 1, 2, "НПС")
        textbutton "Объект":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 2, 2, "Объект")
        textbutton "Интерфейс":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 3, 2, "Интерфейс")
        textbutton "Звуки и музыка":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 4, 2, "Звуки и музыка")
        textbutton "Диалоги и сценарий":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 5, 2, "Диалоги и сценарий")
        textbutton "Графическое оформление":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 1, 6, 2, "Графическое оформление")
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Hide("BugWhat")

screen BugType():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Взаимодействие   ":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 1, 1, "Взаимодействие")
        textbutton "Совместимость":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 2, 1, "Совместимость")
        textbutton "Баланс":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 3, 1, "Баланс")
        textbutton "Локализация":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 4, 1, "Локализация")
        textbutton "Поведение":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 0, 5, 1, "Поведение")
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Hide("BugType")

screen BugReason():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Алгоритмы поведения ии":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 1, 3, "Алгоритмы поведения ии")
        textbutton "Алгоритмы отображения":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 2, 3, "Алгоритмы отображения")
        textbutton "Алгоритмы механик":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 3, 3, "Алгоритмы механик")
        textbutton "Недочеты звука":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 4, 3, "Недочеты звука")
        textbutton "Недочеты текста":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Function(ChangeKey, 2, 5, 3, "Недочеты текста")
#         textbutton "Отсутсвие оптимизации":
#             text_idle_color "#ffffff"
#             text_hover_color "#0b08a1"
#             action Function(ChangeKey, 2, 5, 3, "Отсутсвие оптимизации")
#         textbutton "Отсутсвие перевода":
#             text_idle_color "#ffffff"
#             text_hover_color "#0b08a1"
#             action Function(ChangeKey, 2, 6, 3, "Отсутсвие перевода")
        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"
            action Hide("BugReason")

screen AvatarFrame():
    $ av = getAvatar()
    frame:
        xpos 30 ypos 726
        background "avatarFrame.png"
        vbox:
            xpos 0 ypos (frameH-user.curSpeakerYFrame)
            add "[av]"
        vbox:
            xpos 50 ypos 30
            $ curSpeaker = getSpeaker()
            $ color = curSpeaker[1]
            $ curSpeaker = curSpeaker[0]
            text "{color=[color]}[curSpeaker]{/color}"

screen Cheats():
    vbox:
        xpos 1830 ypos 100
        $ images = GetCheatsButtons()
        imagebutton:
            idle images[0]
            hover images[1]

            action Function(ChangeStat, 1)
        imagebutton:
            idle images[2]
            hover images[3]

            action Function(ChangeStat, 2)