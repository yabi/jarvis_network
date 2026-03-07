import asyncio
import logging
import subprocess
import sys

logger = logging.getLogger(__name__)

try:
    import pyttsx3
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])
    import pyttsx3


class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init() if pyttsx3 else None

    async def speak(self, text):
        if self.engine:
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            print(f"[Mock TTS] {text}")
            await asyncio.sleep(len(text) * 0.05)
