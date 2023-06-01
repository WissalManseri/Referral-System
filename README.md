# Système de recommandation de produits
Ce projet consiste à développer un système de recommandation de produits basé sur l'algorithme de filtrage collaboratif. Le système recommande des produits aux utilisateurs en fonction de leurs préférences passées et des préférences d'autres utilisateurs similaires.

#Installation
Cloner le dépôt GitHub sur votre machine locale :

        git clone https://github.com/WISSAL-MN/Referral-System-/.git
Installer les dépendances en utilisant pip :

          pip install -r requirements.txt
Exécuter le script principal :

python main.py

# Utilisation
Le script principal "main.py" charge les données d'un fichier CSV, crée une table de pivot pour représenter les interactions utilisateur-produit,
entraîne un modèle k-NN sur les données et génère des recommandations pour un utilisateur donné.

Pour générer des recommandations pour un utilisateur spécifique, vous pouvez modifier la ligne suivante dans le fichier "main.py" :

recommendations = recommend_products(1, 5)
Ici, le premier argument est l'ID de l'utilisateur et le deuxième argument est le nombre de recommandations à générer.

# Données
Les données doivent être stockées dans un fichier CSV avec les colonnes suivantes : "user_id", "product_id" et "rating". Les notes sont des nombres entiers compris entre 1 et 5.

Un exemple de fichier de données est inclus dans le dépôt GitHub sous le nom "product_data.csv".

# Auteur
Ce projet a été développé par wissalmanseri@gmail.com.

#Licence
Ce projet est sous licence MIT. Voir le fichier LICENCE pour plus d'informations.






