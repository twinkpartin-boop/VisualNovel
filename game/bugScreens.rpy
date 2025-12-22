#bugTree 1035 446

screen BugTreeSkin():
    layer "master"
    vbox:
        xpos 1035 ypos 446
        imagebutton:
            idle "BugTree.png"
            hover "BugTreeHover.png"

            action Call("TreeSkinBug")
