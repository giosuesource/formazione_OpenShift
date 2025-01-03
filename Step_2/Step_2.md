
# Step. 2
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di creare una ROOT CA self-signed e locale, creare un CSR e rilasciare i certificati richiesti dal CSR tramite ROOT CA creata.
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)
- Openssl (https://docs.openssl.org/master/)
### Svolgimento:

Per la creazione della ROOT CA si deve creare una key con il comando "openssl genrsa -out rootCA.key 2048".
Si può poi creare il certificato utilizzando il comando 'openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 3650 -out rootCA.crt -subj "/C=IT/ST=Italy/L=Rome/O=Sourcesense/OU=DevOps Department/CN=RootCA"'. Questo comando va ad utilizzare la key creata in precedenza e permette di specificare i vari parametri che faranno parte del certificato, tra cui country, organization e certificate name.

Per creare il CSR si deve generare una nuova key con il comando "openssl genrsa -out chiave.key 2048" e si può poi passare alla creazione con il comando "openssl req -new -key chiave.key -out chiave.csr -subj "/C=IT/ST=Italy/L=Rome/O=Sourcesense/OU=DevOps Department/CN=example.com", anche in questo caso specificando i vari parametri.

Per effettuare il rilascio dei certificati tramite la ROOT CA si deve utilizzare il comando "openssl x509 -req -in chiave.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial \
-out chiave.crt -days 825 -sha256 -extfile openssl.cnf -extensions v3_ca"
