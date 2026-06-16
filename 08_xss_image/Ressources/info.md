# Récupération de la Clé — Injection XSS via Data URI encodée en Base64

## 🔍 Méthode d'exploitation

Pour ce flag, il faut se rendre sur la **home page** du site et cliquer sur le **logo de la NSA**, qui amène sur la page :

```
/?page=media&src=nsa
```

On remarque que le paramètre **`src`** charge une ressource directement par son nom, ce qui suggère que le serveur **construit un chemin vers un fichier** à partir de cette valeur. Il est donc possible de manipuler ce paramètre pour y injecter du code.

---

### Étape 1 — Préparer le payload

On encode le payload en **Base64** pour contourner les éventuelles vérifications :

| Payload original | Encodé en Base64 |
|---|---|
| `<script>alert(1);</script>` | `PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=` |

---

### Étape 2 — Injecter via le paramètre src

On injecte le payload en utilisant une **Data URI** dans le paramètre `src` :

```
?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=
```

Le serveur décode la valeur et lit le fichier demandé, ce qui **déclenche le flag**.

---

## 🛡️ Recommandations

Pour se protéger contre ce type d'injection :

- **Valider et filtrer strictement** le paramètre `src` côté serveur en n'autorisant que des valeurs whitelistées
- **Ne jamais construire un chemin de fichier** directement à partir d'une entrée utilisateur
- **Bloquer les Data URIs** dans les paramètres attendant un nom de fichier
- Mettre en place une **Content Security Policy (CSP)** pour limiter les sources de contenu autorisées