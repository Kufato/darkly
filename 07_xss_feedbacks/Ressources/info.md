Pour ce flag il faut se rendre dans la page "/?page=feedback".

Ici on trouve un formulaire avec deux champs : Name et Message, permettant de signer un guestbook. Ce type de formulaire est potentiellement vulnérable au XSS stocké (Cross-Site Scripting). On teste donc en injectant dans un des champs le mot "script" ou "alert".

<script>alert("XSS")</script>

Si l'application n'échappe pas le contenu soumis avant de l'afficher, le script sera sauvegardé en base de données dans la table guestbook et exécuté dans le navigateur de quiconque consulte la page. La popup s'affiche bien, ce qui confirme que l'entrée est exécutée comme du JavaScript sans être sanitisée, et le flag est retourné par l'application.