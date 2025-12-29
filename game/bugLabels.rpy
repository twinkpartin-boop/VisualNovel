init python:
    def CheckKey(bugKey="---"):
        global bugs
        global entropy
        global realEntropy
        global criticals
        global key
        if ('-' in bugKey):
            return False
        if ("-" in key):
            entropy -= 1*(not(bugs[bugKey][1]))
            bugs[bugKey][1] = True
            return False
        if (key == bugs[bugKey][0]):
            entropy -= 1*(not(bugs[bugKey][1]))
            realEntropy -= 1*(not(bugs[bugKey][2]))
            criticals -= 1*(not(bugs[bugKey][2]))*bugs[bugKey][3]
            bugs[bugKey][1] = True
            bugs[bugKey][2] = True
            return True
        else:
            entropy -= 1*(not(bugs[bugKey][1]))
            bugs[bugKey][1] = True
            return True
default curBug = "---"
label FoundBug:
    kirill "Я уже отправил эту ошибку на рассмотрение."
    kirill "Отправить ли мне новый отчет?"
    menu:
        "Думаю прошлый отчет был неправильный":
            call CheckBug from _call_CheckBug

        "В прошлый раз я отправил всё верно.":
            $ key = "---"
            return
    return

label CheckBug:
    hide screen chooseBugType
    call screen entropy(bugKey=curBug)
    $ result = _return
    show screen entropy
    if result:
        kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
    else:
        kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"
    $ key = "---"
    return

label TreeSkinBug:
    $ curBug = "TreeSkin"
    if bugs[curBug][1]:
        call FoundBug from _call_FoundBug
    else:
        kirill "Что-то не так с текстурой дерева. Нужно отправить отчет."
        call CheckBug from _call_CheckBug_1
    return

label FirstBug:
    $ curBug = "FirstBug"
    hide screen chooseBugType
    call screen entropy(bugKey=curBug)
    $ result = _return
    show screen entropy
    if result:
        $ entropy -= 1
        $ realEntropy -= 1
        if (bugs[curBug][2]):
            oleg_matrix "Отличная работа! Вы отправили всё верно!"
            oleg_matrix "В дальнейшем вам будут встречаться различные ошибки, которые я буду не в состоянии распознать из вне."
            oleg_matrix "Будьте аккуратны и отправляйте правильные отчеты"
        else:
            oleg_matrix "Отчет был отправлен неверный..."
            oleg_matrix "Надеюсь это была лишь случайность. Если вы в дальнейшем будете отправлять мне неправильные отчеты, то потом мы не сможем исправить игру."
            oleg_matrix "А не отловив особо опасные ошибки... {w=0.5} Вы можете застрять в матрице..."
            kirill "Хорошо... {w=0.5} Буду аккуратен."
    else:
        $ entropy -= 1
        $ realEntropy -= 1
        oleg_matrix "Кирилл, Вы не заполнили все поля. Обязательно заполнять каждое, запомните это на следующий раз."
    $ key = "---"
    return


label WallBug:
     hide screen BugWall
     hide screen chooseBugType
     show screen BugWall(isFound=True)
     if bugs["WallBug"][1]:
         kirill "Опять эта невидимая стена не в том месте..."
         kirill "Но отправил ли я правильный отчет?"
         menu:
            "Думаю прошлый отчет был неправильный":
                call screen entropy(bugKey="WallBug")
                $ result = _return
                show screen entropy
                if result:
                    kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
                else:
                    kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"

            "В прошлый раз я отправил всё верно.":
                $ key = "---"
                return
     else:
         kirill "Нашел эту невидимую стену! Или чтобы это ни было..."
         oleg_matrix "Отличная работа, это одна из критических ошибок в игре, ведь из-за нее ты не можешь дальше проходить."
         oleg_matrix "Такие ошибки необходимо устранить. Возможно, если оставишь даже одну, то мне не получится выпустить Вас из матрицы."
         kirill "ЧТО?!"
         oleg_matrix "Спокойно, в виду их критичности их не должно быть сложно найти... {w=0.5} Я так думаю."
         oleg_matrix "Так или иначе отправьте отчет об этой ошибке. Судя по Вашим словам это ошибка совместимости, этого обьекта тут быть не должно."
         oleg_matrix "По крайне мере в таком виде."
         oleg_matrix "Причина наверняка в алгоритмах отображения из-за которых ты не можешь увидеть обьект, когда должен."
         oleg_matrix "А вот что находится перед вами понять должны вы сами, ведь я не вижу. Если это что-то правильной формы, то наверняка это стена или проход, вход в который ты не можешь увидеть. Тогда выберите пункт ГРАФИЧЕСКОЕ ОФОРМЛЕНИЕ."
         oleg_matrix "Если же объект неправильной формы, то проблема в нем самом. В таком случае выберите пункт ОБЪЕКТ в предмете ошибки."
         kirill "Хорошо, сейчас изучу и отправлю."
         call screen entropy(bugKey="WallBug")
         $ result = _return
         show screen entropy
         if result:
             kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
             oleg_matrix "Отличная работа!"
         else:
             kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"
             oleg_matrix "Тогда отправьте снова, вернувшись к предмету ошибки и подойдя к нему."
             kirill "Приму к сведению."
     $ key = "---"
     return

label FastTextBug:
    $ curBug = "FastText"
    if bugs[curBug][1]:
        call FoundBug from _call_FoundBug_1
    else:
         kirill_himself "Почему старик стал так тараторить? Думаю это ошибка, стоит отправить отчет."
         call CheckBug from _call_CheckBug_2
    return

label RockBug:
    $ curBug = "RockBug"
    if bugs[curBug][1]:
        call FoundBug from _call_FoundBug_2
    elif not(speed):
        with hpunch
        kirill_himself "Камень как камень..."
        kirill_himself "Хотя он какой-то неровный... Может если влетететь на него на большой скорости, то что-то будет?"
    else:
        with hpunch
        kirill "ААААА{nw}"
        hide eldrin
        hide screen BugRock
        hide screen RiverBug
        show bg thrownhall
        with flashbulb
        kirill "ЧТО?! {w=0.5}Я В ЗАМКЕ!?"
        kirill "Мне кажется меня тут буть не должно{nw}"
        with hpunch
        kirill "Дверь закрылась?!"
        kirill "И Короля нет... {w=0.5} Как мне закончить игру?"
        kirill_himself "Это однозначно ошибка. Нужно отправит отчет и вернуться обратно с помощью читов"
        call CheckBug from _call_CheckBug_3
        show bg river
        with pixellate
        if isEldrinShowed:
            show eldrin
        show screen BugRock
        show screen RiverBug
    return

label RepeatBugCode:
    kirill_himself "Итак, мне нужно написать небольшой код, чтобы провзаимодействовать со всеми жителями в городе."
    kirill_himself "С чего начать?"
    default res = ""
    $ res = ""
    menu:
        "foreach (NPC i in town.NPCs)":
            $ res += '1'
            jump RepeatBugCode1
        "foreach (Building i in town.Buildings)":
            $ res += '2'
            jump RepeatBugCode1
    return
label RepeatBugCode1:
    menu:
        "return player.DistanceTo(i)":
            $ res += '1'
        "player.InteractWith(i)":
            $ res += '2'
    if res == "12":
        jump RepeatBug
    else:
        kirill_himself "Вроде ничего не случилось..."
    return
label RepeatBug:
    $ curBug = "RepeatBug"
    villager "День идет. Тени длиннее становятся. Его Величество - Темный Король на горе бдит. Мы здесь сидим. Все как должно быть."
    if bugs[curBug][1]:
        call FoundBug from _call_FoundBug_3
    else:
        kirill_himself "(Снова про него...)"
        kirill "Темный Король - это кто?"
        villager "День идет. Тени длиннее становятся. Его Величество - Темный Король на горе бдит. Мы здесь сидим. Все как должно быть."
        kirill "Ты разве только что это не говорил?"
        villager "День идет. Тени длиннее становятся. Его Величество - Темный Король на горе бдит. Мы здесь сидим. Все как должно быть."
        kirill "Ясно... Это ещё один странный баг..."
        villager "День идет. Тени длиннее становятся. Его Величество - Темный Король на горе бдит. Мы здесь сидим. Все как должно быть."
        kirill_himself "Пора отправить отчет."
        call CheckBug from _call_CheckBug_4
    return

label RiverBug:
    $ curBug = "RiverBug"
    hide screen BugRock
    hide screen RiverBug
    hide eldrin
    if bugs[curBug][1]:
        call FoundBug from _call_FoundBug_4
    else:
        kirill "ААА! {nw}"
        show bg pixels
        with pixellate

        kirill_himself "И вот снова я выпал за текстуры..."
        kirill_himself "Думаю данная ошибка очень сильно может мешать прохождению, наверное её можно считать критической."
        kirill_himself "Пора отправить отчет."
        call CheckBug from _call_CheckBug_5
        if iter < 1:
            kirill "Олег! Вытащите меня из-за текстуры, пожалуйста"
            oleg_matrix "Ох... снова похожий баг? Сейчас"
        else:
            kirill_himself "А теперь выбираемся"
        show bg river
        with flashbulb
        if isEldrinShowed:
            show eldrin
    show screen BugRock
    show screen RiverBug
    return

label eldrinSpeechBug:
    $ curBug = "eldrinSpeechBug"
    if bugs[curBug][1]:
        kirill_himself "Опять шрифт поломался..."
        call FoundBug from _call_FoundBug_5
    else:
        kirill_himself "Размер шрифта слов Элдрина внезапно стал слишком огромным... Это невозможно читать..."
        kirill_himself "Думаю стоит отправить отчет об этой странной ошибке."
        call CheckBug from _call_CheckBug_6
    return

default hitCounter = 0
label StickBug:
    $ curBug = "stickBug"
    $ hitCounter += 1
    if bugs[curBug][1]:
         kirill_himself "Небо, конечно, было красивое, но мне не до этого..."
         call FoundBug
    elif hitCounter == 1:
         with hpunch
         kirill_himself "Странная палка..."
    elif hitCounter == 2:
         with hpunch
         kirill_himself "(И что я в ней нашел?)"
    elif hitCounter == 3:
         with hpunch
         kirill_himself "Почему я веду себя как ребенок?"
    else:
         with hpunch
         stop music
         stop sound
         kirill "{cps=50}ВООООООУ!!!{/cps}{nw}"
         hide screen BugTreeSkin
         hide screen StickBug
         show bg sky
         with flashbulb_long
         queue music ["forest1.mp3", "forest2.mp3"] loop
         kirill "{w=2} Вау... {w=2} Красота..."
         kirill "Это... наверняка не было запланировано... {w=1}"
         kirill "Надо бы {w=0.5} отправить отчет..."
         kirill "Но зачем торопиться?"
         hide screen AvatarFrame
         call CheckBug
         show screen AvatarFrame
         if iter == 0:
             kirill "Наверно... пора бы и уходить... {w=1} ОЛЕГ! Опустите меня вниз, пожалуйста."
             oleg_matrix "Вы куда-то улетели? Такой бывает из=за проблем с коллизией."
         else:
             kirill "Наверно... пора бы и уходить..."
         show bg forest
         with flashbulb
         play sound "ForestWhisper.mp3" loop volume 0.2
         show screen BugTreeSkin
         show screen StickBug
    return

label CastleWallBug:
    $ curBug = "CastleWallBug"
    if bugs[curBug][1]:
         call FoundBug
    elif not(speed and power):
        kirill_himself "Стены кажутся довольно крепкими..."
        kirill_himself "Интересно... А они разрушаемы?"
    else:
        hide screen CastleWallBug
        kirill_himself "Сила есть... Скорость... Проверим стену на прочность!"
        with hpunch
        hide eldrin
        play music "boss.mp3" loop
        show bg thrownhall
        with flashbulb
        show king

        king "Кто посмел потревожить мой покой?"

        kirill_himself "(Ой... Видимо разрушаемую стену поставили не там, где планировалось...)"

        king "Кто ты воин?"

        kirill_himself "(Пора отправлять отчет и возвращаться...)"

        call CheckBug

        hide king
        show bg castle
        with fade
        show eldrin
        show screen CastleWallBug
        queue music ["forest1.mp3", "forest2.mp3"] loop