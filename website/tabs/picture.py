import streamlit as st
from PIL import Image
import numpy as np

def show_predictions():
    st.header("Prédictions du champignon")
    
    # Diviser la page en deux colonnes pour importer et prendre une photo
    col1, col2 = st.columns(2)

    # Colonne de gauche : Importer une photo
    with col1:
        st.subheader("Importer une photo")
        uploaded_file = st.file_uploader("Importer ou glisser une image", type=["jpg", "jpeg", "png"])

    # Colonne de droite : Prendre une photo avec la caméra
    with col2:
        st.subheader("Prendre une photo")
        show_camera = st.checkbox("Afficher la caméra")
        camera_photo = None
        if show_camera:
            camera_photo = st.camera_input("Prendre une photo")

    # Afficher l'image sélectionnée ou capturée au centre
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        toxic_int = np.random.randint(0,100)
        if toxic_int > 30:
            st.markdown(f'<div class="centered-text-toxic">{toxic_int} % TOXIQUE DON\'T EAT</div>', unsafe_allow_html=True)
            st.image(image, caption="Image importée", use_column_width=True)
        else :
            st.markdown(f'<div class="centered-text-edible">{toxic_int} % TOXIQUE, U HAVE TO COOK IT</div>', unsafe_allow_html=True)
            st.image(image, caption="Image importée", use_column_width=True)

    elif camera_photo is not None:
        image = Image.open(camera_photo)
        toxic_int = np.random.randint(0,100)
        if toxic_int > 30:
            st.markdown(f'<div class="centered-text-toxic">{toxic_int} % TOXIQUE DON\'T EAT</div>', unsafe_allow_html=True)
            st.image(image, caption="Image importée", use_column_width=True)
        else :
            st.markdown(f'<div class="centered-text-edible">{toxic_int} % TOXIQUE, U HAVE TO COOK IT</div>', unsafe_allow_html=True)
            st.image(image, caption="Image importée", use_column_width=True)
