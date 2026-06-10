Pour ce flag il faut encore regarder ce qu'il y a dans le fichier /robots.txt du site.

On y trouve un dossier nommé /whatever/ qui nous donne un fichier nommé "htpasswd" contenant ceci : root:437394baff5aa33daa618be47b75cb49
En le décryptant via md5 on trouve ceci : qwerty123@

On peut ensuite se rendre sur la page /admin et rentrés les informations dans le formulaire de login (login : root et pawword : qwerty123@) pour trouver le flag.

Comme pour la faille du dossier /.hidden/ il ne faut pas laisser de données sensible dans le fichier robots.txt ou bien protéger ce fichier pour que les users n'y ai pas accés facilement.