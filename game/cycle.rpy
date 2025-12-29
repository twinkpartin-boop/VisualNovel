define villager = Character("Житель", color="#ede611")
define eldrin = Character("Элдрин", color="#db0928")
define king = Character("Король", color="#f0731a")
define book = Character(None, color="#fffafa", what_italic=True)

default iter = 0
default speed = False
default power = False

default isEldrinShowed = False
label cycle:
    default eldrin_ = Eldrin()
    $ ConsoleLock = True
    if iter > 1:
        show screen Console
        show screen Cheats
    elif iter > 0:
        show screen Cheats
    queue music ["town1.mp3", "town2.mp3"] loop
    show bg town
    with fade
    show screen AvatarFrame
    $ cps = 40 + 1000*speed
    kirill "Вроде я на месте. Почему этот город выглядит таким угнетенным? Надо поговорить с местными жителями"
    $ cps = 40 + 1000*speed
    show villager

    kirill "Привет. Я задам пару вопросов?"
    $ cps = 40 + 1000*speed
    villager "{cps=[cps]}День идет. Тени длиннее становятся. Его Величество - Темный Король на горе бдит. Мы здесь сидим. Все как должно быть.{/cps}"
    if iter > 1:
        show screen Console(CodeBugLabel="RepeatBugCode")
        $ ConsoleLock = False
        kirill_himself "(Может попробовать написать алгоритмя для взаимодествия со всеми жителями сразу?)"
    $ cps = 40 + 1000*speed
    kirill "Темный король? Это кто?"
    $ cps = 40 + 1000*speed
    villager "{cps=[cps]}Он — наш щит. Щит не может быть светлым или темным. Он просто есть. Лес шепчет не для нас. Река течет не для нас. Все для Замка. Все для Порядка.{cps=[cps]}"
    $ cps = 40 + 1000*speed
    kirill "О чем ты говоришь? Этот король типо главный тут?"
    $ cps = 40 + 1000*speed
    villager "{cps=[cps]}Король - создатель этого мира. Замок его возвышается над просторами леса теней и реки забвения.{cps=[cps]}"
    if speed:
        call FastTextBug from _call_FastTextBug
    if iter == 0:
        kirill "Лес... Река... Олег, это туда мне нужно идти?"

        oleg_matrix "Все верно. Направляйся к лесу теней"
    else:
        kirill_himself "Теперь пора снова идти к реке."
    if iter > 1:
        show screen Console
    $ ConsoleLock = True
    hide villager

    show screen BugWall

    kirill "Мне кажется тут что-то мешает пройти..."
    kirill "О! Смог протиснуться."

    hide screen BugWall

    stop music fadeout 1.0
    play sound "ForestWhisper.mp3" loop volume 0.2
    queue music ["forest1.mp3", "forest2.mp3"] loop
    default music = False
    $ music = renpy.music.is_playing()
    show bg forest
    with fade

    show screen StickBug
    show screen BugTreeSkin
    kirill "Я на месте"
    if iter == 0:
        kirill "Тут не просто страшно, тут реально голова болит от этого шепота. Это нормально?"

        oleg_matrix "Аудио-воздействие запланировано. Продолжай свой путь"
    else:
        kirill_himself "Как же этот шепот раздражает..."

    kirill "О! кажется я вижу выход к реке"
    if iter == 0:
        oleg_matrix "Молодец. Ты на правильном пути"
    else:
        kirill_himself "Надеюсь я нашел тут все ошибки"
    hide screen BugTreeSkin
    hide screen StickBug
    show bg river
    with pixellate
    show screen BugRock
    show screen RiverBug

    kirill "Странно... Река неглубокая. Мне что просто пройти ее?"

    Character(None, kind=eldrin) "{size=[eldrin_.size]}Войдешь в воду - потеряешь всю свою память{/size}"

    kirill "Ты еще кто такой?"

    show eldrin
    $ isEldrinShowed = True

    eldrin "{size=[eldrin_.size]}Я маг Элдрин. Ранее я служил королю придворным магом. Но король стал тираном, и я покинул его{/size}"

    if eldrin_.size > 50:
        show screen BugRock(untouchable=True)
        hide screen RiverBug
        call eldrinSpeechBug from _call_eldrinSpeechBug
        show screen BugRock
        show screen RiverBug
        hide eldrin
        show eldrin

    kirill "Можешь провести меня до замка? Я собираюсь убить короля"

    eldrin "{size=[eldrin_.size]}Хорошо, я проведу тебя. Следуй за мной{/size}"

    hide screen BugRock
    hide screen RiverBug
    stop sound
    show bg castle
    with fade
    show screen CastleWallBug

    kirill "Спасибо за помощь. А ты разве не пойдешь сражаться?"

    eldrin "{size=[eldrin_.size]}К сожалению моя магия слаба. Я только буду тебе мешать{/size}"

    if eldrin_.size > 50:
        hide screen CastleWallBug
        call eldrinSpeechBug from _call_eldrinSpeechBug_1
    hide screen CastleWallBug

    kirill "Я одолею его!"

    stop music fadeout 1.0
    hide eldrin
    $ isEldrinShowed = False

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
        iter += 1
        if (iter==1):
            renpy.jump("inter1")
        elif (iter==2):
            renpy.jump("iter2")
        else:
            renpy.jump("iter")


label book:

    book "{size=40}Руководство тестировщика{/size}"
    return