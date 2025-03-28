# Hero Team API

## Structure
```bash
requirements.txt # Liste des dépendances nécessaires.
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
pip freeze > requirements.txt
```

## Deux modèles principaux :

- Hero: représente les héros.
- Team: représente les équipes à laquelles appartiennent les héros.