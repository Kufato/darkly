# Tricher dans le sondage

## 🔍 Méthode d'exploitation

Sur la page survey, la **valeur de vote maximale est de 10**, pourtant une moyenne est a plus de 4000, ce qui met la puce à l'oreille.

En **inspectant** puis augmantant la valeur associée à une option, on peut voter une fois avec une grosse valeur, ce qui fausse completement le sondage.

---

## 🛡️ Recommandation

Verifier dans le code du site que la valeur soit bien comprise entre 1 et 10.

