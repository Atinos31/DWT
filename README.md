Quick install
Run the following in a virtual environment of your choice:

$ pip install wagtail
(Installing outside a virtual environment may require sudo.)

Once installed, Wagtail provides a command similar to Django’s django-admin startproject to generate a new site/project:

$ wagtail start mysite
This will create a new folder mysite, based on a template containing everything you need to get started. More information on that template is available in the project template reference.

Inside your mysite folder, run the setup steps necessary for any Django project:

$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
Your site is now accessible at http://localhost:8000, with the admin backend available at http://localhost:8000/admin/.

This will set you up with a new stand-alone Wagtail project. If you’d like to add Wagtail to an existing Django project instead, see Integrating Wagtail into a Django project.

There are a few optional packages which are not installed by default but are recommended to improve performance or add features to Wagtail, including:

Elasticsearch.

Feature Detection.

Your first Wagtail site
Demo site
Integrating Wagtail into a Django project
The Zen of Wagtail

Happy coding!
