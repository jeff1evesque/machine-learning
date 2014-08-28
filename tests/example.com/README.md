README
------

### Information

Project includes directory and file structure to support small and large applications alike.

Tree below describes structure.

```
../procect_folder/
├── config.py = confuration file for flask + modules, such as SQL URI
├── env = python virtualenv folder. holds libraries and python bin for project
├── flask.wsgi = WSGI file for mod_wsgi
├── log
│   ├── access.log
│   └── error.log
├── README.md
├──run.py = Use to run flask development server vs using apache. Not for prod
│
├── app = actual application directory
   ├── __init__.py
   ├── mod_1 = example module. use modules to structure better. module can be anything from module that handles authentication, payment processing, etc
   │   ├── __init__.py = makes directory a python package
   │   ├── views.py = routing logic. module might also include models.py, forms.py, etc depending on what you're doing
   │   └── views.pyc
   ├── static = static files
   │   ├── css
   │   ├── fonts
   │   ├── img
   │   └── js
   └── templates = html templates with some examples inside. 
       ├── 404.html
       ├── home.html
       ├── layout.html
       └── mod_1
           └── test.html

```
