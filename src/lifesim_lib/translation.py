import gettext
import os as _os

LANGUAGES = [
    dir
    for dir in _os.listdir("./locale")
    if _os.path.isdir(_os.path.abspath("./locale/" + dir))
]

_ = lambda s: s

dir = _os.getcwd()
langs = {"en": None}

for lang in LANGUAGES:
    try:
        l = gettext.translation("lifesim", localedir=dir + "/locale", languages=[lang])
    except:
        pass
    else:
        langs[lang] = l

lang_map = {
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "ko": "한국인",
    "bn": "বাংলা",
    "id": "bahasa Indonesia",
    "np": "नेपाली ",
}

names = []
codes = []
for lang in langs:
    codes.append(lang)
    names.append(lang_map.get(lang, lang))

# Not using choice_input as we want translation.py to be the first thing loaded
for i, name in enumerate(names):
    print(f"{i+1}. {name}")
valid = False
while not valid:
    valid = True
    try:
        num = int(input())
    except ValueError:
        valid = False
        continue
    if not 1 <= num <= len(codes):
        valid = False
language = codes[num - 1]

if language != "en":
    langs[language].install()
    _ = langs[language].gettext
