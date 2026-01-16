
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd

url_log = "https://raw.githubusercontent.com/DPewpew/Streamlit-Partie-3/refs/heads/main/log.csv"

@st.cache_data
def load_credentials(url: str) -> dict:
    df = pd.read_csv(url)

    required = ["name", "password", "email", "failed_login_attempts", "logged_in", "role"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Colonnes manquantes: {missing} | Colonnes trouvées: {list(df.columns)}")

    # Normaliser types
    df["failed_login_attempts"] = pd.to_numeric(df["failed_login_attempts"], errors="coerce").fillna(0).astype(int)
    df["logged_in"] = df["logged_in"].astype(str).str.lower().isin(["true", "1", "yes", "y", "vrai"])

    usernames = {}
    for _, row in df.iterrows():
        username = str(row["name"]).strip()  
        usernames[username] = {
            "name": str(row["name"]).strip(),
            "password": str(row["password"]),
            "email": str(row["email"]).strip(),
            "failed_login_attempts": int(row["failed_login_attempts"]),  
            "logged_in": bool(row["logged_in"]),
            "role": str(row["role"]).strip(),
        }

    return {"usernames": usernames}

# 1) Charger les comptes depuis GitHub
lesDonneesDesComptes = load_credentials(url_log)

# 2) Créer l’authenticator
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

# 3) Login
authenticator.login()


    
def log():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")


if st.session_state["authentication_status"]:
    user_name = st.session_state["name"]

    def accueil():
        st.title("Bienvenue sur ma page")
        col1, col2 = st.columns(2)

        with col1:
            st.image("https://www.gifcen.com/wp-content/uploads/2022/01/clapping-gif.gif")

        with col2:
            st.image("https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUyeHJnYmw0YmM1b25lNWN1anZzYXNpOGpsN2p5YWd5c2x5bmxlZ29tZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xT77XWum9yH7zNkFW0/200.gif")

    def page_2():
        st.title("Les rêves de Paul")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://media0.giphy.com/media/jk7AiMeeQyelPuqjQt/giphy.gif")

        with col2:
            st.image("https://animesher.com/orig/2/204/2046/20463/animesher.com_anime-gifs-gifs-subway-2046395.gif")


    def page_3():
        st.title("La réalité de Paul")
        st.image("https://media.tenor.com/pWomGhqRkowAAAAM/subway-awkward.gif")  

    def page_4():
        st.title("Notre réaction en face de paul")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image("https://media0.giphy.com/media/v1.Y2lkPTZjMDliOTUyZHRjMjh6bXV1cmQ3MTN4MjZlMGVyM290N215ZmhhcnFwYmt3Z2RvZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/29HRejgahYenVsohB5/200w.gif")
        with col2:
            st.image("https://media0.giphy.com/media/1PgPvWLfXGkCY/giphy-downsized.gif")
        with col3:
            st.image("https://images.ecency.com/p/2ufhwNgM3qHKGxq8wdcWAiFpcm29FF1vQ7VZHkTuxDWpeRA2JBiXSRUDv2SiqmhCwiqhLXSeZ.png?format=match&mode=fit")
        st.image("https://media0.giphy.com/media/APcFiiTrG0x2/giphy.gif")

    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    with st.sidebar:
        st.title(f"Bienvenue {user_name} !")
        selection = option_menu(
                menu_title=None,
                options = ["Accueil", "Paul Dream's", "Réality", "Nos réaction"],
            )
        authenticator.logout("Déconnexion")
    if selection == "Accueil":
        accueil()
    elif selection == "Paul Dream's":
        page_2()
    elif selection == "Réality":
        page_3()
    elif selection == "Nos réaction":
        page_4() 
    
    

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')