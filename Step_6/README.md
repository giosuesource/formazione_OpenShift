
# Step. 6
### Descrizione esercizio:

Lo scopo di questo esercizio è quello di scrivere due applicazioni in Python che effettuino le seguenti operazioni:

App1 => creare topic "foobar" che agisca da producer di messaggi

App2 => consumer messaggi

Biaogna poi utilizzare qualche strumento di monitoring per calcolare il lag tra i messaggi prodotti e quelli consumati.
### Tools utilizzati:

- Openshift (https://docs.openshift.com/)
- Apache Kafka (https://kafka.apache.org/documentation/)
- Docker Compose (https://docs.docker.com/compose/)

### Svolgimento:
Per lo svolgimento di questo esercizio sono stati creati 2 container, con rispettivamente image "zookeeper" e "confluentinc/cp-kafka". Per velocizzare questa operazione è stato utilizzato Docker Compose: è stato infatti scaricato e avviato su macchina host e di conseguenza è stato creato un file yaml contenente la configurazione dei container. Dopo aver salvato quest' ultimo file è stato utilizzato il comando "docker compose up -d" per avviare la creazione.
Dopo aver fatto ciò è stato verificato lo stato dei container con il comando "docker ps -a", visualizzando lo stato "up" su entrambi.
Adesso si può utilizzare il comando "docker exec -it step_6-kafka-1 kafka-topics --create --topic foobar --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1" per andare a creare il topic che ci servirà più tardi. 

Successivamente sono stati creati i file consumer.py e producer.py per la configurazione del consumer e del producer dei messaggi. Dopo la creazione si può utilizzare il comando "python producer.py" e "python consumer.py" per avviare entrambe le applicazioni. 

Infine per il monitoraggio del lag è stato utilizzato il comando di Kafka "docker exec -it kafka kafka-consumer-groups --bootstrap-server localhost:9092 --group my-group --describe".