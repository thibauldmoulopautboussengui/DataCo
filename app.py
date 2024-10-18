import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title("Dashboard des données déjà scrapées")

# Charger les données depuis un fichier CSV
uploaded_file = st.file_uploader("Charger les données", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.write(df.head())

    # Bouton de téléchargement des données
    st.sidebar.download_button(
        label="Télécharger les données",
        data=df.to_csv(index=False),
        file_name='scraped_data.csv',
        mime='text/csv'
    )
    
    # Afficher un dashboard simple
    st.title("Visualisation des données")
    
    # Exemple : Histogramme d'une colonne spécifique (modifiez selon vos colonnes)
    if 'Price' in df.columns:
        df['Price'] = df['Price'].str.replace('$', '').astype(float)

        fig, ax = plt.subplots()
        sns.histplot(df['Price'], kde=True, ax=ax)
        st.pyplot(fig)

    # Ajouter d'autres visualisations
    if 'Rating' in df.columns:
        st.write("Distribution des évaluations")
        fig, ax = plt.subplots()
        sns.countplot(x='Rating', data=df, ax=ax)
        st.pyplot(fig)

# Formulaire d'évaluation
st.title("Formulaire d'évaluation")

with st.form("feedback_form"):
    name = st.text_input("Votre nom")
    rating = st.slider("Notez l'application", 1, 5)
    feedback = st.text_area("Vos retours")

    submitted = st.form_submit_button("Soumettre")

    if submitted:
        st.write(f"Merci pour votre évaluation, {name} !")
        st.write(f"Votre note : {rating}/5")
        st.write(f"Vos retours : {feedback}")