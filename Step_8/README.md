
## Step. 8
### Descrizione esercizio:

Crea sul tuo cluster Kubernetes tre tipi di applicazioni:
 
Applicazione frontend: Espone un servizio web all'esterno del cluster.
Applicazione backend: Fornisce servizi all'applicazione frontend.
Database: Contiene i dati delle applicazioni.

Assegna le seguenti labels ai deployment delle applicazioni:
app=frontend
app=backend
app=database
 
Configura le Network Policy per garantire la seguente sicurezza:
L'applicazione frontend può comunicare solo con l'applicazione backend.
L'applicazione backend può comunicare solo con il database.
Il database non può comunicare con l'esterno.

Network Policy per l'applicazione frontend:
Consenti il traffico in uscita verso l'applicazione backend.
Nega tutto il traffico in entrata, tranne quello proveniente da servizi esterni.
 
Network Policy per l'applicazione backend:
Consenti il traffico in uscita verso il database.
Consenti il traffico in entrata dall'applicazione frontend.
Nega tutto il traffico restante.
 
Network Policy per il database:
Nega tutto il traffico in entrata e in uscita.
 
 
Verifica:
Utilizza il comando kubectl get networkpolicies per verificare che le Network Policy siano state create correttamente.
Utilizza strumenti come kubectl exec per eseguire dei ping tra i pod e verificare che la comunicazione sia conforme alle policy configurate.

### Tools utilizzati:

- Openshift (https://docs.openshift.com/)

### Svolgimento:
Per lo svolgimento di questo esercizio per prima cosa si dovrà controllare lo stato di Minikube con il comando "minikube status", e qualora non fosse nello stato "running" si potrà avviare con il comando "Minikube start". 
Poi si potranno andare a scrivere i file YAML richiesti nella traccia, quindi i file contenenti deployment, service e Network policy per back-end, front-end e database. In ognuno di loro andranno specificate le labels richieste e una volta salvate le modifiche, si potranno creare i vari oggetti con il comando " oc apply -f nome_file". In questo modo, prendendo come riferimento il deployment backend, dopo aver utilizzato il comando "oc apply -f backend_deploy.yaml" si potrà verificarne lo stato con i comandi "oc get deploy backend-deploy" e "oc describe deploy backend-deploy". 

Per la riuscita dell' esercizio si dovrà andare a verificare la creazione e il funzionamento delle network policy: si potrà utilizzare il comando "oc get networkpolicies" per verificarne la riuscita creazione.

Successivamente si potrà andare a verificare l' effettivo funzionamento sfruttando il comando exec, nello specifico il comando "kubectl exec -it nome_pod -- /bin/bash".
Con questo comando si potrà effettuare la connessione al terminale del Pod e si potrà verificare il funzionamento delle networkpolicies con il comando ping.
