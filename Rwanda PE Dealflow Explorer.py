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
    layout="wide"
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
    # Chargement du fichier CSV depuis la racine ou le dossier
    return pd.read_csv("Rwanda_Pe_DealFlow_Cleaned.csv")
# Appel de la fonction pour creer la variable globale
df_Origine= load_data()


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
                    options=Option_Location,
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
option_ESG=df_Origine[Col_ESG].dropna().unique().tolist() if Col_ESG in df_Origine.columns else []
filtre_ESG= st.sidebar.multiselect(
                label="ESG Score:",
                options=option_ESG,
                default=option_ESG
)

# --- Application des filtres sur le DataFrame

# Copie initiale des données
DF_Filtre = df_Origine.copy()

# 1. Filtre Location
if filtre_Location:
    DF_Filtre = DF_Filtre[DF_Filtre[Col_Location].astype(str).isin([str(x) for x in filtre_Location])]

# 2. Filtre Stage
if filtre_Stage:
    DF_Filtre = DF_Filtre[DF_Filtre[Col_Stage].astype(str).isin([str(x) for x in filtre_Stage])]

# 3. Filtre ESG
if filtre_ESG:
    DF_Filtre = DF_Filtre[DF_Filtre[Col_ESG].astype(str).isin([str(x) for x in filtre_ESG])]



# ==============================================================================
# 5. AFFICHAGE DES METRIQUES CLES ET RESULTATS
# ==============================================================================
st.subheader("Metrique Cles du Portfolio") 
col1, col2, col3, col4= st.columns(4)

with col1:
    st.metric(
        label="Selected Companies", 
        value=len(DF_Filtre) if not DF_Filtre.empty else 0
    )

with col2:
    if Col_EBITDA in DF_Filtre.columns and not DF_Filtre.empty:
        EBITDA_Moyen= DF_Filtre[Col_EBITDA].mean()
        st.metric(label="EBITDA Moyen", value=f"{EBITDA_Moyen:, .0f} $")

        #Verification si la moyenne est valide(non NaN):
        if pd.notna(EBITDA_Moyen):
            st.metric(label="EBITDA Moyen", value=f"{EBITDA_Moyen: , .0f} $")
        else:
            st.metric(label="EBITDA Moyen", value="N/A")

with col3:
    if Col_EBITDA in DF_Filtre.columns and not DF_Filtre.empty:
        val = DF_Filtre[Col_EBITDA].sum()
        st.metric(label="EBITDA Cumulé", value=f"{val:,.0f} $" if pd.notna(val) else "N/A")
    else:
        st.metric(label="EBITDA Cumulé", value="N/A")
        
with col4:
    if Col_Location in DF_Filtre.columns and not DF_Filtre.empty:
        val = DF_Filtre[Col_Location].nunique()
        st.metric(label="Zones Couvertes", value=val)
    else:
        st.metric(label="Zones Couvertes", value=0)

st.markdown("---")

# Affichage du tableau de donnees filtres
st.subheader("Liste des Opportunites")
st.dataframe(DF_Filtre, use_container_width=True)


