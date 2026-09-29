# Dream Entity GUI Theme Selector
# Based on the Ren'Py launcher GUI color-selector concept.
# This version uses the selected light-blue theme:
# Accent: #99ccff
# Background: #000000

define dream_gui.accent = "#99ccff"
define dream_gui.background = "#000000"
define dream_gui.text = "#ffffff"
define dream_gui.idle = "#888888"
define dream_gui.hover = "#cce6ff"

default dream_display = "Window"
default dream_text_speed = 0.5

screen dream_gui_swatches():

    # The selected Dream Entity theme.
    frame:
        style "empty"
        xysize (85, 60)

        add Solid("#000000")

        button:
            style "empty"
            xpadding 3
            ypadding 3
            xmargin 10
            ymargin 10

            idle_child Solid("#99ccff")
            hover_child Solid("#cce6ff")

            action NullAction()


screen dream_gui_demo():

    frame:
        style "empty"
        background Solid(dream_gui.background)
        xfill True
        yfill True
        padding (20, 20)

        vbox:
            spacing 8

            text "Display":
                style "empty"
                color dream_gui.accent
                size 24

            for option in ["Window", "Fullscreen", "Planetarium"]:

                textbutton option:
                    style "empty"

                    action SetScreenVariable("dream_display", option)

                    text_style "empty"
                    text_size 24

                    text_color dream_gui.idle
                    text_hover_color dream_gui.hover
                    text_selected_color dream_gui.text

                    selected_background Solid(
                        dream_gui.accent,
                        xsize=5
                    )

                    xmargin 4
                    ymargin 4
                    left_padding 21

            null height 30

            text "Text Speed":
                style "empty"
                color dream_gui.accent
                size 24

            bar:
                value ScreenVariableValue("dream_text_speed", 1.0)
                style "empty"

                base_bar Solid("#555555")
                hover_base_bar Solid("#777777")

                thumb Solid(dream_gui.accent, xsize=10)
                hover_thumb Solid(dream_gui.hover, xsize=10)

                ysize 30


screen dream_gui_selector():

    tag menu

    frame:
        style "empty"
        background Solid("#ffffff")
        xalign 0.5
        yalign 0.5
        xsize 1050
        ysize 650

        vbox:
            spacing 20
            xfill True
            yfill True

            text "Select Accent and Background Colors":
                color "#333333"
                size 30

            text "Dream Entity uses the selected theme below.":
                color "#555555"
                size 20

            hbox:
                spacing 25
                yfill True

                frame:
                    style "empty"
                    xsize 425
                    yfill True

                    vbox:
                        spacing 15

                        text "Selected Theme":
                            color "#333333"
                            size 22

                        text "Light Blue / Black":
                            color "#555555"
                            size 18

                        use dream_gui_swatches()

                        null height 20

                        text "Accent: #99ccff":
                            color "#333333"
                            size 18

                        text "Background: #000000":
                            color "#333333"
                            size 18

                frame:
                    style "empty"
                    xsize 450
                    yfill True
                    padding (5, 5)

                    use dream_gui_demo()

            hbox:
                xfill True
                spacing 20

                textbutton "Return":
                    style "dream_gui_button"
                    action Return(False)

                textbutton "Continue":
                    style "dream_gui_button"
                    action Return(True)


style dream_gui_button:
    background Solid("#eeeeee")
    hover_background Solid("#d9ecff")
    xpadding 25
    ypadding 12

style dream_gui_button_text:
    color "#333333"
    hover_color "#000000"
    size 22


label dream_gui_test:

    call screen dream_gui_selector

    if _return:
        "Dream Entity GUI initialized."
        "Accent color: #99ccff."
        "Background color: #000000."

    return
