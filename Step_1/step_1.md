
# Step. 1
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di creare un deployment che installi Nginx o un'applicazione con footprint minimale
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)

### Svolgimento:

Per iniziare bisogna andare a scaricare Openshift. Da sistema MacOS si può utilizzare il gestore di pacchetti brew, pertanto si può utilizzare il comando "brew install openshift". Si può verificare l' installazione utilizzando il comando "oc version". 
Per iniziare si deve far partire Minikube (già presente sulla macchina locale) con il comando "Minikube start". Dopodicché si deve creare un file YAML (step_1.yaml) che conterrà il Deployment. 
Dopo aver completato la configurazione del Deployment nel file Yaml, si può far partire con il comando "oc apply -f step_1.yaml". Per verificare che sia tutto corretto possiamo utilizzare il comando "oc get deploy" per visualizzare il Deployment appena creato.