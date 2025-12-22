init python:
    def CheckKey(bugKey="---"):
        global bugs
        if ('-' in bugKey):
            return False
        if ("-" in user.key):
            return False
        if (user.key == bugs[bugKey][0]):
            global entropy
            entropy -= 1*(not(bugs[bugKey][1]))
            global realEntropy
            realEntropy -= 1*(not(bugs[bugKey][2]))
            bugs[bugKey][1] = True
            bugs[bugKey][2] = True
            return True
        else:
            global entropy
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