'''
I.	  TABLEAU DE BORD DE PORTEFEUILLE PME (Rwanda PE Dealflow Explorer)
•	Concepts réutilisés : st.sidebar.multiselect pour filtrer les entreprises par secteur (Agro-business, Fintech, Énergie) et par étape d'investissement 
(Seed, Series A, Buyout). 

•	Cas d'usage : Filtrer dynamiquement un portefeuille d'entreprises rwandaises et afficher leurs métriques clés (chiffre d'affaires, EBITDA, valorisation). 

• Objectif de l'application : 
                                - Filtrage des entreprises rwandaises par emplacement et etapes d'investissement et criteres ESG
                                - Filtrage des entreprises rwandaises par etapes d'investissement et EBITDA
                                - Affichage des metriques des metriques cles
                                
'''

'''
Filtrage dynamique d'un portefeuille d'entreprises rwandaises et affichage de leurs metriques cles.s
1. st.sidebar.header('')


2. st.sidebar.selectbox()




3. st.sidebar.multiselect 
sert à créer une liste de sélection multiple positionnée dans le menu latéral (sidebar) d'une application Streamlit. Elle permet à l'utilisateur de choisir une ou 
plusieurs options parmi une liste proposée. Le résultat retourné par cette fonction est une liste Python contenant les éléments sélectionnés.

    3.1. Pourquoi l'utiliser ?

        Gestion de filtres : C'est le composant idéal pour filtrer des données (par exemple, filtrer un tableau Pandas par pays, catégorie, statut ou période).

        Gain d'espace : Placer le sélecteur dans la barre latérale (st.sidebar) permet de désencombrer la zone principale de votre application et de la réserver à 
        l'affichage des graphiques, des tableaux ou des indicateurs.


'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
plt.style.use('ggplot')
import yfinance as yf
import streamlit as st
# Importation des donnees financieres au format csv

# ===========================================================================
# 1. CONFIGURATION DE LA PAGE ET STYLE CUSTOM (CSS)
# ===========================================================================
st.set_page_config(
    page_title="RWANDA PE DEALFLOW EXPLORER",
    page_icon="RW",
    layout="Wide"
) # 

# Injection du style CSS personnalise
st.markdown("""
        <style>
        .stApp {
        background: radial-gradient(circle at 50% 20%, #1e293b 0%, #0f172a 100%); 
        color: #f8fafc;} </style> """, unsafe_allow_html=True)

# =============================================================================
# 2. EN-TETE ET DESCRIPTION 
# =============================================================================
st.title("RWANDA PE DEALFLOW EXPLORER")

st.markdown("""
            Executive dashboard dedicated to performance analysis of Rwandan SME portfolios.
            This platform centralizes the tracking of key financial metrics (EBITDA, IRR, profitability ratios)
            and multi-sector time-series monitoring.
            """
)

st.divider()


# ==============================================================================
# 3. CHARGEMENT ET PRESENTATION DES DONNEES
#===============================================================================
@st.cache_data #
def load_data():
    # Chargement du fichier CSV nettoye
    df_Origine=pd.read_csv("C:\Users\hp\OneDrive\Documents\VSCODE_WORKING_2026\EXERCICES_APPS_2026\pages_2026\Rwanda_Pe_DealFlow_Cleaned.csv")
    return df_Origine


# ==============================================================================
# 4. BARRE LATERALE (SIDEBAR) _ FILTRES MULTISELECT
# ==============================================================================
st.sidebar.header("Filtres de Recherche")

# Remplacer les noms entre guillemets par le nom exact des colonnes dans le CSV
Col_Location="Location"
Col_Stage="INVESTMENT_STAGE"
Col_ESG="ESG_Score"
Col_EBITDA="EBITDA_RWF_M"

# --- Filtre 1: Location
Option_Location= df_Origine[Col_Location].dropna().unique().tolist() if Col_Location in df_Origine.columns else[]
filtre_Location= st.sidebar.multiselect(
                    label="Location/District:",
                    Options=Option_Location,
                    default=Option_Location
)

# --- Filtre 2: Etape d'investissement
Option_stage=df_Origine[Col_Stage].dropna().unique().tolist() if Col_Stage in df_Origine.columns else []
filtre_stage= st.sidebar.multiselect(
                label="Investment Stage:",
                options=Option_stage,
                default=Option_stage

)

# --- Filtre 3: Criteres ESG
option_ESG=df_origine[Col_ESG].dropna().unique().tolist() if Col_ESG in df_Origine.columns else []
filtre_ESG= st.sidebar.multiselect(
                label="ESG Score:",
                options="option_ESG",
                default="option_ESG"
)

# --- Application des filtres sur le DataFrame
DF_Filtre= df_Origine.copy() #

if Col_Lociation in DF_Filtre.columns and filtre_Location:
    DF_Filtre=DF_Filtre[DF_Filtre[Col_Location].isin(filtre_Location)]

if Col_Stage in DF_Filtre.columns and filtre_stage:
    DF_Filtre=DF_Filtre[DF_Filtre[Col_ESG].isin(filtre_stage)]  

if Col_ESG in DF_Filtre.columns and filtre_ESG:
    DF_Filtre=DF_Filtre[DF_Filtre[Col_ESG].isin(filtre_ESG)]



# ==============================================================================
# 5. AFFICHAGE DES METRIQUES CLES ET RESULTATS
# ==============================================================================
st.subheader("Metrique Cles du Portfolio") 
col1, col2, col3, col4- st.columns(4)

with col1:
    st.metric(
            label="Selected Companies"
            value=len(DF_Filtre)

    )

with col2:
    if Col_EBITDA in DF_Filtre.columns and not DF_Filtre.empty:
        EBITDA_Moyen= DF_Filtre[Col_EBITDA].mean()
        st.metric(label="EBITDA Moyen", value=f"{EBITDA_Moyen:, .0f} $")
    else:
        st.metric(label="EBITDA Moyen", value="N/A")

with col3:
    if Col_EBITDA in DF_Filtre.columns and not DF_Filtre.empty:
        ebitda_total=DF_Filtre[Col_EBITDA].sum()
        st.metric(label="EBITDA Cumule", value=f"{ebitda_total:,.0f} $")
    else:
        st.metric(label="EBITDA Cumule", value="N/A")
with col4:
    if COL_EMPLACEMENT in df_filtre.columns and not df_filtre.empty:
        nb_villes = df_filtre[COL_EMPLACEMENT].nunique()
        st.metric(label="Zones Couvertes", value=nb_villes)
    else:
        st.metric(label="Zones Couvertes", value="0")

st.markdown("---")

# Affichage du tableau de donnees filtres
st.subheader("Liste des Opportunites")
st.dataframe(DF_Filtre, use_container_width=True)


