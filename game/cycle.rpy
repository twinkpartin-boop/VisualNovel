define villager = Character("Житель", color="#ede611")
define eldrin = Character("Элдрин", color="#db0928")
define king = Character("Король", color="#f0731a")

init python:
    cycleIteration = 0

label cycle:
    queue music ["town1.mp3", "town2.mp3"] loop
    show bg town
    with fade
    show screen AvatarFrame

    kirill "Вроде я на месте. Почему этот город выглядит таким угнетенным? Надо поговорить с местными жителями"

    show villager

    kirill "Привет. Я задам пару вопросов?"

    villager "День идет. Тени длиннее становятся. Его Величество на горе бдит. Мы здесь сидим. Все как должно быть."

    kirill "Темный король? Это кто?"

    villager "Он — наш щит. Щит не может быть светлым или темным. Он просто есть. Лес шепчет не для нас. Река течет не для нас. Все для Замка. Все для Порядка."

    kirill "О чем ты говоришь? Этот король типо главный тут?"

    villager "Король - создатель этого мира. Замок его возвышается над просторами леса теней и реки забвения."

    kirill "Лес... Река... Олег, это туда мне нужно идти?"

    oleg_matrix "Все верно. Направляйся к лесу теней"

    hide villager

    stop music fadeout 1.0
    queue music ["forest1.mp3", "forest2.mp3"] loop
    show bg forest
    with fade
#     show BugTree:
#         xpos 1035
#         ypos 446
    show screen BugTreeSkin
    kirill "Я на месте"

    kirill "Тут не просто страшно, тут реально голова болит от этого шепота. Это нормально?"

    oleg_matrix "Аудио-воздействие запланировано. Продолжай свой путь"

    kirill "О! кажется я вижу выход к реке"
#     hide BugTree
    oleg_matrix "Молодец. Ты на правильном пути"
    hide screen BugTreeSkin
    show bg river
    with pixellate


    kirill "Странно... Река неглубокая. Мне что просто пройти ее?"

    Character(None, kind=eldrin) "Войдешь в воду - потеряешь всю свою память"

    kirill "Ты еще кто такой?"

    show eldrin

    eldrin "Я маг Элдрин. Ранее я служил королю придворным магом. Но король стал тираном, и я покинул его"

    kirill "Можешь провести меня до замка? Я собираюсь убить короля"

    eldrin "Хорошо, я проведу тебя. Следуй за мной"

    show bg castle
    with fade

    kirill "Спасибо за помощь. А ты разве не пойдешь сражаться?"
    stop music fadeout 2.0
    eldrin "К сожалению моя магия слаба. Я только буду тебе мешать"

    hide eldrin

    play music "boss.mp3" loop
    show bg thrownhall
    with pixellate
    show king

    king "Кто посмел потревожить мой покой?"

    kirill "О! А вот и король"

    king "Кто ты воин?"

    kirill "Кирилл. Студент"

    king "Ну что же студент Кирилл сразись со мной"

    hide king
    stop music fadeout 1.0

    python:
        cycleIteration += 1
        if (cycleIteration==1):
            renpy.jump("inter1")
        elif (cycleIteration==2):
            renpy.jump("iter2")
        else:
            renpy.jump("iter")













