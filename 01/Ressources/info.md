Pour cette clé il faut se concentrer dans le footer du site.

Ici le but est de trouver que les 3 icones qui permettent une redirection sur les réseaux sociaux n'ont pas les urls des dits réseaux en dur mais passe par une redirection.
En modifant simplement le site de refirection on récupère le flag.

Pour s'en protéger il faut soit définir une liste de redirection possible dans le back du site :

$allowed = ['facebook', 'twitter', 'instagram'];
if (in_array($_GET['site'], $allowed)) {
    $urls = ['facebook' => 'https://facebook.com', ...];
    header('Location: ' . $urls[$_GET['site']]);
}

Ou bien écrire en dur les urls vers lesquels on redirige les users :

<a href="https://facebook.com">...</a>