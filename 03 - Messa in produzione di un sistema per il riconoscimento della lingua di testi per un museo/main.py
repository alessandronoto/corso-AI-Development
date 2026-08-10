#Import delle librerie necessarie
import pickle
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Configurazione del file di log
logging.basicConfig(
    filename = "log_info.log",   #definiamo il nome del file in cui salvare i log
    level = logging.INFO,   #definiamo il livello minimo dei messaggi da registrare
    format = "%(asctime)s - %(levelname)s - %(message)s")  #definiamo il formato del messaggio

#Isoliamo i log relativi all'API
logger = logging.getLogger(__name__)

#Caricamento del Modello di Machine Learning
filename = "language_detection_pipeline.pkl"

try:
    with open(filename, "rb") as f:
        loaded_pipeline = pickle.load(f)
except FileNotFoundError:
    logger.warning(f"ERRORE: File {filename} non trovato")
    raise SystemExit("Impossibile avviare il server: file mancante")
except Exception as e:
    logger.warning(f"Errore durante il caricamento del file: {e}")
    raise SystemExit("Impossibile avviare il server: errore nel caricamento del file")

#Creazione istanza
app = FastAPI(
    title = "MuseumLangAPI",
    description = "API per l'identificazione della lingua di un testo"
)

#Creazione schemi Pydantic
class TextRequest(BaseModel):
    text: str
    
class LanguageResponse(BaseModel):
    language_code: str
    confidence: float

#Creazione endpoint
@app.post("/identify-language", response_model = LanguageResponse)
def identify_language(request: TextRequest):
    """
    Aalizza il testo inviato all'endpoint e restituisce il codice della lingua
    identificate ed il relativo livello di confidenza
    """
    #verifico che l'input non sia vuoto
    clean_text = request.text.strip()
    if not clean_text:
        logger.warning("Testo vuoto")
        raise HTTPException(status_code = 400, detail = "Il testo inviato non può essere vuoto")

    #Registro la richiesta
    log_text = clean_text[:30] +"..." if len(clean_text) > 30 else clean_text
    logger.info(f"Testo inviato: {log_text}")

    #Calcolo delle probabilità delle varie lingue identificabili dal modello
    probabilities = loaded_pipeline.predict_proba([clean_text])[0]

    #Calcolo della probabilità massima della lingua identificata
    max_proba = float(max(probabilities))

    #Verifico che la confidenza sia sopra una soglia minima che rende l'identificazione affidabile
    valore_soglia = 0.35
    if max_proba < valore_soglia:
        logger.warning(f"Lingua non identificabile (confidenza troppo bassa: {max_proba:.2f})")
        raise HTTPException(
            status_code = 400,
            detail = "Impossibile identificare la lingua")

    #Previsione lingua con il modello di ML caricato in precedenza
    prediction = loaded_pipeline.predict([clean_text])[0]

    #Registro risultato
    logger.info(f"Lingua identificata: {prediction}")

    #Restituiamo come output della funzione un oggetto di tipo LanguageResponse
    return LanguageResponse(language_code=str(prediction), confidence = max_proba)
