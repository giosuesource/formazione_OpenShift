
## Step. 7
### Descrizione esercizio:

Crea un nuovo deployment per un'applicazione web in ambiente di sviluppo, posizionata nella regione europea.
Assegna le seguenti labels al deployment:

environment=dev

app=web

region=EU

Crea un servizio di tipo LoadBalancer per esporre l'applicazione web all'esterno del cluster.
Seleziona tutti i pod con le labels app=web e environment=dev.
 
Crea un ReplicaSet per gestire le repliche del deployment dell'applicazione web.
Associa al ReplicaSet le stesse labels del deployment.

Crea un Ingress per esporre l'applicazione web tramite un nome di dominio personalizzato.
Configura l'Ingress per instradare il traffico verso il servizio creato in precedenza.
Utilizza un selector basato sulle labels per selezionare il servizio corretto.

Crea un DaemonSet per eseguire un'applicazione di logging su tutti i nodi del cluster.
Assegna al DaemonSet la label app=logging.
 
Per verificare che tutti gli oggetti siano stati creati correttamente utilizza il comando:

kubectl get deployments,services,replicasets,ingress,daemonsets -o wide

Per visualizzare i pod associati all'applicazione web in ambiente di sviluppo utilizza il comando:

kubectl get pods -l app=web,environment=dev 

Infine, accedi all'applicazione web tramite il nome di dominio configurato nell'Ingress.

### Tools utilizzati:

- Openshift (https://docs.openshift.com/)

### Svolgimento:
Per lo svolgimento di questo esercizio per prima cosa si dovrà controllare lo stato di Minikube con il comando "minikube status", e qualora non fosse nello stato "running" si potrà avviare con il comando "Minikube start". 
Poi si potranno andare a scrivere i file YAML richiesti nella traccia, quindi i file deploy.yaml, service.yaml, replicaset.yaml, ingress.yaml e deamonset.yaml. In ognuno di loro andranno specificate le labels richieste e una volta salvate le modifiche, si potranno creare i vari oggetti con il comando " oc apply -f nome_file". In questo modo, prendendo come riferimento il deployment, dopo aver utilizzato il comando "oc apply -f deploy.yaml" si potrà verificarne lo stato con i comandi "oc get deploy deploy-step7" e "oc describe deploy deploy-step7". 

Per la riuscita dell' esercizio ci si dovrà assicurare che sia installato un ingress controller, che servirà per l' utilizzo dell' ingress. 

In questo caso si può scaricare NGINX controller, utilizzando il comando "helm install my-release oci://ghcr.io/nginxinc/charts/nginx-ingress --version 2.0.0"
