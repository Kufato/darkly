Pour ce flag il faut se rendre dans la page "/?page=member".

Ici on trouve un form sur lequel on nous demande de rentrer un l'id d'un membre. Lorsque l'on rentre un id, par exemple "1", on nous donne des information structuré de cette manière :

ID: 1 
First name: one
Surname : me

On remarque bien que on est sur une structure typique du sql et que par conséquent on doit pouvoir récupérer des information via des injections SQL. On peut ensuite chercher à lister toutes les tables avec leurs colonnes et voir si des informations nous semble utiles. On utilise donc cette commande SQL :

1 or 1=1 UNION SELECT table_name, column_name FROM information_schema.columns-- -

Cette requête retourne toutes les tables avec leurs colonnes. On repère la table users et on note ses colonnes : user_id, first_name, last_name, town, country, planet, Commentaire et countersign. C'est cette dernière colonne, combinée à Commentaire, qui va nous intéresser. On va donc récupérer les données de cette table via cette commande SQL :

1 or 1=1 UNION SELECT Commentaire, countersign FROM users-- -

Dans les données que l'on récupère on tombe sur ceci qui nous donne la marche à suivre :

ID: 1 or 1=1 UNION SELECT Commentaire, countersign FROM users-- - 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28

Il nous suffit de casser les hash de la donnée présente dans la colonne "Surname" qui est encodé en md5 (comme pour le reste des codes du projet). On peut aussi le passer dans décrypteur comme CrackStation qui trouvera tout seul que c'est encodé en md5. Le résultat nous donne "FortyTwo".

On passe ensuite tous les caractères en minuscule comme dit dans l'indice. On applique ensuite le hash SHA-256 dessus pour trouver le flag via cette commande shell :

echo -n "fortytwo" | sha256sum