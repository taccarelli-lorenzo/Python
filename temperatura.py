temperature = []
giorni = 7
giorniPari = 0
scelta = 0

temperatureDaInserire = (int(input(f"Quante temperature si vogliono inserire? : ")))

for i in range(temperatureDaInserire):
        temperature.append(float(input(f"Inserisci la {len(temperature) + 1} temperatura giorno: ")))
        if temperature[i] % 2 == 0 :
            giorniPari += 1

while temperatureDaInserire != 0:   
        
    print("""Cosa si vuole fare? 
          1. Inserisci altre temperature
          2. Visualizzare le temperature inserite fino ad ora
          3. Visualizzare la temperatura minore
          4. Visualizzare la temperatura maggiore
          5. Visualizzare la temperatura media
          6. Visualizzare i giorni con temperatura pari
          0. Terminare il programma""")
    
    scelta = int(input("Scegli un'opzione: "))
    
    
    match scelta:
        case 0:
            temperatureDaInserire = 0
        case 1: 
            temperatureDaInserire = (int(input(f"Quante altre temperature si vogliono inserire? [0 per terminare] : ")))
            for i in range(temperatureDaInserire):
                temperature.append(float(input(f"Inserisci la {len(temperature) + 1} temperatura giorno: ")))
                if temperature[i] % 2 == 0 :
                    giorniPari += 1
        case 2:
            print(f"Le temperature inserite sono: {temperature} ")
        case 3: 
            print(f"La temperatura minore è: {min(temperature)}")
        case 4: 
            print(f"La temperatura maggiore è: {max(temperature)}")
        case 5: 
            print(f"La temperatura media è: {sum(temperature)/len(temperature)} ")
        case 6: 
            print(f"Ci sono stati: {giorniPari} giorni con una temperatura pari ")
        case _:
            print("Input non valido!")    
    
print("Arrivederci!")