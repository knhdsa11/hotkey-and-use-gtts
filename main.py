import pyperclip ,subprocess , os , keyboard , traceback
from gtts import gTTS 
from webbrowser import open_new

# ====== CONFIG ======
VLC_EXE = r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
LOG_FILE = r"C:\\mp3\\hotkey_log.txt"
SAVE_DIR = r"C:\\mp3"
os.makedirs(SAVE_DIR, exist_ok=True)
# ====================

def log_error(e):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(traceback.format_exc() + "\n")

def tts_clipboard():
    try:
        text = pyperclip.paste().strip()
        if not text:
            return

        mp3_file = os.path.join(SAVE_DIR, "tts_clip.mp3")  # ใช้ join ปลอดภัย
        tts = gTTS(text=text, lang="th")
        tts.save(mp3_file)

        subprocess.run([VLC_EXE, "--play-and-exit", mp3_file],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

        os.remove(mp3_file)
    except Exception as e:
        log_error(e)

def key(k1):
    try:
        if "http" in k1:
            open_new(k1)
        else:
            os.system(f'"{k1}"')
    except Exception as e:
        log_error(e)

# Hotkeys
keyboard.add_hotkey("ctrl+alt+g", key, args=("https://google.com",))
keyboard.add_hotkey("ctrl+alt+y", key, args=("https://youtube.com",))
keyboard.add_hotkey("ctrl+alt+s", key, args=("https://music.youtube.com",))
keyboard.add_hotkey("ctrl+alt+f", key, args=("https://web.facebook.com/TempTos1",))
keyboard.add_hotkey("ctrl+alt+m", key, args=("https://www.messenger.com/",))
keyboard.add_hotkey("ctrl+alt+c", key, args=("https://chatgpt.com",))
keyboard.add_hotkey("ctrl+alt+o", key, args=(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk",))
keyboard.add_hotkey("ctrl+alt+t", tts_clipboard)

try:
    keyboard.wait()
except Exception as e:
    log_error(e)
