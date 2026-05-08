from io import BytesIO
from gtts import gTTs


class TextToSpeech:
    def speak(self, text, lang="en"):
        cleaned = (text or "").strip()

        if not cleaned:
            return

        buffer = BytesIO()
        gTTs(text=cleaned, lang=lang).write_to_fp(buffer)
        buffer.seek(0)

        return buffer.read()
