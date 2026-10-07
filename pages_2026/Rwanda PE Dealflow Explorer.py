'''
1.	  TABLEAU DE BORD DE PORTEFEUILLE PME (Rwanda PE Dealflow Explorer)
•	Concepts réutilisés : st.sidebar.multiselect pour filtrer les entreprises par secteur (Agro-business, Fintech, Énergie) et par étape d'investissement 
(Seed, Series A, Buyout). 

•	Cas d'usage : Filtrer dynamiquement un portefeuille d'entreprises rwandaises et afficher leurs métriques clés (chiffre d'affaires, EBITDA, valorisation). 

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
df_Origine = pd.read_csv("Rwanda_Pe_DealFlow_Cleaned.csv")

# 2. Nettoyer les guillemets superflus dans les valeurs textuelles en creant une boucle for:
# for col in df_Origine.select_dtypes(include=['str', 'object']).columns:
    #df_Origine[col]=df_Origine[col].astype(str).str.replace('"', '').str.strip()

# 3.1. Anonymisation et adaptation aux PME Rwandaises en creant une liste
#Companies_Rwanda=['Kigali AgriTech','Kivu Green Energy','Huye Tech Hub','Gicumbi Dairy','Nyarugenge Hydro Power','Musanze Food Processing','Bugesera Housing Corp','Kigali Health Partners','Akagera Express','Rwamagana Solar Ltd','Rubavu Eco-Lodge','Nyamata Textile']

# 3.2. Creation de dictionnaire
#Mapping_Secteurs={
    #'Management':'Fintech & ICT',
    #'Technician':'Renewable Energy',
    #'Blue-Collar':'Manufacturing',
    #'Admin':'Real Estate',
    #'Services':'Hospitality & Tourism',
    #'Retired':'AgriBusiness',
    #'Self-Employed':'Healthcare',
    #'Entrepreneur':'Logistics & Trade',
    #'Unemployed':'Education',
    #'Housemaid':'Retail & FMCG',
    #'Student':'CleanTech',
    #'Unknown':'Diversified Services'

# 3.3. Creation de liste pour ville du Rwanda et etapes d'investissement:
#Cities_Rwanda=['Kigali','Musanze','Rubavu','Huye','Rwamagana','Bugesera']
#Investment_Stage=['Seed','Series A','Growth Equity','Buyout']

# 4. Remplacement et renommage des colonnes
#df_Origine['Company_Name']=[Companies_Rwanda[i % len(Companies_Rwanda)] for i in range(len(df_Origine))]
#df_Origine['Sector']=df_Origine['job'].map(Mapping_Secteurs).fillna('Other')
#df_Origine['Location']=np.random.choice(Cities_Rwanda, size=len(df_Origine))
#df_Origine['INVESTMENT_STAGE']=np.random.choice(Investment_Stage, size=len(df_Origine))

# Reprise des colonnes chiffrees existantes
#df_Origine['Years_in_Operation']=df_Origine['age']
#df_Origine['EBITDA_RWF_M']=df_Origine['balance'].apply(lambda x: abs(x) + 100 ) # Rendu positif 
#df_Origine['IRR_Target_%']=np.round((df_Origine['duration']/10).clip(10, 35), 2)
#df_Origine['ESG_Score']=np.random.randint(65, 99, size=len(df_Origine))

# 5. Selection et conservation des colonnes finales nettoyees en creant une liste
#Colonnes_Finales=['Company_Name','Sector','Location','INVESTMENT_STAGE','Years_in_Operation','EBITDA_RWF_M','IRR_Target_%','ESG_Score']

#Final_Data_Project= df_Origine[Colonnes_Finales]

# 6. Sauvegarde du fichier propre dans le dossier actuel

#Final_Data_Project.to_csv('Rwanda_Pe_DealFlow_Cleaned.csv', index=False)
#print("Nettoyage termine ! Fichier 'Rwanda_Pe_DealFlow_Cleaned.csv' cree avec succes")

#Final_Data_Project


# 7. Titre principale en en-tete
st.title('RWANDA PE DEALFLOW EXPLORER') # Afficher le titre principale de mon application en tres grands caracteres au sommet de la page centrale
# 8. Commentaire du projet en dessous de l'en-tete
st.markdown("""
Executive dashboard dedicated to performance analysis of Rwandan SME portfolios. This platform centralizes the tracking of key financial metrics 
(EBITDA, IRR, profitability ratios) and multi-sector time-series monitoring
""") # Permet d'afficher du texte formate en utilisant le langage Markdown

# INJECTION CSS POUR LE FOND ET LE STYLE
st.markdown("""
    <style>
    /* Fond principal de l'application avec un dégradé subtil */
    .stApp {
        background: radial-gradient(circle at 50% 20%, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    
    /* Style de la carte d'en-tête */
    .header-card {
        background-color: rgba(30, 41, 59, 0.7);
        padding: 2.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
        backdrop-filter: blur(8px);
    }
    
    .header-title {
        color: #ffffff;
        font-weight: 800;
        letter-spacing: -0.025em;
        margin-bottom: 0.75rem;
    }
    
    .header-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# Contenu de l'en-tête dans une structure stylisée
st.markdown("""
    <div class="header-card">
        <h1 class="header-title">RWANDA PE DEALFLOW EXPLORER</h1>
        <p class="header-subtitle">
            Executive dashboard dedicated to performance analysis of Rwandan SME portfolios. 
            This platform centralizes the tracking of key financial metrics (EBITDA, IRR, profitability ratios) 
            and multi-sector time-series monitoring.
        </p>
    </div>
""", unsafe_allow_html=True)





# %%
