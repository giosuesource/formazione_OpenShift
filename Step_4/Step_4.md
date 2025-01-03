
# Step. 4
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di installare Prometheus Stack tramite helm chart ufficiale e provare il BlackBox Exporter per il monitoring di endpoint http
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)
- Quotas (https://docs.openshift.com/container-platform/4.8/applications/quotas/quotas-setting-per-project.html)
### Svolgimento:
Per iniziare bisogna installare Prometheus tramite Helm Chart. Per farlo si può utilizzare il comando “helm repo add prometheus-community https://prometheus-community.github.io/helm-charts && helm repo update” per aggiungere la repository e il comando “helm install prod prometheus-community/kube-prometheus-stack” per installare. 

Successivamente si possono andare a creare i file che compongono il blackbox exporter, ovvero “blackbox_config.yml” e “prometheus.yml”, che ci serviranno per il monitoring di endpoint http.

