# Récupération de la Clé — Page de Recovery

## 🔍 Méthode d'exploitation

Pour cette clé, il faut se rendre dans la **page de recovery du mot de passe** (`/index.php?page=recover#`).

Ici, il faut **inspecter la page** pour trouver que dans le **code HTML du formulaire** il y a l'**adresse de recovery écrite en dur**. Il suffit de la **modifier dans l'inspecteur** pour avoir accès à la clé.

---

## 🛡️ Recommandation

Pour éviter ce genre de problème, il ne faut **pas laisser ce genre d'information dans le front** et les **gérer dans le back** du site/webapp.