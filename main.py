def button_a_click():
    light.show_animation(light.color_wipe_animation, 1000)
    light.clear()
input.button_a.onEvent(ButtonEvent.CLICK, button_a_click)
def button_b_click():
    light.clear()
    light.set_pixel_color(2, 0xff8000)
input.button_b.onEvent(ButtonEvent.CLICK, button_b_click)
RED = [255, 0, 0]
def on_forever():
    pass
forever(on_forever)