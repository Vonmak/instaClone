# instaClone
an imitation of instagram

## Live Link
[View Site](https://sniffgram.herokuapp.com/)


## User Story
Sign in to the application to start using.
Upload my pictures to the application.
See my profile with all my pictures.
Follow other users and see their pictures on my timeline.
Like a picture and leave a comment on it.
### Prerequisites

Use the package manager pip to install all project requirements. 
```sh
(virtual) $ pip install -r requirements.txt
```

## Built With

* [Django 4.0.4](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python3.10](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system


## Authors

* [Vonmak](https://github.com/Vonmak)

## Known Bugs
* When you click on follow it opens the followed users account but records the follow in the database.
* the issue is the number of follows dont show.
* also the email sending ability hasan issue.

<!-- Requirements -->

<!-- asgiref==3.5.2
beautifulsoup4==4.11.1
certifi==2022.5.18.1
cloudinary==1.29.0
dj-database-url==0.5.0
Django==4.0.5
django-bootstrap-v5==1.0.11
django-heroku==0.3.1
gunicorn==20.1.0
Pillow==9.1.1
psycopg2==2.9.3
psycopg2-binary==2.9.3
python-decouple==3.6
six==1.16.0
soupsieve==2.3.2.post1
sqlparse==0.4.2
urllib3==1.26.9
whitenoise==6.2.0
 -->