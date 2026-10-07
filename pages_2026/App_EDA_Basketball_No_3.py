import streamlit as st
import pandas as pd
import base64 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer') # Afficher le titre principale de mon application en tres grands caracteres au sommet de la page centrale

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* ** Python librairies:** base64, pandas, streamlit
* **Data source:** [Baskeball-reference.com](https://www.baskeball)
""") # Permet d'afficher du texte formate en utilisant le langage Markdown

st.sidebar.header('User Input Features') # Permet d'afficher un sous titre de section a l'interieur du panneau lateral situe a gauche de l'ecran
selected_year=st.sidebar.selectbox('Year', list(reversed(range(2000, 2024)))) # Permet de creer un menu deroulant d'options dans la barre laterale. De plus, list(reversed(range(1950, 2024))) 

# Web scraping of NBA player stats
@st.cache_data # Un décorateur Streamlit qui met en cache le résultat de la fonction load_data. Cela évite de recharger et de re-télécharger les données du site web à chaque fois que l'utilisateur interagit avec l'application, ce qui améliore fortement les performances.
def load_data(year):
    url="https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html=pd.read_html(url, header=0) # Utilisation de Pandas pour lire et extraire tous les tableaux HTML trouvés à l'URL spécifiée. L'argument header=0 indique que la première ligne du tableau contient les en-têtes de colonnes.
    df=html[0] # Sélection du premier tableau extrait de la page web (index 0) et stockage de celui-ci dans la variable DataFrame df
    raw= df.drop(df[df.Age=='Age'].index) # Suppression des lignes d'en-tête répétées au milieu du tableau web. En supprimant les lignes où la colonne Age a pour valeur la chaîne 'Age', on nettoie les doublons d'en-têtes présentés périodiquement sur le site.
    # Suppression de la colonne de rang (Rk, ou RK)
    playerstats=raw.drop(['Rk', 'RK'], axis=1, errors='ignore').fillna(0) # Suppression de la colonne nommé 'Rk' (Rang / Rank) du DataFrame, car l'argument axis=1 spécifie qu'il s'agit d'une colonne.
    playerstats= playerstats.fillna(0)
    # Nettoyage des noms des colonnes
    playerstats.columns=[str(c).strip() for c in playerstats.columns]
    return playerstats
# Chargement des donnees selon l'annee selectionnee
playerstats= load_data(selected_year)
# Detection automatique de la colonne d'equipe ('Tm' ou 'Team')
team_column='Tm' if 'Tm' in playerstats.columns else 'Team'
# Sidebar - Team selection
sorted_unique_team=sorted(playerstats[team_column].unique().astype(str))
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team) # Crée un menu déroulant à choix multiples dans la barre latérale Streamlit avec le titre 'Team'. Le deuxième argument définit les options sélectionnables (sorted_unique_team), et le troisième indique que toutes les équipes sont sélectionnées par défaut.

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG'] # Définit une liste contenant les abréviations des 5 positions du basket-ball
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos) # Crée un second menu à choix multiples dans la barre latérale intitulé 'Position'. Par défaut, toutes les positions sont sélectionnées.

# Filtering data(Filtrage des donnees)
df_selected_team = playerstats[(playerstats[team_column].isin(selected_team)) & (playerstats['Pos'].isin(selected_pos))]
# Affichage des resultats(display)
st.header('Display Player Stats of Selected Team(s)') # Affiche un titre de section (Header) sur la page principale
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.') # Affiche un titre de section (Header) sur la page principale
st.dataframe(df_selected_team) # Affiche le tableau de données filtré (df_selected_team) sous forme de grille interactive sur l'application Streamlit.

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False) # Convertit le DataFrame en une chaîne de caractères au format CSV, en excluant les index de lignes (index=False).
    b64 = base64.b64encode(csv.encode()).decode()  # Encode le texte CSV en binaire (ASCII/UTF-8), puis en une chaîne Base64 pour pouvoir l'intégrer directement sous forme d'URL de données (Data URI).
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>' # Crée une balise HTML d'ancrage (<a>) contenant les données encodées, permettant au navigateur de télécharger directement un fichier nommé 'playerstats.csv'.
    return href # La fonction renvoie le lien HTML généré.


st.markdown(filedownload(df_selected_team), unsafe_allow_html=True) # Appelle la fonction avec les données filtrées (df_selected_team) et affiche le lien de téléchargement sur la page Streamlit. L'option unsafe_allow_html=True autorise Streamlit à interpréter le code HTML brut.

# Heatmap # La carte de chaleur
if st.button('Intercorrelation Heatmap'): # Crée un bouton dans l'interface intitulé. Ce code ci-dessous ne s'exécute que lorsque l'utilisateur clique sur ce bouton.
    st.header('Intercorrelation Matrix Heatmap') # Affiche un titre de section sur la page : "Intercorrelation Matrix Heatmap"
    df_selected_team.to_csv('output.csv',index=False) # Sauvegarde le DataFrame filtré dans un fichier local 'output.csv', puis le re-télécharge dans df. (Cette étape permet de s'assurer que toutes les colonnes sont relues avec les types de données appropriés pour la matrice de corrélation).
    df = pd.read_csv('output.csv') 

    df_numeric=df.select_dtypes(include=['float64','int64']) # Filtrage explicite des colonnes avant calcul de correlation
    corr = df_numeric.corr() # Calcule la matrice de corrélation de Pearson entre toutes les colonnes numériques du DataFrame.
    mask = np.zeros_like(corr) # Génère un masque booléen pour masquer le triangle supérieur de la matrice de corrélation (car la matrice est symétrique), afin d'éviter la répétition des informations sur le graphique.
    mask[np.triu_indices_from(mask)] = True # Génère un masque booléen pour masquer le triangle supérieur de la matrice de corrélation (car la matrice est symétrique), afin d'éviter la répétition des informations sur le graphique.
    with sns.axes_style("white"): # Configure un fond blanc
        f, ax = plt.subplots(figsize=(7, 5)) # initialise une figure Matplotlib de dimensions 7x5 pouces
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True) # puis dessine la matrice de corrélation à l'aide de Seaborn (sns.heatmap) en appliquant le masque et en fixant la valeur maximale de corrélation à 1.
    st.pyplot(f) # Affiche le graphique Matplotlib/Seaborn ainsi généré directement sur l'interface de l'application Streamlit.