#bugTree 1035 446
#bugWall 761 99
init python:
    def CallEntropy(bugKey):
        renpy.call_screen("entropy", bugKey=bugKey)
screen BugTreeSkin():
    layer "master"
    vbox:
        xpos 1035 ypos 446
        imagebutton:
            idle "BugTree.png"
            hover "BugTreeHover.png"

            action Call("TreeSkinBug")

screen BugWall(isFound=False):
    layer "master"
    vbox:
        xpos 761 ypos 99
        imagebutton:
            idle "InvicibleIdle.png"
            hover "Invicible.png"
            if (isFound):
                action NullAction()
            action Call("WallBug")
