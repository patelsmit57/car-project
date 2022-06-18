django = 4.0.7
psycopg2 = 2.9.3
pillow = 9.1.1
django-ckeditor = 3.5.2
django-multiselectfield = 3.5.2
django-colorfield = 0.7.0
django-allpath
python-decouple-3.6

# send email -> https://www.sitepoint.com/django-send-email/
# python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Premission --indent 4 > project_dump.json
# or 
# python -Xutf8 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json
# pip freeze > requirements.txt
#>heroku --version
# heroku login
# heroku whoami

dj-database-url-0.5.0
whitenoise-6.2.0    ->  static file use


heroku --version
heroku create smitpatel-car-project
                    ^^ app name
heroku git:remote -a smitpatel-car-project
git push heroku master
heroku open