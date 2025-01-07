
# Step. 5
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di creare ogni tipo di Secret e provare a leggere i vari secret creati (che siano ConfigMap o Key-Value) tramite un pod
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)
- Secret (https://kubernetes.io/docs/concepts/configuration/secret/)

### Svolgimento:
I secret che andremo a creare sono: Opaque, kubernetes.io/service-account-token, kubernetes.io/dockercfg, kubernetes.io/dockerconfigjson, kubernetes.io/basic-auth,	kubernetes.io/ssh-auth, kubernetes.io/tls e bootstrap.kubernetes.io/token.

I secrets sono stati definiti in un file yml e sono poi stati creati utilizzando il comando "oc apply -f nome_file.yml". 

Il secret 0paque è stato invece creato senza andare a configurare un file yml, ma direttamente da terminale utilizzando il comando "oc create secret generic empty-secret".

La creazione dei secrets può essere verificata utilizzando " oc get secret", ma non tutti saranno visibili dall' output di questo comando.

Per la lettura dei secret attraverso i pod si può utilizzare il comando "oc get secret my-secret -o jsonpath='{.data.username}'"DA RIVEDERE