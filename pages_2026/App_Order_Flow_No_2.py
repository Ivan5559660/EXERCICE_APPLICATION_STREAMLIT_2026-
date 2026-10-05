import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
import yfinance as yf
import streamlit as st
import altair as alt
from PIL import Image

############################
# Page Title
############################

image=Image.open(r"C:\Users\hp\Downloads\ChatGPT Image 2 oct. 2026, 01_10_39.png")

st.image(image, use_container_width=True)

st.write("""#Connectivity Infrastructure Application

## A trusted digital infrastructure for Rwanda’s capital markets


***
""")

############################
# Input Text Box
############################
"""
Pour adapter ce concept au domaine de la finance de marche, l'equivalent parfait d'une sequence genetique (comme l'ADN) est une sequence d'ordre boursiers(un carnet d'ordre ou Order Log) ou un flux de cotations(Tick Data). Au lieu de compter des nucleotides(A, T, C, G), notre application va analyser la frequence et la repartition des actions des investisseurs: Achats, Ventes, Annulations et Executions.
"""

# st.sidebar.header('')
st.header('')

# Input
sequence_input=""">Order Log AAPL 2026-10-01
                  BUY_LIMIT_150_AAPL
                  BUY_LIMIT_150_AAPL
                  SELL_LIMIT_152_AAPL
                  BUY_LIMIT_150_AAPL
                  EXECUTE_ORDER_150
                  CANCEL_ORDER_152
                  BUY_LIMIT_153_AAPL
                  EXECUTE_ORDER_151
                  BUY_LIMIT_150_AAPL
                  CANCEL_ORDER_150
                  EXECUTE_ORDER_153
                """

# Ce code applique exactement la même structure que la vidéo (nettoyage de l'en-tête, filtrage et comptage des éléments), mais transposée aux opérations boursières

st.title("Order Flow Analysis Web Application")
st.write(""" Cette application analyse le flux d'ordre bruts d'un carnet pour en extraire la repartition des operations.""")
st. header("Enter Order Sequence")
# Sequence Input
sequence_input=""">Order Log AAPL 2026-10-01
                  BUY_LIMIT_150_AAPL
                  BUY_LIMIT_150_AAPL
                  SELL_LIMIT_152_AAPL
                  BUY_LIMIT_150_AAPL
                  EXECUTE_ORDER_150
                  CANCEL_ORDER_152
                  BUY_LIMIT_153_AAPL
                  EXECUTE_ORDER_151
                  BUY_LIMIT_150_AAPL
                  CANCEL_ORDER_150
                  EXECUTE_ORDER_153
                """
# Transformation en DataFrame
lines=[line.strip() for line in sequence_input.splitlines() if line.strip()]
# Affichage sous forme de tableau a une colonne 
df_lines=pd.DataFrame(lines, columns=["Order Details"])
st.subheader("Order Input")
st.table(df_lines) # N.B: "st.stable() sert a afficher des tableaux statistiques"
# Zone de texte Streamlit:
# st.table(sequence_input) # N.B: "st.stable() sert a afficher des tableaux statistiques"
sequence = sequence_input.splitlines()
# 1. Traitement de la sequence (Meme logique que le script DNA)
sequence=lines
sequence=sequence[1:] # On ignore la 1ere ligne d'en tete (> Order Log...)
sequence=" ".join(sequence) # Fusion du texte en une seule ligne

st.write("""""")
st.header("INPUT (Processed Orders)")
st.write(sequence)

# 2. Comptage des types d'ordres
st.header("OUTPUT(Order Type Distribution)")

# Compter l'occurence de chaque mot-cle financier
num_buy=sequence.count("BUY")
num_sell=sequence.count("SELL")
num_execute=sequence.count("EXECUTE")
num_cancel=sequence.count("CANCEL")

# 3. Affichage des resultats sous forme de dictionnaire/DataFrame
st.header("1. Dictionnaire des frequences")
order_count={
    "BUY(Achats)": num_buy,
    "SELL(Ventes)": num_sell,
    "EXECUTE(Executions)": num_execute,
    "CANCEL(Annulations)": num_cancel
}

st.write(order_count)

# 4. Affichage du tableau structure
st.subheader("2. Tableau recapitulatif")
df_lines_2=pd.DataFrame.from_dict(order_count, orient="index", columns=["quantities"])
st.dataframe(df_lines_2)

# 5. Affichage d'un graphique a barres
st.subheader("3. Graphique du flux d'ordes")
st.bar_chart(df_lines_2)