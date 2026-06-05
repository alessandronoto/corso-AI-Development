import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

def data_cleaner(sentence):
    """Esegue la pulizia del testo rimuovendo punteggiatura e numeri."""
    sentence = sentence.lower()
    # Mantiene solo caratteri alfabetici (inclusi accentati) e spazi
    sentence = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", sentence)
    return sentence

def lang_prediction(query, vectorizer, model):
    """Ottiene la lingua associata a una query di input usando il modello addestrato."""
    query = data_cleaner(query)
    vectorized_query = vectorizer.transform([query])
    predict_query_lang = model.predict(vectorized_query)
    return predict_query_lang[0]

def train_pipeline():
    print("Inizializzazione pipeline: Download del dataset e addestramento modello...")
    
    # Importo il dataset dal repository remoto
    BASE_URL = "https://raw.githubusercontent.com/Profession-AI/progetti-ml/refs/heads/main/Modello%20per%20l'identificazione%20della%20lingua%20dei%20testi%20di%20un%20museo/"
    dataset = pd.read_csv(BASE_URL + "museo_descrizioni.csv")

    # Preparazione target e features
    target = dataset["Codice Lingua"]
    clean_dataset = dataset["Testo"].apply(data_cleaner)

    # Suddivisione Train e Test set (70% train, 30% test)
    X_train, X_test, y_train, y_test = train_test_split(
        clean_dataset, target, test_size=0.3, random_state=42
    )

    # Vettorizzazione con Bag-of-Words (n-grammi a livello di carattere)
    cv = CountVectorizer(ngram_range=(2, 4), analyzer='char')
    vectorized_X_train = cv.fit_transform(X_train)
    vectorized_X_test = cv.transform(X_test)

    # Inizializzazione e addestramento del modello Multinomial Naive Bayes
    clf = MultinomialNB()
    clf.fit(vectorized_X_train, y_train)

    print("Modello addestrato con successo.\n")
    return cv, clf


def main():
    # Avvia l'addestramento e recupera gli oggetti vettorizzatore e modello
    cv, clf = train_pipeline()
    
    print("--- 🏛️ MuseumLangID: Sistema di Identificazione Lingue ---")
    print("Pronto per l'uso nell'infrastruttura del museo.\n")
    
    while True:
        query = input("Inserisci il Testo da identificare (digita 'esci' per terminare): ")

        if query.lower() == 'esci':
            print("Chiusura programma MuseumLangID.")
            break

        # Verifico che l'input abbia almeno una lettera
        if not re.search(r'[a-zA-ZÀ-ÿ]', query):
            print("Inserire almeno una lettera!")
            print("-" * 40)
            continue

        # Eseguiamo la previsione passando i parametri necessari
        risultato = lang_prediction(query, cv, clf)
        print(f"Codice Lingua Rilevato: {risultato}")
        print("-" * 40)

if __name__ == "__main__":
    main()
