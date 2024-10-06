from googletrans import Translator
from utils.logger import log_error

translator = Translator()

def detect_language(text):
    try:
        detected = translator.detect(text)
        return detected.lang
    except Exception as e:
        log_error(f"Language detection error: {e}")
        return "Unknown"

def translate_text(text, target_lang='en'):
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        log_error(f"Translation error: {e}")
        return "Translation failed."
