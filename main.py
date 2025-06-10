def on_button_pressed_a():
    global X
    X += 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    global y
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    y += 10
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_logo_long_pressed():
    global y
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    y += -10
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_b():
    global X
    X += -10
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    global z
    z += -10
input.on_sound(DetectedSound.LOUD, on_sound_loud)

basic.show_icon(IconNames.HEART)
xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
X = 28
y = 69
z = 150
music.set_built_in_speaker_enabled(False)

def on_forever():
    xgo.Manipulator_clampX(X)
    xgo.Manipulator_clampZ(y)
    xgo.Manipulator_clamp(z)
basic.forever(on_forever)
