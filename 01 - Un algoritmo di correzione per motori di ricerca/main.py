def zero_matrix(n_columns:int, n_row:int):
  """
  restituisce un matrice di zeri composta da liste annidate

  Parametri:
  n_columns (int): numero di colonne
  n_row (int): numero di righe

  Ritorna:
  matrix (list): lista annidata di zeri
  """
  matrix=[[0 for _ in range(n_columns)] for _ in range(n_row )]
  return matrix

def levenshtein_dist(word_1:str,word_2:str):
  """
  restituisce la distanza di Levenshtein tra word_1 e word_2

  Parametri:
  word_1 (str): parola uno
  word_2 (str): parola due

  Ritorna:
  dist (int): distanza
  """
  n=len(word_1)
  m=len(word_2)

  # inizializzo una matrice di zeri
  matrix=zero_matrix(m+1 , n+1)

  # compilo la matrice per determinare la distanza di Levenshtein
  for i in range(m + 1):
    matrix[0][i]=i         # compilo la prima riga con numeri progressivi che partono da zero fino alla lunghezza della parola nel database
  for j in range(n + 1):
    matrix[j][0]=j         # compilo la prima colonna con numeri progressivi che partona da zero fino alla lunghezze della parola inserita dall'utente

  # per compilare la restante parte della tabella confronto tra loro le varie lettere
  for i, letter_in_word1 in enumerate(word_1):
    for j, letter_in_word2 in enumerate(word_2):

      if letter_in_word1==letter_in_word2:
        matrix[i+1][j+1]=matrix[i][j]
      else:
        matrix[i+1][j+1]=min(matrix[i][j],matrix[i+1][j],matrix[i][j+1])+1

  #il numero nella cella in basso a destra rappresenta la distanza di Levenshtein tra word_1 e word_2
  dist=matrix[n][m]
  return dist

def suggest_correction(query:str, dictionary:list):
  """
  suggerisce la query corretta o l'originale se quella inserita è già corretta

  Parametri:
  query (str): stringa inserita dall'utente
  dictionary (list): database di parole corrette

  Ritorna:
  query_output (str): la query corretta o l'originale
  is_query_correct (bool): True se la query in input è corretta
                           False se presenta errori
  """

  query_split=list(map(str.lower, query.split()))

  low_dictionary=map(str.lower, dictionary)
  font_dictionary=dict(zip(low_dictionary,dictionary)) #dizionario che associa la parola in minuscolo alla parola con formattazione corretta

  len_query_split=len(query_split)

  # inizializzo delle variabili
  count_correct_word=0              # variabile che conteggia le parole corrette inserite dall'utente
  output_query_list=[]              # lista in cui verranno salvate le parole corrette

  # itero sulle parole inserite dall'utente verificando prima se siano contenute nel database
  for query_word in query_split:
    if query_word in font_dictionary:                                # se la parola è contenuta nel dizionario:
      count_correct_word += 1                                        # aumento il contatore
      output_query_list.append(font_dictionary[query_word.lower()])  # aggiungo la parola alla lista di output

    else:
      # se non è contenuta nel database calcolo la distanza di edit
      # determino la parola che ha la minore distanza analizzando il dizionario e applicando alle chiavi la funzione per il calcolo della distanza
      min_key = min(font_dictionary, key=lambda dict_key: levenshtein_dist(query_word, dict_key))

      #alla fine aggiungo la parola alla query di output
      output_query_list.append(font_dictionary[min_key])

  # genero la query di output unendo le parole prsenti nella lista
  output_query=" ".join(output_query_list)

  # ritorno una variabile booleana che indica se la query in input era corretta o meno
  if count_correct_word==len_query_split:
    return output_query, True
  else:
    return output_query, False

def run_test(dictionary:list):
    """
    Esegue una serie di test automatizzati
    """
    # Definiamo una lista di tuple: (input_utente, output_atteso, booleano che indica se l'input è corretto)
    test_cases = [
        ("KPI", "KPI", True),                  # Caso 1: Parola esatta
        ("kpi", "KPI", True),                  # Caso 2: Case insensitivity
        ("raporto", "Rapporto", False),        # Caso 3: Errore semplice
        ("budjet", "Budget", False),           # Caso 4: Lettera errata
        ("mmeting", "Meeting", False),         # Caso 5: Doppia lettera errata
        ("KPI raporto", "KPI Rapporto", False),# Caso 6: Frase mista
        ("ProFIt", "Profit", True),            # Caso 7: Maiuscolo e minuscolo
        ("stakholder", "Stakeholder", False),  # Caso 8: Omissione di una lettera
        ("bussiness", "Business", False),      # Caso 9: Lettera in più
        ("ROI budget", "ROI Budget", True)     # Caso 10: Due parole corrette
    ]

    print("--- INIZIO TEST ---")

    for i, (user_input, expected_output, expected_status) in enumerate(test_cases, 1):
        # Chiamo la funzione suggest_correction, passando come input: user input e dictionary
        result, status = suggest_correction(user_input, dictionary)

        # Uso assert per verificare che tutto funzioni correttamente
        try:
            assert result == expected_output, f"Errore Output: atteso '{expected_output}', ricevuto '{result}'"
            assert status == expected_status, f"Errore Stato: atteso {expected_status}, ricevuto {status}"
            print(f"Test {i}: SUPERATO ({user_input} -> {result})")
        except AssertionError as e:
            print(f"Test {i}: FALLITO! {e}")

    print("--- FINE TEST ---")


def main():
  print("---Algoritmo correzione per motori di ricerca---")

  # definisco un database di parole corrette
  database=[
      "KPI", "ROI", "Stakeholder", "Budget", "Deadline", "Feedback", "Meeting",
      "Brainstorming", "Outsourcing", "Core", "Business", "Target", "Workflow",
      "B2B", "B2C", "Deliverable", "Escalation", "Quarter", "Revenue", "Vendite",
      "Backlog", "Scrum", "Agile", "Onboarding", "Offboarding", "CEO",
      "CTO", "CFO", "HR", "R&D", "Asset", "Compliance", "Governance", "Rapporto",
      "Scalability", "Benchmark", "Best", "Practice", "Bottleneck", "CRM","ERP",
      "Headcount", "Incentive", "Leadership", "Logistics", "Market", "Share",
      "Mindset", "Networking", "Overhead", "Performance", "Pipeline", "Pitch",
      "Profit", "Project", "Management", "Quality", "Assurance", "Recruitment",
      "Retargeting", "Roadmap", "SEO", "SEM", "SLA", "Strategy", "Supply", "Chain",
      "Synergy", "Task", "Force", "Turnover", "Upskilling", "User", "Experience",
      "Value", "Proposition", "Vision", "Mission", "Breefing"
  ]
  
  # chiedo un input all'utente
  query_user=input("Inserire query di ricerca: ")
  
  #per lanciare i test, inserire in input start_test
  if query_user=="start_test":
    run_test(database)
  
  #altrimenti procediamo con il programma normalmente
  else:
    # richiamo la funzione
    output, is_query_correct = suggest_correction(query_user, database)
  
    if is_query_correct:
      print(f"Risultato di ricerca per: {output}")
    else:
      print(f"Forse intendevi: {output}")


if __name__ == "__main__":
    main()
  
