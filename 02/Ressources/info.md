Pour ce flag il faut se render sur la page disponible en cliquant sur le "© BornToSec" disponible dans le footer.

En inspectant cette page, on y voit des commentaire nous donnant des indices sur la marche à suivre. Il faut ici modifier le Referer et le User-Agent (via un curl par exemple) avec les valeurs données dans les commentaires de la page.

Le Referer est un header envoyé automatiquement par le navigateur qui indique d'où vient l'utilisateur, c'est-à-dire l'URL de la page depuis laquelle il a cliqué sur un lien. Ici il faut le modifier par "https://www.nsa.gov/"

Le User-Agent est un header envoyé par le navigateur qui s'identifie auprès du serveur : quel navigateur, quelle version, quel OS. Ici il faut le modifier par "ft_bornToSec"

On peut donc créer une petite commande pour modifier ces infos pour pouvoir récupérer le flag :

curl -H "Referer: https://www.nsa.gov/" \
     -H "User-Agent: ft_bornToSec" \
     http://127.0.0.1:8080/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f | grep flag


Pour s'en protéger il faut utiliser des tokens (JWT, sessions), créer un système d'authentification plus propre (login, mot de passe) ou bien exclure les headers clients en les considérant comme non fiable.