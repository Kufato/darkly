# Acces a etc/passwd

## 🔍 Méthode d'exploitation

Ici on cherche a remonter a la racine du site et avoir acces a **/etc/passwd**, fichier dans lequel on retrouve la liste complete des utilisateurs.

Pour ca je teste l'url avec de plus en plus de retour ne arriere dans l'arborescence des fichiers jusqu'a ce que le flag arrete le programme.

---

## 🛡️ Recommandation

Mettre des restrictions d'acces sur les fichiers sensibles comme lui.
