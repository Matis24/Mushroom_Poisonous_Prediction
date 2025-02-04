import streamlit as st
from tabs.picture import show_predictions
from tabs.map import show_map
from tabs.presentation import presentation
from Weather.weather import show_weather

# python -m streamlit run Poisonous_Mushroom_Detection/Website/app.py
st.markdown(
    """
    <style>
    .centered-text-toxic {
        color: red;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
    }
    .centered-text-edible {
        color: green;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

show_weather()
    
# Afficher l'application avec un fond dynamique

st.title("ChampIA")

tabs = st.tabs(["Présentation du site", "Prédictions du champignon", "Détection de champignon"])
    
# Presentation of the website
with tabs[0]:
    presentation()

# Prediction of the mushroom with picture   
with tabs[1]:
    show_predictions()

# Detection of the mushroom on the map
with tabs[2]:
    show_map()
