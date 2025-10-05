# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define asker = Character('Вопрошатель', color="#3c0f13")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show asker

    asker "Я задам тебе несколько вопросов"
    python:
        count = 0
        ans = renpy.input("Сколько будет 3+5?")
        flag1 = (ans == "8")

    if flag1:
        asker "Верно"
        python:
            ans = renpy.input("Сколько будет 3*5?")
            count += 1
            flag2 = (ans == "15")
        if flag2:
            asker "Ты на что-то способен. Но как насчет следующего?"
            python:
                ans = renpy.input("Сколько будет cos³(π/3) * 5!")
                count += 1
                flag3 = (ans == "15")
            if flag3:
                asker "Я надеюсь ты не просто так ввел тот же ответ"
                python:
                    count += 1
        else:
            asker "Я в тебе разочарован"
        asker "Ты дал [count] правильных ответа. Доволен собой?"
    else:
        asker "С ГЛАЗ МОИХ ПРОЧЬ!"

    menu:
        "Да, вполне":
             "Не будь слишком самонадеян"
             jump go
        "Нет... Я стремлюсь к большему":
             "Верно, никогда не останавливайся на достигнутом"
#
#     choice1_yes:
#          asker "Не будь слишком самонадеян"
#          jump choice1_done
#
#     choice1_no:
#          asker "Верно, никогда не останавливайся на достигнутом"
#          jump choice1_done
#
#     choice1_done:
#          asker "Я ВИЖУ ТЕБЯ"

label after_menu:
    return
label go:
    asker "ТЫ КУДА?!"
    return
