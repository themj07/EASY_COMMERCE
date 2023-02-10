INSTALLATION : 


1 - activer environnement virtuel : .\venv\Scripts\activate

2 - installer dependance : pip install -r requirements. txt

3 - creer dans postgreSQL via pgAdmin4 une base de données du nom de dbeasycommerce et configuer le reste de informations en fonction de vos informations postgres dans le settings.py :
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'dbeasycommerce',
       'USER': 'Votre_user',
       'PASSWORD': 'Votre_password',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}


4 - acceder aux applications en fesant : cd final/finalproject

5 - Apres configurations du settings faire : 
- python manage.py makemigrations
- python manage.py migrate 

6 - lancer le server en fesant : python manage.py runserver 127.0.0.1:7000 

FONCTIONNALITE :

NB : Architecture du projet :
Ce projet comporte 3 applications : user ( tous ce qui est rapport avec l'utilsateur) , easycommerce (tous ce qui est en rapport avec la boutique de vente) , blog (tous ce qui est rapport avec le blog )

I/ Authentification : 

- possibilité de s'inscrire avec compte Gmail avec verification obligatoire avant de pouvoir se connecter

- possibilité de se connecter avec compte Gmail ou avec username

- possibilité recuperer le mot de passe en cas d'oublie grace à un mail envoyé à votre adresse d'inscription (obligatoire)

- si vous etes deja connecteé vous pouvez en appuiyant sur la section profile dans la navbar modifier le mot de passe , le prenom et votre gmail (plus besoin de verification par mail vu que vous etes dejà connecté 

- si vous etes un administrateur (superuser) vous pouvez en appuiyant sur la section admin( qui s'affiche que lorsque vous etes connctez et un superuser ) avoir accès à la base de données afin de pouvoir faire des ajouts ou des retraits d'informations

II/ Boutique de vente

- possibilite d'ajouter ou de retirer un ou plusieurs produits au panier selon la quantite choisie

III/ Blog

- Administrateur(superuser) peut publier des articles
 
- les utilisateurs peuvent commenter et repondre aux commentaires deja existants 

IV / Formulaire de contact 

V/ Bannière de cookies

Une bannière de cookies (avec la possibilité d'accepter ou de refuser)

VI/ Micro-services

-API REST pour intégrer les fonctionnalités dans une application mobile.

-API GraphQL pour améliorer la fluidité de l'application avec un query optimisé qui retourne un maximum d'informations.



