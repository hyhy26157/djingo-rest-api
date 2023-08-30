1. create venv
1.1 source ./djangoenv/Scripts/activate


3. run server  - python <path_to_manage.py>/manage.py runserver
4. create jango application - python <path_to_manage.py>/manage.py startapp <namme of the app>
 4.1 edit the settings.py in the project folder and define the path of base folder * add in the app <name of the app> into the INSTALLED_APPS portion.
 4.2 edit the settings.py in the project folder and define the path of template folder & add in the template <name of the template> in the TEMPLATES portion.
 4.3 edit the settings.py in the project folder and define the path of static folder & add in the static <name of the static> in the STATICFILES_DIRS
5.  make migration for model - python manage.py makemigrations
6. run migration for model - python manage.py migrate
7. run shell - - python manage.py shell
8. improve security  - python <path_to_manage.py>/manage.py createsuperuser
8.1 add rights to user - <http://webpage>/admin 
<optional> 9 add faker data to test out the admin page. see populate_first_app.py
