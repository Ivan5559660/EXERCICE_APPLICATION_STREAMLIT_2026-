
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |


Show are the stock **closing price** and **volume** of Google!
""") # "St.write" permet d'afficher du texte sur l'application Streamlit

"""
1ere APPROCHE: Utilisation de la librairie yfinance pour récupérer les données boursières de Google et les afficher sous forme de graphiques de prix de clôture et de volume.
"""
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# Define the ticjer Symbol
Ticker_Symbol='GOOGL'
Ticker_Symbol_2='AAPL'
Ticker_Symbol_3='MSFT'
Ticker_Symbol_4='AMZN'
Ticker_Symbol_5='TSLA'
Ticker_Symbol_6='NVDA'
Ticker_Symbol_7='META'
Ticker_Symbol_8='NFLX'
Ticker_Symbol_9='BABA'
Ticker_Symbol_10='INTC'

# Get data on the ticker
Ticker_Data=yf.Ticker(Ticker_Symbol)
Ticker_Data_2=yf.Ticker(Ticker_Symbol_2)
Ticker_Data_3=yf.Ticker(Ticker_Symbol_3)
Ticker_Data_4=yf.Ticker(Ticker_Symbol_4)
Ticker_Data_5=yf.Ticker(Ticker_Symbol_5)
Ticker_Data_6=yf.Ticker(Ticker_Symbol_6)
Ticker_Data_7=yf.Ticker(Ticker_Symbol_7)
Ticker_Data_8=yf.Ticker(Ticker_Symbol_8)
Ticker_Data_9=yf.Ticker(Ticker_Symbol_9)
Ticker_Data_10=yf.Ticker(Ticker_Symbol_10)

# Get the historical prices for this ticker
Ticker_DF=Ticker_Data.history(start='2010-5-31', end='2020-5-31')
Ticker_DF_2=Ticker_Data_2.history(start='2010-5-31', end='2020-6-30')
Ticker_DF_3=Ticker_Data_3.history(start='2010-6-30', end='2020-7-30')
Ticker_DF_4=Ticker_Data_4.history(start='2015-5-30', end='2022-6-30')
Ticker_DF_5=Ticker_Data_5.history(start='2020-7-30', end='2025-7-30')
Ticker_DF_6=Ticker_Data_6.history(start='2012-2-28', end='2023-3-30')
Ticker_DF_7=Ticker_Data_7.history(start='2022-8-30', end='2024-9-30')
Ticker_DF_8=Ticker_Data_8.history(start='2018-5-30', end='2021-6-30')
Ticker_DF_9=Ticker_Data_9.history(start='2024-10-30', end='2025-11-30')
Ticker_DF_10=Ticker_Data_10.history(start='2011-12-30', end='2023-12-30')


# Open high, low, volume, dividend and stock splits
st.write(""" ## Closing Price GOOGL""")
st.subheader("GOOGLE (GOOGL) - Closing Price")
st.line_chart(Ticker_DF.Close, color="#00FF7F") # Cette ligne permet de afficher le graphique de l'évolution du prix de clôture de l'action Google sur la période spécifiée
st.write(""" ## Volume Price GOOGL""")
st.subheader("GOOGLE (GOOGL) - Volume Price")
st.line_chart(Ticker_DF.Volume, color="#FF5733") # Cette ligne permet de afficher le graphique de l'évolution du volume de transactions de l'action Google sur la période spécifiée

st.write("""## Closing Price AAPL""")
st.subheader("APPLE (AAPL) - Closing Price")
st.line_chart(Ticker_DF_2.Close, color="#007AFF")
st.write("""## Volume Price AAPL""")
st.subheader("APPLE (AAPL) - Volume Price")
st.line_chart(Ticker_DF_2.Volume, color="#9D4EDD")

st.write(""" ## Closing Price MSFT""")
st.subheader("MICROSOFT (MSFT) - Closing Price")
st.line_chart(Ticker_DF_3.Close, color="#FFD700")
st.write(""" ## Volume Price MSFT """)
st.subheader("MICROSOFT (MSFT) - Volume Price")
st.line_chart(Ticker_DF_3.Volume, color="#00F5FF")

st.write("""## Closing Price AMZN""")
st.subheader("AMAZON (AMZN) - Closing Price")
st.line_chart(Ticker_DF_4.Close, color="#FF007F")
st.write("""## Volume Price AMZN""")
st.subheader("AMAZON (AMZN) - Volume Price")
st.line_chart(Ticker_DF_4.Volume, color="#4169E1")

st.write("""## Closing Price TSLA """)
st.subheader("TESLA (TSLA) - Closing Price")
st.line_chart(Ticker_DF_5.Close, color="#1B2A4A")
st.write("""## Volume Price TSLA""")
st.subheader("TESLA (TSLA) - Volume Price")
st.line_chart(Ticker_DF_5.Volume, color="#6C5CE7")

st.write("""## Closing Price NVDA""")
st.subheader("NVIDIA (NVDA) - Closing Price")
st.line_chart(Ticker_DF_6.Close, color="#8E44AD")
st.write("""## Volume Price NVDA""")
st.subheader("NVIDIA (NVDA) - Volume Price")
st.line_chart(Ticker_DF_6.Volume, color="#FF7F50")

st.write("""## Closing Price META""")
st.subheader("META (META) - Closing Price")
st.line_chart(Ticker_DF_7.Close, color="#FFBF00")
st.write("""## Volume Price META""")
st.subheader("META (META) - Volume Price")
st.line_chart(Ticker_DF_7.Volume, color="#FC8EAC")

st.write("""## Closing Price NFLX""")
st.subheader("NETFLIX (NFLX) - Closing Price")
st.line_chart(Ticker_DF_8.Close, color="#FFD1DC")
st.write("""## Volume Price NFLX""")
st.subheader("NETFLIX (NFLX) - Volume Price")
st.line_chart(Ticker_DF_8.Volume, color="#C77DFF")

st.write("""## Closing Price BABA""")
st.subheader("ALIBABA (BABA) - Closing Price")
st.line_chart(Ticker_DF_9.Close, color="#1B2A4A")
st.write("""## Volume Price BABA""")
st.subheader("ALIBABA (BABA) - Volume Price")
st.line_chart(Ticker_DF_9.Volume, color="#FF5733")

st.write("""## Closing Price INTC""")
st.subheader("INTEL (INTC) - Closing Price")
st.line_chart(Ticker_DF_10.Close, color="#00FF7F")
st.write("""## Volume Price INTC""")
st.subheader("INTEL (INTC) - Volume Price")
st.line_chart(Ticker_DF_10.Volume, color="#FFB6C1")

"""
2eme APPROCHE: Utilisation de la librairie yfinance pour récupérer les données boursières de Google et les afficher sous forme de graphiques de prix de clôture et de volume, avec des options d'interaction pour l'utilisateur.
OPTIMISATION.
"""

# Titre principal
st.title("Simple Stock Price App - Interactive")
st.write(" Visualisation des prix de cloture et volumes pour plusieurs actions boursieres")

# COnfiguration des entreprises(nom, symbole, couleur, prix, couleur de volume)
Companies=[('GOOGL', '#00FF7F', '#FF5733'),
              ('AAPL', '#007AFF', '#9D4EDD'),
              ('MSFT', '#FFD700', '#00F5FF'),
              ('AMZN', '#FF007F', '#4169E1'),
              ('TSLA', '#1B2A4A', '#6C5CE7'),
              ('NVDA', '#8E44AD', '#FF7F50'),
              ('META', '#FFBF00', '#FC8EAC'),
              ('NFLX', '#FFD1DC', '#C77DFF'),
              ('BABA', '#1B2A4A', '#FF5733'),
              ('INTC', '#00FF7F', '#FFB6C1')
           ]

# Creation de la boucle unique 'For' pour recuperer les donnees et afficher chaque section 
for symbol, color_close, color_vol in Companies:
    st.divider() # Ligne de separation visuelle entre les entreprises 
    st.header(f"Action:{symbol}")
    # Recuperation des donnees historiques sur 10 ans
    data= yf.Ticker(symbol).history(start='2020-01-30', end='2025-12-30')
    # Affichage du prix de cloture
    st.subheader(f"{symbol} - Closing Price ($)")
    st.line_chart(data.Close, color=color_close)
    # Affichage du volume
    st.subheader(f"{symbol} - Transaction Volume")
    st.line_chart(data.Volume, color=color_vol)







