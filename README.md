# repoviewer

How to run the app
1. Create a virtual environment
2. install dependencies:
    $ pip install -Ur requirements.txt
3. setup database config in settings.py
4. run migrations:
    $ python manage.py migrate
5. run the app:
    $ python manage.py runserver
6. use the app
7. run the test
    $ python manage.py test --settings=repoviewer.test_settings
8. run coverage:
    $ cd repoviewer && coverage run --source='.' manage.py test viewer --settings=repoviewer.test_settings
9. generate coverage report:
    $ coverage report
