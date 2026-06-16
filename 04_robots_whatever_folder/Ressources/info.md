# Récupération de la Clé — Exposition de htpasswd via robots.txt

## 🔍 Méthode d'exploitation

Pour ce flag, il faut à nouveau regarder le contenu du fichier **`/robots.txt`** du site.

On y trouve un dossier nommé **`/whatever/`** qui contient un fichier **`htpasswd`** avec le contenu suivant :

```
root:437394baff5aa33daa618be47b75cb49
```

En **déchiffrant le hash via MD5**, on obtient le mot de passe : **`qwerty123@`**

On peut ensuite se rendre sur la page **`/admin`** et entrer les identifiants dans le formulaire de login pour récupérer le flag :

- **Login** : `root`
- **Mot de passe** : `qwerty123@`

---

## 🛡️ Recommandations

Comme pour la faille du dossier `/.hidden/` :

- **Ne pas laisser de données sensibles dans `robots.txt`** — ce fichier est accessible publiquement et peut exposer des chemins critiques
- **Protéger ou restreindre l'accès à `robots.txt`** pour limiter la surface d'attaque visible par les utilisateurs