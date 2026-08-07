# Caso d'Uso Aziendale: MuseumLangAPI
> **Messa in Produzione di un Sistema per il Riconoscimento della Lingua di Testi per un Museo**

---

## Introduzione all'Azienda & Contesto

**MuseumLangID**, il sistema sviluppato per il riconoscimento automatico della lingua di testi museali, è pronto per essere messo in produzione. L'obiettivo principale è fornire le funzionalità del modello tramite un'**API REST** per integrarlo facilmente nei sistemi gestionali e software del museo.

---

## Problema

Il museo richiede un **accesso remoto e standardizzato** alle funzionalità del modello di riconoscimento della lingua. Attualmente, il sistema è limitato all'utilizzo locale, ostacolando la collaborazione tra i vari reparti dell'organizzazione e impedendo l'integrazione con altri strumenti software già in uso.

---

## Obiettivo del Progetto

Implementare un'API RESTful per esporre le funzionalità del modello di Machine Learning. L'API deve essere in grado di:

1. **Ricevere** testi in ingresso nel formato `JSON`.
2. **Restituire** il codice ISO della lingua riconosciuta e il relativo indice di confidenza.
3. **Garantire** scalabilità, robustezza e predisposizione per l'integrazione con sistemi e client esterni.

---

## Benefici Attesi

- **Accessibilità**: Consentire a tutti i reparti del museo e alle applicazioni client di accedere al servizio da remoto.
- **Integrazione**: Facilitare l'interoperabilità del sistema con le infrastrutture ed i gestionali software esistenti.
- **Scalabilità**: Permettere un utilizzo simultaneo e in parallelo da parte di più utenti o sistemi automatizzati.

---

## Specifiche Tecniche e Funzionali

### Architettura Tecnologica
- **Language & Framework**: Python 3.9+ con **FastAPI**
- **Machine Learning Core**: Pipeline Scikit-learn caricata da file Pickle (`languagedetectionpipeline.pkl`)

---

### Specifiche dell'API REST

#### **Endpoint:** `POST /identify-language`

* **Input**: JSON contenente il testo della targhetta/opera da analizzare.
* **Output**: JSON contenente il codice della lingua identificata e la probabilità associata.

#### Esempio di Payload di Input:
```json
{
  "text": "Questo è un esempio di testo."
}
