init python:
    def CheckKey(bugKey="---"):
        global bugs
        global entropy
        global realEntropy
        global criticals
        if ('-' in bugKey):
            return False
        if ("-" in user.key):
            bugs[bugKey][1] = True
            return False
        if (user.key == bugs[bugKey][0]):
            entropy -= 1*(not(bugs[bugKey][1]))
            realEntropy -= 1*(not(bugs[bugKey][2]))
            criticals -= 1*(not(bugs[bugKey][2]))*bugs[bugKey][3]
            bugs[bugKey][1] = True
            return True
        else:
            entropy -= 1*(not(bugs[bugKey][1]))
            bugs[bugKey][1] = True
            return True

label TreeSkinBug:
    $ user.key = "---"
    if bugs["TreeSkin"][1]:
        kirill "Я уже отправил эту ошибку на рассмотрение."
        kirill "Отправить ли мне новый отчет?"
        menu:
            "Думаю прошлый отчет был неправильный":
                call screen entropy(bugKey="TreeSkin")
                $ result = _return
                show screen entropy
                if result:
                    kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
                else:
                    kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"

            "В прошлый раз я отправил всё верно.":
                return
    else:
        kirill "Что-то не так с текстурой дерева. Нужно отправить отчет."
        call screen entropy(bugKey="TreeSkin")
        $ result = _return
        show screen entropy
        if result:
            kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
        else:
            kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"
    return

label WallBug:
     $ user.key = "---"
     hide screen BugWall
     show screen BugWall(isFound=True)
     if bugs["WallBug"][1]:
         kirill "Опять эта невидимая стена не в том месте..."
         kirill "Но отправил ли я правильный?"
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
     return

label FastTextBug:
    $ user.key = "---"
    if bugs["FastText"][1]:
        kirill "Опять он начал быстро тараторить, но я уже отправил эту ошибку на рассмотрение."
        kirill "Отправить ли мне новый отчет?"
        menu:
            "Думаю прошлый отчет был неправильный":
                call screen entropy(bugKey="FastText")
                $ result = _return
                show screen entropy
                if result:
                    kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
                else:
                    kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"

            "В прошлый раз я отправил всё верно.":
                return
    else:
         kirill_himself "Почему старик стал так тараторить? Думаю это ошибка, стоит отправить отчет."
         call screen entropy(bugKey="FastText")
         $ result = _return
         show screen entropy
         if result:
             kirill "Отчет отправил. {w=0.5} Надеюсь правильно."
         else:
             kirill "Я НЕ ЗАПОЛНИЛ ВСЁ!"
    return
