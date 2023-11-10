import win32api
import win32con
import win32process
import ctypes

def get_application_name(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    h_process = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
    exe_path = win32process.GetModuleFileNameEx(h_process, 0)
    return exe_path


def getActiveWindowPos():
    user32 = ctypes.windll.user32
    window = user32.GetForegroundWindow()
    buffer_size = 512
    buffer = ctypes.create_unicode_buffer(buffer_size)
    name = get_application_name(window)
    name = name.split('\\')[-1].split('.')[0]

    rect = ctypes.wintypes.RECT()
    DWMWA_EXTENDED_FRAME_BOUNDS = 9
    ctypes.windll.dwmapi.DwmGetWindowAttribute(  ctypes.wintypes.HWND(window),
        ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
        ctypes.byref(rect),
        ctypes.sizeof(rect)
    )
    return (rect.left, rect.top, rect.right, rect.bottom), name