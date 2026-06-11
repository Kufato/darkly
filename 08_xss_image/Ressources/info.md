Pour ce flag il faut se rendre sur la home page du site et cliquer sur le logo de la NSA, il nous amène sur cette page : /?page=media&src=nsa.

On remarque que le paramètre src charge une ressource directement par son nom, ce qui suggère que le serveur construit un chemin vers un fichier à partir de cette valeur. On peut donc essayer de manipuler ce paramètre pour y insérer du code. On encode notre payload que on veut injecter en base64 pour bypass les vérifications 

?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=

PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4= est le base64 de <script>alert(1);</script>

Le serveur décode la valeur et lit le fichier demandé, ce qui déclenche le flag.