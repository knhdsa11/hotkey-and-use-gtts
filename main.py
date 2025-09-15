import pyperclip, subprocess, os, keyboard, traceback , time
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

        mp3_file = os.path.join(SAVE_DIR, "tts_clip.mp3")
        tts = gTTS(text=text, lang="th")
        tts.save(mp3_file)

        subprocess.run([VLC_EXE, "--play-and-exit", mp3_file],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

        if os.path.exists(mp3_file):
            os.remove(mp3_file)
    except Exception as e:
        log_error(e)

def key(k1):
    try:
        if os.path.exists(k1):
            subprocess.Popen([k1], shell=True)
        elif "http" in k1:
            open_new(k1)
        else:
            open_new(k1)  # fallback
    except Exception as e:
        log_error(e)

def k12(hotkey, mode, command):
    try:
        keyboard.add_hotkey(hotkey, mode, args=(command,))
    except Exception as e:
        log_error(e)

# ==== HOTKEYS ====
k12("ctrl+alt+g", key, "https://google.com")
k12("ctrl+alt+y", key, "https://youtube.com")
k12("ctrl+alt+s", key, "https://music.youtube.com")
k12("ctrl+alt+f", key, "https://web.facebook.com/TempTos1")
k12("ctrl+alt+m", key, "https://www.messenger.com/")
k12("ctrl+alt+c", key, "https://chatgpt.com")
k12("ctrl+alt+4", key, "")
k12("ctrl+alt+d", key, r"c:\Users\TEMPTOS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")
k12("ctrl+alt+l", key, r"c:\Users\TEMPTOS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\LINE\LINE.lnk")
k12("ctrl+alt+o", key, r"c:\Program Files\obs-studio\bin\64bit\obs64.exe")
k12("ctrl+alt+6", key, "https://copilot.microsoft.com/")
k12("ctrl+alt+t", lambda: tts_clipboard(), None)

# ==== WAIT FOR HOTKEYS ====
keyboard.wait()
