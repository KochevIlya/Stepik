d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
with open("cyrillic.txt", encoding="utf-8") as fin, open("transliteration.txt", "w") as fout:
    itxt = fin.read()
    result_str = ""
    for c in itxt:
        if c.lower() not in d.keys():
            result_str += c
        else:
            result_str += d[c.lower()] if c.islower() else d[c.lower()].title()
    fout.write(result_str)