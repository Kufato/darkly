Dans les cookies, on peut observer un cookie "i_am_admin".

Sa valeur est un hash en md5 du mot "false". En remplaçant cette valeur par le hash de "true" en md5, le flag apparait car nous sommes devenu admin.

Solution : ne pas stocker le fait d'etre admin dans un cookie modifiable, mais plutot par reconnaissance d'utilisateur.
