# Hero Team API

## Structure
```bash
requirements_full.txt # Liste des dépendances nécessaires.
main.py # Point d'entrée de l'application.
schemas/ # Contiendra les modèles Pydantic pour la validation.
db/ # Contiendra le fichier de connexion à la base de données.
crud/ # Contiendra les opérations CRUD sur chaque table.
routes/ # Contiendra les routes FastAPI.
tests/ # Contiendra les tests unitaires.
```

## Stack technique :

- FastAPI pour l'API
- SQLModel comme ORM
- PostgreSQL comme base de données
- Pydantic pour la validation des données
- Uvicorn pour exécuter le serveur
- HTTPX (TestcClient) pour exécuter les tests.
- Pytest pour exécuter les tests.

```bash
pip install fastapi
pip install uicorn
pip install sqlmodel
pip install pydantic
pip install httpx
pip install pytest
pip freeze > requirements_full.txt
```

## Deux modèles principaux :

- Hero: représente les héros.
- Team: représente les équipes à laquelles appartiennent les héros.

## 🚀 Lancer l'application

### 🧱 Prérequis

- Python 3.11
- [poetry](https://python-poetry.org/) ou `pip` pour la gestion des dépendances
- Virtualenv recommandé

---

### ⚙️ Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/<utilisateur>/hero_team_api.git
cd hero_team_api
```

2. Créer et activer un environnement virtuel :

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Installer les dépendances :

```bash
pip install -r requirements_full.txt
```

4. ▶️ Lancer le serveur

Depuis la racine du projet (`hero_team_api/`), lance la commande suivante :

```bash
uvicorn app.main:app --reload
```

Une autre alternative consiste à utiliser le script `run_uvicorn.py` qui se trouve dans le 
répertoire `utils`:

```bash
python -m app.utils.run_uvicorn
```