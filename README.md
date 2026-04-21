# 🌐 Streamlit — App Multi-pages avec Authentification

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Status](https://img.shields.io/badge/Status-Terminé-brightgreen)

> Application Streamlit multi-pages avec système d'authentification, réalisée dans le cadre d'un exercice de cours.

---

## À propos

Ce projet est un exercice pratique réalisé pendant ma **formation Data Analyst**, pour apprendre à structurer une application Streamlit avec navigation et gestion des accès utilisateurs.

Il fait partie de mon portfolio GitHub, conçu pour montrer les compétences acquises tout au long de ma formation.

> 👤 **[Mon profil GitHub →](https://github.com/DPewpew)**

---

## Structure du projet

```
├── partie_3_chat.py      # Application principale
├── log.csv               # Comptes utilisateurs (hébergé sur GitHub)
├── requirements.txt
└── README.md
```

---

## Fonctionnalités

- **Authentification** — connexion sécurisée via `streamlit-authenticator`, comptes chargés depuis un CSV hébergé sur GitHub
- **Navigation** — menu latéral avec `streamlit-option-menu`
- **Multi-pages** — 4 pages accessibles après connexion
- **Session** — gestion de l'état de connexion et déconnexion

---

## Identifiants de démonstration

| Username | Password |
|----------|----------|
| `utilisateur` | `utilisateurMDP` |

---

## Installation

```bash
git clone https://github.com/DPewpew/Streamlit-Partie-3
cd Streamlit-Partie-3

pip install -r requirements.txt

streamlit run partie_3_chat.py
```

---

## Stack technique

| Catégorie | Outils |
|-----------|--------|
| Framework | Streamlit |
| Authentification | streamlit-authenticator |
| Navigation | streamlit-option-menu |
| Données | Pandas, CSV GitHub |
