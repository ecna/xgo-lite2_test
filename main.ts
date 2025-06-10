input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    X += 10
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    music.playTone(988, music.beat(BeatFraction.Whole))
    y += 10
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    
    music.playTone(262, music.beat(BeatFraction.Whole))
    y += -10
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    X += -10
})
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    
    z += -10
})
basic.showIcon(IconNames.Heart)
xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
let X = 28
let y = 69
let z = 150
music.setBuiltInSpeakerEnabled(false)
basic.forever(function on_forever() {
    xgo.Manipulator_clampX(X)
    xgo.Manipulator_clampZ(y)
    xgo.Manipulator_clamp(z)
})
