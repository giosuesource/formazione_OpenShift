
# Step. 5
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di creare ogni tipo di Secret e provare a leggere i vari secret creati (che siano ConfigMap o Key-Value) tramite un pod
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)
- Secret (https://kubernetes.io/docs/concepts/configuration/secret/)

### Svolgimento:
I secret che andremo a creare sono: Opaque, kubernetes.io/service-account-token, kubernetes.io/dockercfg, kubernetes.io/dockerconfigjson, kubernetes.io/basic-auth,	kubernetes.io/ssh-auth, kubernetes.io/tls e bootstrap.kubernetes.io/token.

I secrets sono stati definiti in un file yml e sono poi stati creati utilizzando il comando "oc apply -f nome_file.yml". 

Il secret 0paque è stato invece creato senza andare a configurare un file yml, ma direttamente da terminale utilizzando il comando "kubectl create secret generic \        
       passwd-secret --from-literal=password=topolino".

La creazione dei secrets può essere verificata utilizzando " oc get secret", ma non tutti saranno visibili dall' output di questo comando.

Per verificare la lettura dei secret attraverso i pod si può prendere come riferimento il pod 0paque. Si può utilizzare il comando "oc describe secret passwd-secret" per essere sicuri della creazione dello stesso. 
Successivamente si dovrà andare a creare un file pod_env.yml per consentire la creazione del Pod, che sarà configurato come Database Mysql per consentire di verificare il secret grazie al login al database.

Dopo aver scritto il file yml, si deve utilizzare il comando "oc apply -f pod_env.yml" per lanciare il Pod e il comando "oc exec -it database-server -c con -- bash" per la connessione al database. Una volta connessi, dal terminale del database possiamo utilizzare il comando "mysql -u root -p" per effettuare l' autenticazione: verrà infatti richiesta la password contenuta nel secret. Se il login con la suddetta password andrà a buon fine, l' esercizio sarà corretto.

Per verificare la lettura attraverso Config Map, si può inizialmente usare il comando "oc create configmap example-config \
 --from-literal=PARAMETRO_PROVA=valore_a_caso". In questo modo verrà creata una configMap passandogli un singolo parametro.  

kubectl exec pod-per-config -- env
