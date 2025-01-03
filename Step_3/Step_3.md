
# Step. 3
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di creare Quotas, applicarle e verificarne l'effettivo funzionamento al superamento delle soglie indicate
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)
- Quotas (https://docs.openshift.com/container-platform/4.8/applications/quotas/quotas-setting-per-project.html)
### Svolgimento:

Per creare le Quotas bisogna per prima cosa andare a definirle in un file yaml. Pertanto si può creare il file quota.yaml, dove andremo ad effettuarne la scrittura.
Successivamente si può andare a farle partire con il comando "oc create -f quota.yaml". 
Per verificare che sia tutto corretto si può utilizzare il comando "oc describe quota -n formazione-sou", il quale mostrerà a video tutte le quotas a confronto con i valori di sistema.