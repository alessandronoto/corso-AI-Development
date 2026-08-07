#Import delle librerie necessarie
import pickle
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Configurazione del file di log
logging.basicConfig(
    filename="log_info.log",   #definiamo il nome del file in cui salvare i log
    level=logging.INFO,   #definiamo il livello minimo dei messaggi da registrare
    format="%(asctime)s - %(levelname)s - %(message)s")  #definiamo il formato della messaggio


#Caricamento del Modello di Machine Learning
filename="language_detection_pipeline.pkl"
loaded_pipeline=pickle.load(open(filename, "rb"))

#Creazione istanza
app=FastAPI(
    title="MuseumLangAPI",
    description="API per l'identificazione della lingua di un testo"
)

#Creazione schemi Pydantic
class TextRequest(BaseModel):
    text: str
    
class LanguageResponse(BaseModel):
    language_code: str

#Creazione endpoint
@app.post("/identify-language", response_model=LanguageResponse)
def identify_language(request: TextRequest):
    #verifico che l'input non sia vuoto
    clean_text=request.text.strip()
    if not clean_text:
        logging.warning("Testo vuoto")
        raise HTTPException(status_code=400, detail="Il testo inviato non può essere vuoto")

    #Registro della richiesta
    logging.info(f"Testo inviato: {clean_text[:30]}...")

    #Previsione lingua con il modello di ML caricato in precedenza
    prediction=loaded_pipeline.predict([clean_text])[0]

    #Registro risultato
    logging.info(f"Lingua identificata: {prediction}")

    #Restituiamo come output della funzione un oggetto di tipo LanguageResponse
    return LanguageResponse(language_code=str(prediction))
