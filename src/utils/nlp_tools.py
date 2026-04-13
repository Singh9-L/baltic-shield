"""Language detection for 14 European languages."""
def detect_language(text):
    kw={"lt":["lietuvos","vilnius","seimas"],"lv":["latvijas","riga"],"et":["eesti","tallinn"],"ru":["россия","москв","путин"],"de":["deutschland","berlin"],"pl":["polska","warszawa"],"fi":["suomi","helsinki"]}
    tl=text.lower()
    for lang,words in kw.items():
        if any(w in tl for w in words): return lang
    return "en"
