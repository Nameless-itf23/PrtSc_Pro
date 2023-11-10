import screen_brightness_control as sbc
import keyboard
import time
import screenshot
import save


def on_key_event(e):
    if keyboard.is_pressed('ctrl+alt+p'):
        save_func, name, now = screenshot.screenshot()
        save.save(save_func, name, now)
        brightness = sbc.get_brightness()[0]
        sbc.set_brightness(0)
        time.sleep(0.3)
        sbc.set_brightness(brightness)


if __name__ == "__main__":
    keyboard.hook(on_key_event)
    keyboard.wait()
