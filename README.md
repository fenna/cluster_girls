# README

## Workshop Clusteren - CBS Data

Welkom bij de repository voor de workshop over het clusteren van Nederlandse wijken en buurten met behulp van CBS data. Deze repository bevat alle benodigde scripts en notebooks voor het uitvoeren van een clusteranalyse, inclusief preprocessing van de data en verschillende clusteringmethodes.

### Bestanden

1. **preprocessing.py**  
   Dit script bevat de code voor het preprocessen van de CBS data. Het doel hiervan is om de data in een geschikt formaat te krijgen voor verdere analyse. Het resultaat is een CSV-bestand waarin de verschillende wijken en buurten zijn opgenomen, met bijbehorende variabelen die gebruikt kunnen worden voor de clusteranalyse.

2. **EDA.ipynb**  
   Dit notebook bevat de Exploratory Data Analysis (EDA) van de CBS data. In dit stadium worden de data verkend, en worden keuzes gemaakt over welke variabelen meegenomen worden in de clustering en hoe de data voorbereid moeten worden. De inzichten uit de EDA worden gebruikt in de preprocessing-stap.

3. **feature_importance.py**  
   Dit script bevat code snippets om de belangrijkheid van verschillende features in de dataset te evalueren. Het helpt bij het begrijpen welke variabelen het meeste invloed hebben op de clustering en biedt input voor het optimaliseren van het model.

4. **cluster_kmeans.py**  
   Hier vind je een implementatie van KMeans clustering, die kan worden toegepast op de geprepareerde CBS data. Dit script is bedoeld als een startpunt voor het uitvoeren van de clustering zelf.

5. **cluster_analysis.ipynb**  
   Dit notebook vergelijkt verschillende clusteringmethoden, zoals KMeans, Hiërarchische clustering en DBSCAN, om te bepalen welke methode het beste resultaat geeft voor het clusteren van wijken en buurten. Dit notebook geeft ook inzicht in de kwaliteit van de verschillende clusters en helpt bij het interpreteren van de resultaten.

### Vereisten

Voor het draaien van de scripts en notebooks in deze repository zijn de volgende Python libraries vereist:
- pandas
- numpy
- sklearn
- matplotlib
- jupyter

Deze kun je installeren met het volgende commando:

```bash
pip install <library>
```

### Hoe te gebruiken

1. **Data Preprocessing**: Start met het uitvoeren van `preprocessing.py` om de CBS data voor te bereiden. Dit script genereert een CSV-bestand met de benodigde data.
   
2. **Exploratory Data Analysis**: Bekijk de EDA in het `EDA.ipynb` notebook om inzicht te krijgen in de data.

3. **Feature Importance**: Gebruik `feature_importance.py` om te bepalen welke variabelen belangrijk zijn voor de clustering.

4. **Cluster Analysis**: Voer verschillende clusteringmethodes uit en vergelijk de resultaten in `cluster_analysis.ipynb`.

### Doel van de Workshop

Het doel van deze workshop is om deelnemers inzicht te geven in hoe clustering kan worden toegepast op CBS data om vergelijkbare wijken en buurten te groeperen. Dit kan bijvoorbeeld gebruikt worden om best practices te identificeren voor het verbeteren van de leefbaarheid in wijken met lage scores op indicatoren zoals sociale samenhang.

Veel succes!

### Contact

Als je vragen hebt over deze repository, neem dan gerust contact op met de f.feenstra@pl.hanze.nl
