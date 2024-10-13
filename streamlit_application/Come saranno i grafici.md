# E-Commerce Customer Data Procedura Guida (Olist)

![x](https://img.notionusercontent.com/s3/prod-files-secure%2F591dff13-5117-425d-a983-ca995144a283%2Fa3119321-46eb-47aa-9e5d-648920e181b6%2FFrame_2.png/size/w=2000?exp=1727884335&sig=SAmwn0L1lk8QH_MnrV-3FqoP62FeMol-PUJtnl69ZSI)

---



## Analisi delle colonne e dimensioni:

Per creare un cubo di dati con le dimensioni elencate, possiamo organizzare queste informazioni in categorie, facilitando l'analisi da varie prospettive. Divideremo le dimensioni del cubo di dati nelle seguenti categorie:

### 1. **Dimensione Ordine** (`order`)
- `order_id`: Identificazione univoca dell'ordine.
- `order_item_id`: ID univoco dell'articolo nell'ordine.
- `order_unique_id`: ID univoco combinato per rappresentare l'ordine e l'articolo.
- `order_status`: Stato dell'ordine (es: consegnato, cancellato).
- `order_purchase_timestamp`: Data e ora dell'acquisto.
- `order_approved_at`: Data e ora dell'approvazione dell'ordine.
- `order_delivered_carrier_date`: Data di consegna al corriere.
- `order_delivered_customer_date`: Data di consegna al cliente.
- `order_estimated_delivery_date`: Data stimata di consegna.
- `shipping_limit_date`: Data limite per la spedizione.
- `shipping_duration`: Durata della spedizione (tempo effettivo di consegna).

### 2. **Dimensione Cliente** (`customer`)
- `customer_id`: ID del cliente.
- `customer_unique_id`: Identificazione univoca del cliente.
- `customer_zip_code_prefix`: Prefisso del CAP del cliente.
- `customer_city`: Città del cliente.
- `customer_state`: Stato del cliente.
- `customer_zone`: Zona geografica (es: Sud, Nord).

### 3. **Dimensione Prodotto** (`product`)
- `product_id`: Identificazione del prodotto.
- `product_category_name`: Nome della categoria del prodotto.
- `product_name_lenght`: Lunghezza del nome del prodotto.
- `product_description_lenght`: Lunghezza della descrizione del prodotto.
- `product_photos_qty`: Quantità di foto del prodotto.
- `product_weight_g`: Peso del prodotto (in grammi).
- `product_length_cm`: Lunghezza del prodotto (in cm).
- `product_height_cm`: Altezza del prodotto (in cm).
- `product_width_cm`: Larghezza del prodotto (in cm).
- `Kg`: Peso in chilogrammi (conversione da `product_weight_g`).

### 4. **Dimensione Venditore** (`seller`)
- `seller_id`: Identificazione del venditore.
- `seller_zip_code_prefix`: Prefisso del CAP del venditore.
- `seller_city`: Città del venditore.
- `seller_state`: Stato del venditore.
- `seller_zone`: Zona geografica del venditore.

### 5. **Dimensione Pagamento** (`payment`)
- `payment_sequential`: Sequenza del pagamento.
- `payment_type`: Tipo di pagamento (es: carta di credito, bonifico).
- `payment_installments`: Numero di rate.
- `installments_price`: Prezzo per rata.
- `price`: Prezzo totale del prodotto.
- `freight_value`: Valore della spedizione.
- `payment_value`: Valore totale pagato.

### 6. **Dimensione Recensione** (`review`)
- `review_id`: Identificazione della recensione.
- `review_score`: Voto della recensione.
- `review_comment_title`: Titolo del commento.
- `review_comment_message`: Contenuto del commento.
- `review_creation_date`: Data di creazione della recensione.
- `review_answer_timestamp`: Data di risposta alla recensione.

### 7. **Dimensione Temporale** (`time`)
- `day_of_purchase`: Giorno dell'acquisto.
- `month_of_purchase`: Mese dell'acquisto.
- `year_of_purchase`: Anno dell'acquisto.
- `month/year_of_purchase`: Mese e anno dell'acquisto (combinazione).



## 1. Pagina principale - Controllo

### 1.1 Metriche delle intestazioni

- Totale di prodotti venduti e media giornaliera
- Profitto totale e media giornaliera
- Persone riguardate/in circa più di X città
- Quantità di fornitori e media

### 1. Clienti e venditori

- Quantità (solo i nuovi)

### 1. Giorni della settimana

- Totale di vendite
- Profitti

---

## 2. Analisi dei prodotti:

L’idea è quella di capire meglio le prestazioni e le caratteristiche dei prodotti che si possono trovare sulla piattaforma, e soprattutto, com’è cambiato negli anni.

### 2.1 Prime informazioni (Intestazioni)

- Quantità di prodotti

### 2.2 Raccolta con tutte le categorie

La lista può essere ordinata in base a una certa caratteristica del prodotto e certe caratteristiche potranno esse ammesse, affinché si possa mettere in evidenza ciò che vuole vedere.

- Le vendite del prodotto
- Volte in cui è stato acquistato seguito da un altro prodotto
- Medie:
    - Prezzo
    - Durate fino all’arrivo
    - Degli altri acquisti
    - Recinzione
    - Prezzo dell’espedizione
    - Prezzo finale
    - Quantità di rate e il loro prezzo
    - Durata fino all’approvazione del pagamento
- Accatto a questi numeri, ci sarà un pulsante che ci porta a vedere nel dettaglio come si sono comportate queste metriche nell’ultimo periodo

### 2.3 Metriche delle categorie nell’ultimo periodo

Fare in modo che attraverso un grafico di linea, l’utente possa vedere come si è comportata una metrica di un gruppo di categorie o viceversa.

### 2.4 Rapporto tra categorie e profitto

Sarebbe le categorie che vendono di più a portare più profitti?

---

## 3. Le ordini

Lo possiamo associare anche ai valori dei pagamenti 

- Durata media
- Media dei valori di pagamento (prezzo, spedizione e prezzo finale)
- Media di prodotti per ordine
- Durata fino all’approvazione del pagamento
- Durata fino all’arrivo
- Percentuale di prodotti che arrivano prima o nel giorno previsto e la percentuale di quelli che arrivano dopo il previsto
- Percentuale di ogni tipo di pagamento
- Media del prezzo di ogni singolo prodotto fatto in un ordine con più di un solo prodotto

### 3.1 Gli stratti del prezzo finale

Suddividere il prezzo dei prodotti in stratti e analizzare questi numeri in base a uno spazio di tempo

Grafico di linee a sinistra e grafico di pizza a destra

---

## 4. Analisi dei dati geografici

<aside>

💡Possiamo anche cercare di rispondere alla domanda:

### ***Sarebbe il momento di Olist avere più centri di smistamento?***

</aside>

### 4.1 Le regioni e stati

Un grafico in cui si imposta una metrica per vederla in base alle regioni o agli stati, meglio ancora se si riesce ad aggiungere un’animazione al grafico per vedere come sono stati i cambiamenti durante uno spazio di tempo. 

(Paragonare dimensioni di spazio e tempo associate a determinate misure)

**Creare anche dei gruppi sopra**

- Media del prezzo, spedizione e prezzo finale
- Media di prodotti per ordine
- Grafico delle regioni con due barre una per mostrare il prezzo dei prodotti e l’altra per il prezo dell’espedizione
- Percentuale di prodotti che arrivano prima o nel giorno previsto e la percentuale di quelli che arrivano dopo il previsto

### 4.2 Prezzo dell’espedizione

- Qual è la percentuale di prodotti che vendono acquistati da qualcuno che non si trova nella stessa zona del venditore
- Quali sono le caratteristiche che hanno un impatto maggiore su questo prezzo?
- Com’è questo rapporto?

### 4.3 Rapporto clienti/venditori e zone

- Percentuale di clienti che si trovano nelle zone in cui ci sono venditori

---

## 5. Problemi ripostati dai clienti

### 5.1 Prodotti che non arrivano

### 5.2 Prodotti che arrivano danneggiati

---

# Al di là delle analisi e delle metriche

---

Ala fine di questo progetto ci saranno due analisi incredibili una su un archivio e l’latra potrà essere usata online da chiunque.

## 1. Jupyter Notebook

![Group 55525.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/591dff13-5117-425d-a983-ca995144a283/ba0c7ad4-c48c-42f8-ac40-11c5a7756a0b/Group_55525.png)

## 2. Dashboard

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/591dff13-5117-425d-a983-ca995144a283/b944d79c-674e-4ec3-a0f0-a62c7be27fa1/image.png)

## 1. Machine Learning Models: (Si-T8K)

---

### 1.1 Recinzioni basse e alte

Addestrare un modello per prevedere prodotti che prendono con una recinzione basse per capire quali caratteristiche hanno in comune

### 1.2 Raggruppare i clienti

Usa un modello in grado di raggruppare i dati, come per esempio K-Means