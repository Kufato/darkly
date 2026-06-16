# Récupération de la Clé — Redirection via le Footer

## 🔍 Méthode d'exploitation

Pour cette clé, il faut se concentrer sur le **footer du site**.

Le but est de trouver que les **3 icônes de redirection vers les réseaux sociaux** n'ont pas les URLs des réseaux en dur, mais passent par une **redirection dynamique**. En **modifiant simplement le site de redirection**, on récupère le flag.

---

## 🛡️ Recommandations

Pour s'en protéger, deux approches sont possibles :

### Option 1 — Définir une liste blanche de redirections dans le back

```php
$allowed = ['facebook', 'twitter', 'instagram'];
if (in_array($_GET['site'], $allowed)) {
    $urls = ['facebook' => 'https://facebook.com', ...];
    header('Location: ' . $urls[$_GET['site']]);
}
```

### Option 2 — Écrire les URLs en dur dans le HTML

```html
<a href="https://facebook.com">...</a>
```