input.buttonA.onEvent(ButtonEvent.Click, function button_a_click() {
    light.showAnimation(light.colorWipeAnimation, 1000)
    light.clear()
})
input.buttonB.onEvent(ButtonEvent.Click, function button_b_click() {
    light.clear()
    light.setPixelColor(2, 0xff8000)
})
let RED = [255, 0, 0]
forever(function on_forever() {
    
})
