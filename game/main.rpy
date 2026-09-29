default sleep_clicks = 0
default sleep_timer = 0.0

screen sleep_minigame():

    timer 0.1 repeat True action SetVariable(
        "sleep_timer",
        sleep_timer + 0.1
    )

    if sleep_timer >= 2.0:
        $ sleep_clicks = 0
        $ sleep_timer = 0.0

        text "You try sleeping, but your thoughts won't let you.":
            xalign 0.5
            yalign 0.4

    else:
        textbutton "Sleep":
            xalign 0.5
            yalign 0.5

            action [
                SetVariable("sleep_clicks", sleep_clicks + 1),
                SetVariable("sleep_timer", 0.0)
            ]

    if sleep_clicks >= 20:
        timer 0.0 action Return()


label start:

    "Test the sleep minigame."

    call screen sleep_minigame

    "You successfully fell asleep."

    return
