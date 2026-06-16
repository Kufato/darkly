# Récupération de la Clé — Manipulation des Headers HTTP

## 🔍 Méthode d'exploitation

Pour ce flag, il faut se rendre sur la page disponible en cliquant sur le **"© BornToSec"** dans le footer.

En **inspectant cette page**, on y trouve des **commentaires HTML** donnant des indices sur la marche à suivre. Il faut modifier deux headers HTTP — le **Referer** et le **User-Agent** — avec les valeurs indiquées dans ces commentaires (via `curl` par exemple).

### Headers à modifier

- **Referer** — Header envoyé automatiquement par le navigateur indiquant l'URL de la page depuis laquelle l'utilisateur vient. Valeur à utiliser : `https://www.nsa.gov/`

- **User-Agent** — Header envoyé par le navigateur pour s'identifier auprès du serveur (navigateur, version, OS). Valeur à utiliser : `ft_bornToSec`

### Commande pour récupérer le flag

```bash
curl -H "Referer: https://www.nsa.gov/" \
     -H "User-Agent: ft_bornToSec" \
     http://127.0.0.1:8080/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f | grep flag
```

---

## 🛡️ Recommandations

Pour s'en protéger, plusieurs approches sont possibles :

- Utiliser des **tokens** (JWT, sessions) pour l'authentification
- Mettre en place un **système d'authentification plus robuste** (login, mot de passe)
- **Ne pas faire confiance aux headers clients** (Referer, User-Agent) et les considérer comme non fiables