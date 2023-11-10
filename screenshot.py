import mss
from screeninfo import get_monitors
import datetime
import win32controller


def screenshot():
    W, H = get_monitors()[0].width, get_monitors()[0].height

    with mss.mss() as sct:
        (left, top, right, bottom), name = win32controller.getActiveWindowPos()
        left = min(max(left, 0), W)
        top = min(max(top, 0), H)
        right = min(max(right, 0), W)
        bottom = min(max(bottom, 0), H)
        print(name)
        print(f'left: {left} top: {top} right: {right} bottom: {bottom}')
        monitor = {'left': left, 'top': top, 'width': right-left, 'height': bottom-top}

        sct_img = sct.grab(monitor)
        now = datetime.datetime.now()

        return lambda output: mss.tools.to_png(sct_img.rgb, sct_img.size, output=output), name, now
