/*

Analisi dei Dati di Vendita di un E-commerce
Alessandro Noto

*/


-- 1. Preparazione dei dati
-- Creazione tabella aggragata
CREATE VIEW tabella_aggregata AS                                                    -- creo una vista della tabella aggregata per poi interrogarla nelle successive query
SELECT
c.id,                                                                               -- colonna id del cliente
c.email,                                                                            -- colonna email del cliente
substring_index(c.email, ".", 1) as nome_cliente,                                   -- in questa colonna estraggo il nome del cliente dalla sua mail
substring_index(substring_index(c.email, "@", 1), ".", -1) as cognome_cliente,      -- in questa colonna estraggo il cognome del cliente dalla sua mail
o.data,                                                                             -- colonna data dell'ordine
o.id_prodotto,                                                                      -- colonna con l'id del prodotto
p.nome,                                                                             -- colonna con il nome del prodotto
p.prezzo                                                                            -- colonna con il prezzo del prodotto
from ecommerce_db.cliente as c
join ecommerce_db.ordini as o
on c.id=o.id_cliente
join ecommerce_db.prodotto as p
on p.id=o.id_prodotto;

-- 2. Analisi dei clienti
-- Tabella con spesa totale di ciascun cliente in ordine decrescente
SELECT
id,
nome_cliente,
cognome_cliente,
SUM(prezzo) as spesa_cliente
from tabella_aggregata
GROUP BY id
ORDER BY spesa_cliente DESC;

-- 3. Analisi dei prodotti
-- Tabella con fatturato totale per ciascun prodotto in ordine decrescente
SELECT
id_prodotto,
nome,
SUM(prezzo) as fatturato_prodotto
from tabella_aggregata
GROUP BY id_prodotto
ORDER BY fatturato_prodotto DESC;

-- 4. Analisi temporale
-- Tabella con fatturato medio giornaliero in ordine decrescente
SELECT
DAYNAME(data) as day_name,
AVG(prezzo) as fatturato_giornaliero_medio
from tabella_aggregata
GROUP BY day_name
ORDER BY fatturato_giornaliero DESC;

-- 5. Analisi degli ordini
-- Numero di prodotti per ciascun ordine
SELECT
id,
data,
COUNT(id) AS num_prodotti
FROM tabella_aggregata
GROUP BY id, data;

-- Media e distribuzione del numero di prodotti per ordine
SELECT
AVG(num_prodotti) AS media_prodotti_per_ordine
FROM (
    SELECT id, data, COUNT(id) AS num_prodotti
    FROM tabella_aggregata
    GROUP BY id, data
) AS ordini_dettaglio;

SELECT
num_prodotti,
COUNT(*) as frequenza_ordine
from(
    SELECT id, data, COUNT(id) AS num_prodotti
    FROM tabella_aggregata
    GROUP BY id, data
    ) as dettaglio
GROUP by num_prodotti;
