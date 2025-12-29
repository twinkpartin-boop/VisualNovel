#bugTree 1035 446
#bugWall 761 99
#rockBug 1564 448
#riverBug 619 186
#StickBug 1598 953
#CastleWallBug 343 694
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

screen BugRock(untouchable=False):
    layer "master"
    default hover = "RockHover.png"
    if untouchable:
        $ hover = "Rock.png"
    vbox:
        xpos 1564 ypos 448
        imagebutton:
            idle "Rock.png"
            hover hover
            if untouchable:
                action NullAction()
            action Call("RockBug")

screen RiverBug():
    layer "master"
    vbox:
        xpos 619 ypos 186
        imagebutton:
            idle "River.png"
            hover "RiverHover.png"
            action Call("RiverBug")

screen StickBug():
    layer "master"
    vbox:
        xpos 1598 ypos 953
        imagebutton:
            idle "Stick.png"
            hover "StickHover.png"
            action Call("StickBug")

screen CastleWallBug():
    layer "master"
    vbox:
        xpos 343 ypos 694
        imagebutton:
            idle "CastleWall.png"
            hover "CastleWallHover.png"
            action Call("CastleWallBug")