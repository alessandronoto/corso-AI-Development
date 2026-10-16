**Analisi dei dati di vendita di un e-commerce con SQL**

questo progetto costituisce il lavoro pratico di fine modulo focalizzato sui **Database relazionali con SQL**

---

**I dati**
Lavorerai su tre tabelle del nostro database:

- ***prodotto***: ID, nome e prezzo dei prodotti;
- ***cliente***: ID ed email dei clienti;
- ***ordini***: le transazioni, che associano i prodotti ai clienti e alla data dell'ordine.
Per ricreare le tabelle in locale, trovi lo script nel repository GitHub dei progetti SQL.

**Output dell'analisi**
1. ***Preparazione dei dati***: importa le tabelle e scrivi le query che le uniscono. Il risultato deve essere un dataset integrato con le informazioni sui clienti, il nome e il prezzo dei prodotti e la data degli ordini.
2. ***Analisi dei clienti***: calcola la spesa totale di ogni cliente, sommando i prezzi dei prodotti acquistati. Poi ordina i clienti per spesa e individua chi ha speso di più. Ci servirà per il programma fedeltà.
3. ***Analisi dei prodotti***: calcola il fatturato totale generato da ciascun prodotto e ordina i prodotti per individuare i best-seller.
4. ***Analisi temporale***: aggrega le vendite per giorno della settimana, calcola il fatturato medio giornaliero e individua i giorni con la media più alta. Ci aiuterà a decidere quando programmare newsletter e promozioni.
5. ***Analisi degli ordini***: calcola quanti prodotti contiene ciascun ordine. Poi ricava la media e la distribuzione del numero di prodotti per ordine.
