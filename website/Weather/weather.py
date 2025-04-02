#%%
import streamlit as st
import requests
from dotenv import load_dotenv
import os
import base64
from pathlib import Path

#%% Récupération de la clé API
load_dotenv("./.env")
API_KEY = os.getenv("API_KEY_WEATHER")

#%% Coordonnées des villes
cities = {
    "Paris": {"latitude": 48.8566, "longitude": 2.3522},
    "Lyon": {"latitude": 45.7640, "longitude": 4.8357},
    "Marseille": {"latitude": 43.2965, "longitude": 5.3698},
    "Bordeaux": {"latitude": 44.8378, "longitude": -0.5792},
    "Toulouse": {"latitude": 43.6047, "longitude": 1.4442},
    "Nice": {"latitude": 43.7102, "longitude": 7.2620},
    "Lille": {"latitude": 50.6292, "longitude": 3.0573},
}

#%% Fonction pour récupérer la météo    
def get_weather(lat, lon, api_key):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    try:
        response.status_code == 200
        return response.json()
    except Exception as e:
        return e
    
    
#%% Affichage de la météo
st.sidebar.markdown(
        """
        <h2 style='text-align: center; padding: 10px; border-bottom: 2px solid #FFD700;'>
        🌤️ Météo</h2>
        """, 
        unsafe_allow_html=True
    )

def show_weather():
    
    st.sidebar.header("Sélectionnez une ville")
    city_name = st.sidebar.selectbox("Choisissez une ville", list(cities.keys()))
    lat = cities[city_name]["latitude"]
    lon = cities[city_name]["longitude"]
    
    weather_data = get_weather(lat, lon, API_KEY)
    print(weather_data)
    if weather_data:
        # Extraction des informations
        temperature = round(weather_data['weather']['temp']-273.15,1)
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        city = weather_data['name']

        # Affichage de la météo
        st.sidebar.write(f"### {city} : {description.capitalize()}")
        st.sidebar.image(f"http://openweathermap.org/img/wn/{icon}@2x.png")
        st.sidebar.metric("🌡️ Température actuelle", f"{temperature}°C")
        
        # Message personnalisé selon le temps
        if "rain" in description:
            st.sidebar.info("🌧️ Prenez un parapluie, il pleut à Paris.")
        elif "sun" in description or "ciel dégagé" in description:
            st.sidebar.success("☀️ Profitez du soleil à Paris !")
        else:
            st.sidebar.write("🌥️ Temps nuageux, une belle journée pour une balade.")
    else:
        st.sidebar.error("Impossible de récupérer les données météo. Vérifiez la clé API ou la connexion.")
        
    def get_base64(file_path):
        with open(file_path, "rb") as file:
            data = file.read()
        return base64.b64encode(data).decode()

    # Charger et encoder le GIF
    gif_path = Path("./Weather/rain.gif")
    gif_base64 = get_base64(gif_path)

    # Appliquer le GIF en arrière-plan
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebarContent"] {{
            background: url("data:image/gif;base64,{gif_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            overflow: hidden;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )