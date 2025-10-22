# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# define e = Character('Эйлин', color="#c8ffc8")
# define asker = Character('Вопрошатель', color="#3c0f13")

define kirill = Character('Кирилл', color="#fffafa")
define kirill_himself = Character(None, what_color="#fffafa", who_color="#fffafa", what_italic=True)
define danil = Character('Данил', color="#0dbf28")
define oleg = Character('Олег', color="#1058e8")
define oleg_matrix = Character('Олег', what_color="#1058e8", who_color="#1058e8", what_font="Handjet-ExtraBold.ttf", what_size=32)
define system = Character(None, what_color="#fa0707", what_font="Handjet-ExtraBold.ttf", what_size=50, what_xalign=0.5, what_textalign=0.5, what_layout='subtitle')

define fade = Fade(1.0, 1.0, 0.5)
define fade_long = Fade(0.5, 1.5, 1)
define flashbulb = Fade(0.2, 0.0, 0.2, color='#fff')
define flashbulb_long = Fade(0.2, 2.0, 0.2, color='#fff')


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
# {font=Handjet-ExtraBold.ttf}{/font} - пресет для телефона и других гаджетов

# Игра начинается здесь:
label start:

    system "СБОЙ CИСТЕМЫ ВОЗРАТА"

#     e "The font tag changes the font, for example to {font=DejaVuSans-Bold.ttf}DejaVuSans-Bold.ttf{/font}."
#
#     e "Sometimes, changing to a bold font looks better than using the {{b} tag."

    window hide dissolve


    show bg room vr scene
    with pixellate

    #звуки искр
    pause 1000

    show bg room
    with fade

    #начало основной музыки

    pause 0.5
    window show dissolve

    kirill_himself "Вроде-бы все собрал. Готов идти"
    "{color=#06347d}{font=Handjet-ExtraBold.ttf}Новое сообщение от Данил{/font}{/color}"
    "{color=#0dbf28}{font=Handjet-ExtraBold.ttf}Привет. У меня есть хорошие новости, давай встретимся в обед{/color}{/font}"
    kirill_himself "мх... Я не в настроении"
    pause 1.0
    kirill_himself "Хотя, может что-то важное, наверное нужно сходить"

    show bg university
    with fade

    show danil calm

    kirill "Привет. Вот я и на месте"
    kirill "О чем хотел поговорить?"

    show danil interested

    danil "Как-то мало радости в человеке, для которого нашлось отличное рабочее место"

    kirill "О чем ты?"

    danil "Скажем так, есть знакомый знакомого, который работает в одной крутой {b}IT компании{/b}"

    kirill "и...?"

    show danil angry
    danil "Не перебивай!"
    pause 0.5
    show danil interested
    danil  "И так уж вышло, что им нужен тестировщик, готовый очень скоро выйти на работу"
    danil "Опыт не требуется"

    kirill "Хочешь сказать, этим тестировщиком должен быть я?"

    danil "Угадал!"
    danil "Ты уже долго ищешь работу, так вот замечательная возможность"

    kirill "Как-то это подозрительно..."
    kirill "Почему нужен именно меня?"

    danil "Я смог договориться, чтобы сначала рассмотрели тебя"

    kirill "{cps=25}Бред какой-то. {w=1.0} Кто вообще так работников набирает?{/cps}"

    show danil dissapointed
    danil "Вот поэтому ты и не можешь найти работу."
    danil "Тебе нужно хвататься за любую возможность, а ты ищешь только {i}идеальные{/i} варианты"

    kirill "{cps=25}Ладно, {w=0.3} ладно {w=0.3}, я схожу {w=0.3}, но не обещаю, что соглашусь на работу{/cps}"

    show danil interested
    danil "Вот и хорошо. Возьми визитку, там есть адрес, приходи завтра после пар"
    hide danil interested

    window hide dissolve

    show bg company
    with fade_long

    window show dissolve

    kirill_himself "Вроде на месте"
    kirill_himself "\"Interworld Association\" {w=0.5} хм... {w=0.5} странное название."
    kirill_himself "Что ж... {w=0.2} в путь"

    window hide dissolve

    show bg reception
    with Fade

    window show dissolve

    show oleg
    oleg "Здравствуйте, добро пожаловать в \"Interworld Association\" чем я могу помочь?"

    kirill "Здравствуйте, я по поводу работы тестировщиком. Меня сюда друг направил и..."

    oleg "А, вы, наверное, Кирилл. Мы вас ждали, идите за мной"

    window hide dissolve

    show bg office
    with Fade

    window show dissolve

    oleg "Итак, Кирилл, наша компания занимается разработкой крупных проектов направленных на создание и внедрение в общество новых технологий, которые помогут..."

    kirill "Извините, мне сказали что крупная компания, так почему..."

    oleg "Совершить прорыв в мире информационных технологий нового поколения, путем создания подходящих условий для простых людей..."

    kirill_himself "Он вообще меня слышит?"

    show oleg question
    oleg "Простите, вы вроде что-то спросили?"

    kirill "{cps=15}А...{w=0.5} Да...{w=0.5} Я...{/cps}"

    show oleg
    oleg "\"Immersive virtual space simulation\" - наш первый публичный проект, поэтому вы о нас не слышали"

    kirill "Это что-то вроде матрицы какой-то?"

    oleg "Можно и так сказать"

    oleg "Так что Кирилл, если решите у нас работать, пройдите тест, который я отправлю вам на почту, и приходите завтра, тогда все и решим"

    kirill "Хорошо, до свидания"
    hide oleg

    window hide dissolve

    show bg room
    with pixellate

    window show dissolve

    kirill_himself "{cps=25}Блин странно это все {w=1.0}. Крупная компания без проектов {w=0.2}, вместо теста на навыки мне прислали тест на стрессоустойчивость{w=0.2}, еще и этот Олег какой-то странный{/cps}"

    kirill_himself "Ладно, Данил был прав, может это та самая возможность, которую нельзя отпускать"
    kirill_himself "Все-таки надо попробовать. В конце концов, если мне не понравится, я могу уйти"

    window hide dissolve

    show bg office
    with fade

    window show dissolve

    show oleg
    kirill "Здравствуйте, я подумал, и решил, что готов приступить к работе"

    oleg "Очень хорошо, Кирилл. Вы набрали почти максимальный балл за тест, нам нужны такие работники"

    kirill "И когда мне приступать к работе?"

    oleg "Прямо сейчас. Пройдемте за мной"

    kirill "Ладно.{w=0.3}.{w=0.3}."

    window hide dissolve

    show bg room vr
    with pixellate

    window show dissolve

    oleg "Итак, Кирилл, ваша задача - провести первый запуск нашего проекта"
    show oleg:
        xalign 1.0
        yalign 1.0

    kirill "Вы поместите меня в матрицу?!"
    kirill "Это безопасно?!"

    oleg "Не волнуйтесь, все сделано по высшим стандартам безопасности"

    kirill "{cps=25}Тогда... {w=1.5} {b}Я готов начать{/b} {/cps}"
    hide oleg

    show bg room vr scene
    with fade_long

    oleg "Итак, запуск через {cps=15}3...{w=1.0} 2...{w=1.0} 1... {/cps}"
    #громкий хлопок, сирена и искры из шлема
    window hide dissolve

#     image bg room vr scene animated:
#         "bg room vr scene"
#         "bg room vr scene" with flashbulb
#         pause 1.0
#         "bg room vr scene" with hpunch
#         pause .2
#         "bg room vr scene" with flashbulb
#         pause 1.0
#         "bg room vr scene" with vpunch
#         pause .2
#         repeat
    show bg room vr scene
    with hpunch
    pause .2
    show bg room vr scene
    with flashbulb
    show bg room vr scene
    with vpunch
    pause .2

    window show dissolve
    system "СБОЙ CИСТЕМЫ ВОЗРАТА"

    show bg matrix
    with flashbulb_long

    kirill "Что, {w=1.0}{size=38} что произошло?! Где я?!{/size}"

    oleg_matrix "Кирилл, {w=0.5} Кирилл {w=0.5}, вы меня слышите?"

    kirill "Олег, это вы? Что произошло?"

    oleg_matrix "Произошел небольшой сбой, модуль возврата устройства вышел из строя"

    kirill "{size=38}Что это значит?!{w=0.5} Я застрял тут?!{w=0.5} Почему вы так спокойны?!{/size}"

    oleg_matrix "Кирилл, не нужно волноваться, мы вас вытащим, только потребуется ваша помощь"

    kirill "Что? Какая помощь?"

    oleg_matrix "Вы должны найти баги, которые сможет устранить наш разработчик, он не может найти баги сам, зато вы можете, проходя игру"
    oleg_matrix "Как найдете все баги, мы сможем вас вытащить"

    pause 1000







#     show asker
#
#     asker "Я задам тебе несколько вопросов"
#     python:
#         count = 0
#         ans = renpy.input("Сколько будет 3+5?")
#         flag1 = (ans == "8")
#
#     if flag1:
#         asker "Верно"
#         python:
#             ans = renpy.input("Сколько будет 3*5?")
#             count += 1
#             flag2 = (ans == "15")
#         if flag2:
#             asker "Ты на что-то способен. Но как насчет следующего?"
#             python:
#                 ans = renpy.input("Сколько будет cos³(π/3) * 5!")
#                 count += 1
#                 flag3 = (ans == "15")
#             if flag3:
#                 asker "Я надеюсь ты не просто так ввел тот же ответ"
#                 python:
#                     count += 1
#         else:
#             asker "Я в тебе разочарован"
#         asker "Ты дал [count] правильных ответа. Доволен собой?"
#     else:
#         asker "С ГЛАЗ МОИХ ПРОЧЬ!"
#
#     menu:
#         "Да, вполне":
#              "Не будь слишком самонадеян"
#              jump go
#         "Нет... Я стремлюсь к большему":
#              "Верно, никогда не останавливайся на достигнутом"
# #
# #     choice1_yes:
# #          asker "Не будь слишком самонадеян"
# #          jump choice1_done
# #
# #     choice1_no:
# #          asker "Верно, никогда не останавливайся на достигнутом"
# #          jump choice1_done
# #
# #     choice1_done:
# #          asker "Я ВИЖУ ТЕБЯ"
#
# label after_menu:
#     return
# label go:
#     asker "ТЫ КУДА?!"
#     return
