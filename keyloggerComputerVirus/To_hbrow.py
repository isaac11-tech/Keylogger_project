import ctypes
import pynput.keyboard as keyboard

def get_current_language():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    hwnd = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(hwnd, None)
    layout_id = user32.GetKeyboardLayout(thread_id)
    lang_id = layout_id & (2**16 - 1)
    return lang_id  # מחזיר מזהה של השפה (עברית = 1037, אנגלית = 1033)

def filter(key):
    lang = get_current_language()

    if hasattr(key, 'char') and key.char is not None:
        if lang == 1037 and 'a' <= key.char <= 'z':  # עברית אבל מקלידים באנגלית
            return convert_to_hebrew(key.char)
        return key.char  # השפה מתאימה, אין צורך להמיר

    return str(key)  # מקשים מיוחדים

def convert_to_hebrew(char):
    mapping = {
        'a': 'ש', 'b': 'נ', 'c': 'ב', 'd': 'ג', 'e': 'ק', 'f': 'כ', 'g': 'ע',
        'h': 'י', 'i': 'ן', 'j': 'ח', 'k': 'ל', 'l': 'ך', 'm': 'צ', 'n': 'מ',
        'o': 'ם', 'p': 'פ', 'q': '/', 'r': 'ר', 's': 'ד', 't': 'א', 'u': 'ו',
        'v': 'ה', 'w': '\'', 'x': 'ס', 'y': 'ט', 'z': 'ז'
    }
    return mapping.get(char, char)
