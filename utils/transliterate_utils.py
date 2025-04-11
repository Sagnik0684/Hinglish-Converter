from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

def transliterate_text(text, lang="hin"):
    if lang == "hin":
        return transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
    elif lang == "ben":
        return transliterate(text, sanscript.BENGALI, sanscript.ITRANS)
    else:
        return "Unsupported language for transliteration"