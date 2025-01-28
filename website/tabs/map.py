import streamlit as st
import pydeck as pdk  

def show_map():
    st.header("Détection de champignon")
    
    # Choice of the date of detection
    st.date_input("Sélectionnez la date de détection")

    # Place the map in the center of France
    view_state = pdk.ViewState(
        latitude=46.603354,
        longitude=1.888334,
        zoom=5,
        pitch=0,
        min_zoom=5,
        max_zoom=15
    )

    # Map display
    r = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v10",
        initial_view_state=view_state
    )

    st.pydeck_chart(r)