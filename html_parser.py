from requests_html import HTMLSession

session = HTMLSession()

bateau_ivre = session.get(
    "https://fr.wikisource.org/wiki/Po%C3%A9sies_(Rimbaud)/%C3%A9d._Vanier,_1895/Le_Bateau_ivre"
)

strophes = [
    elem.full_text
    for elem in bateau_ivre.html.find("div")
    if "poem" in elem.attrs.get("class", [])
]
