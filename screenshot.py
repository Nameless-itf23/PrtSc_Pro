import ctypes
import mss
from screeninfo import get_monitors
import datetime


def getActiveWindowPos():
    user32 = ctypes.windll.user32
    window = user32.GetForegroundWindow()
    buffer_size = 512
    buffer = ctypes.create_unicode_buffer(buffer_size)
    user32.GetWindowTextW(window, buffer, buffer_size)
    name = buffer.value.split(' - ')[-1]

    rect = ctypes.wintypes.RECT()
    DWMWA_EXTENDED_FRAME_BOUNDS = 9
    ctypes.windll.dwmapi.DwmGetWindowAttribute(  ctypes.wintypes.HWND(window),
        ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
        ctypes.byref(rect),
        ctypes.sizeof(rect)
    )
    return (rect.left, rect.top, rect.right, rect.bottom), name


def screenshot():
    W, H = get_monitors()[0].width, get_monitors()[0].height

    with mss.mss() as sct:
        (left, top, right, bottom), name = getActiveWindowPos()
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
