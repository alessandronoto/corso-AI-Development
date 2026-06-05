Un algoritmo di correzione per motori di ricerca *di Alessandro Noto*

Questo progetto costituisce il lavoro pratico di fine modulo focalizzato sulla **Programmazione con Python**

---

**Caso d'Uso Aziendale: Searchify**

***Introduzione all'Azienda***
Searchify è una startup innovativa che offre un motore di ricerca personalizzato per aziende di medie dimensioni, consentendo di cercare informazioni specifiche nei loro database interni. Uno dei principali vantaggi di Searchify è la semplicità d'uso: gli utenti possono trovare rapidamente documenti, report e altre risorse aziendali digitando parole chiave. Tuttavia, l'azienda si trova ad affrontare un problema che mina l'esperienza dell'utente.

***Problema***
Il problema principale di Searchify è che molti utenti commettono errori di digitazione durante l'inserimento delle parole chiave. Questi errori causano risultati di ricerca nulli o non pertinenti, portando a insoddisfazione tra gli utenti. Ad esempio, se un utente cerca "raporto vendite 2023" invece di "rapporto vendite 2023", il motore di ricerca non restituisce alcun risultato.

***Obiettivo del Progetto***
L'obiettivo è sviluppare un algoritmo di correzione automatica per il motore di ricerca di Searchify. Questo algoritmo dovrà:
1. Rilevare automaticamente gli errori di digitazione o le parole non valide.
2. Suggerire la parola corretta più probabile.
3. Restituire risultati pertinenti basati sulla correzione suggerita.

L'implementazione di questa funzionalità migliorerà notevolmente l'esperienza utente, aumentando l'efficienza del motore di ricerca e la soddisfazione dei clienti.

***Benefici Attesi***
- ***Miglioramento dell'accuratezza:*** Riduzione degli errori di ricerca dovuti a digitazioni errate.
- ***Incremento della produttività:*** Gli utenti troveranno le informazioni più velocemente.
- ***Aumento della fedeltà dei clienti:*** Un'esperienza utente più fluida e soddisfacente porterà a una maggiore adozione del prodotto.

***Specifiche del Progetto***
1. ***Input:*** Una stringa rappresentante una query di ricerca, digitata dall'utente.
2. ***Output:***
    - Se la query contiene errori, il sistema suggerisce una correzione.
    - Se la query è corretta, restituisce la stessa query.
3. ***Funzionalità Chiave:***
    - Confronto tra la parola inserita e un dizionario di parole corrette (da predefinire nel codice).
    - Implementazione di un algoritmo che calcoli la "distanza di edit" (es. distanza di Levenshtein) per trovare le parole più simili.
    - Gestione di casi d'uso realistici come errori di battitura comuni, lettere scambiate, omissioni o aggiunte.

***Consegna***
Scrivi un programma Python che implementi l'algoritmo di correzione automatica per il motore di ricerca. Il tuo codice deve:
1. Contenere una funzione principale chiamata ***suggest_correction(query, dictionary).***
    - **Parametri:**
        - *query:* La stringa di input inserita dall'utente.
        - *dictionary:* Una lista di parole corrette.
    - **Ritorno:**
        - La parola corretta più probabile o la query originale se è già valida.
2. Testare il funzionamento con almeno 10 casi d'uso (inclusi errori comuni e query corrette).
3. Essere ben documentato, con commenti che spieghino le principali scelte implementative.
4. Fornire un dizionario base contenente almeno 50 parole.

**Nota**
Il progetto deve essere completato senza l'uso di librerie esterne per il calcolo della distanza di edit o per altre funzionalità. L'obiettivo è che lo studente implementi l'algoritmo interamente da zero.
