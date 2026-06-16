# Récupération de la Clé — XSS Stocké sur la page Feedback

## 🔍 Méthode d'exploitation

Pour ce flag, il faut se rendre sur la page **`/?page=feedback`**.

On y trouve un formulaire avec deux champs — **Name** et **Message** — permettant de signer un guestbook. Ce type de formulaire est potentiellement vulnérable au **XSS stocké** (Cross-Site Scripting).

### Test d'injection

On injecte dans un des champs le payload suivant :

```html
<script>alert("XSS")</script>
```

Si l'application **n'échappe pas le contenu soumis** avant de l'afficher, le script est sauvegardé en base de données dans la table `guestbook` et **exécuté dans le navigateur** de quiconque consulte la page.

La popup s'affiche bien, ce qui confirme que l'entrée est exécutée comme du **JavaScript sans être sanitisée**, et le flag est retourné par l'application.

---

## 🛡️ Recommandations

Pour se protéger contre le XSS stocké :

- **Échapper les entrées utilisateur** avant de les afficher (encoding HTML : `<` → `&lt;`, `>` → `&gt;`, etc.)
- **Valider et filtrer** les données côté serveur avant de les stocker en base de données
- Mettre en place une **Content Security Policy (CSP)** pour limiter l'exécution de scripts non autorisés
- Utiliser des librairies dédiées à la **sanitisation** des entrées (ex. `HTMLPurifier` en PHP)