"""Keyword dictionaries used by the Flavour dialect transpiler and lexer."""
BASE = {
    "if":"if", "elif":"elif", "else":"else", "while":"while", "for":"for",
    "in":"in", "print":"print", "True":"True", "False":"False", "None":"None",
    "and":"and", "or":"or", "not":"not", "def":"def", "return":"return",
    "class":"class", "try":"try", "except":"except", "finally":"finally",
    "raise":"raise", "import":"import", "from":"from", "with":"with", "as":"as",
    "break":"break", "continue":"continue", "pass":"pass", "lambda":"lambda",
}
HINGLISH = {
    "warna_agar":"elif", "agar":"if", "warna_agar":"elif", "warna":"else", "jabtak":"while",
    "har":"for", "mein":"in", "likho":"print", "sahi":"True",
    "galat":"False", "shunya":"None", "aur":"and", "ya":"or",
    "nahi":"not", "banao":"def", "bhejo":"return", "koshish":"try",
    "pakdo":"except", "aakhir":"finally", "uthao":"raise",
    "lao":"import", "se":"from", "saath":"with", "jaisa":"as",
    "todo":"break", "jaari":"continue", "khaali":"pass",
}
GENZ = {
    "lowkey":"if", "highkey":"elif", "deadass":"else", "spin":"while",
    "vibe":"for", "wit":"in", "spill":"print", "fr":"True",
    "cap":"False", "sus":"None", "plus":"and", "either":"or",
    "nope":"not", "cook":"def", "returnz":"return",
}
DIALECTS = {
    "python": {**BASE},
    "hinglish": {**BASE, **HINGLISH},
    "genz": {**BASE, **GENZ},
    "custom": {**BASE, **HINGLISH},
}
# Multiword aliases are represented by one source token in the lexer.
MULTIWORD = {"warna_agar": "elif"}

def get_dialect(name="hinglish"):
    try:
        return DIALECTS[name.lower()].copy()
    except (KeyError, AttributeError):
        raise ValueError("Unknown dialect {!r}. Available: {}".format(name, ", ".join(sorted(DIALECTS))))
