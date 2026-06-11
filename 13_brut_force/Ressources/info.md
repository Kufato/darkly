Dans la page de login, on présuppose que l'administrateur s'appelle admin, et on envoie plein de requetes avec plein de mot de passes differents.

On envoie ces requetes via curl, et on guette le mot "flag".

Solution : faire que l'admin ne s'appelle pas admin, mettre un mot de passe plus sécurisé, et bloquer les ip qui font beaucoup trop de requetes pour se connecter.
