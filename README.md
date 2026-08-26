# ft_linear_regression 🚗

## Description
Ce projet est une introduction aux concepts de base du Machine Learning. Il consiste à implémenter un algorithme de régression linéaire simple (à une seule caractéristique) pour prédire le prix d'une voiture en fonction de son kilométrage, en utilisant la méthode de la descente de gradient.

## Structure du Projet
Le projet est divisé en deux programmes distincts :
* **Entraînement (`train.py`) :** Lit le fichier `data.csv`, entraîne le modèle en ajustant les variables (theta0 et theta1), et sauvegarde ces résultats.
* **Prédiction (`predict.py`) :** Demande un kilométrage à l'utilisateur et retourne le prix estimé en utilisant les variables préalablement calculées.

## Installation et Utilisation
1. Cloner le dépôt :
   `git clone [URL_DE_TON_REPO]`
2. Lancer le programme d'entraînement :
   `python3 train.py`
3. Lancer le programme de prédiction :
   `python3 predict.py`

## Fonctionnalités (Mandatory)
- Calcul de l'erreur moyenne.
- Mise à jour simultanée des variables temporelles.
- Pas d'utilisation de bibliothèques mathématiques complexes (comme numpy.polyfit) pour faire le travail à notre place.

## Bonus
- [ ] Visualisation des données sur un graphique.
- [ ] Tracé de la ligne de régression linéaire.
- [ ] Calcul de la précision de l'algorithme.
