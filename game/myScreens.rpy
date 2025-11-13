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

            action Show("chooseBugType")

screen chooseBugType():
    frame:
        xpos 0 ypos 100

        has vbox

        textbutton "Тип бага":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"

            action Notify("Здесь что-то будет")

        textbutton "Описание бага":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"

            action Notify("Здесь что-то будет")

        textbutton "Описание бага":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"

            action Notify("Здесь что-то будет")

        textbutton "Закрыть":
            text_idle_color "#ffffff"
            text_hover_color "#0b08a1"

            action Hide("chooseBugType")
