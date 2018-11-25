# django-crud

This is the web application to manage Department and Employee details.

**Installation**

The installation is very straightforward and make sure you are using at least python 3.6.x and later.
Make sure *pip* setuptool is installed with python package.

Create virtual environment using following commands.

```
$ cd django-crud
$ pip install virtualenv
$ virtualenv env
```

Activate virtual environment.

*Linux or Mac*

```
$ source env/bin/activate
```

OR

*Windows*

```
$ env\Scripts\activate
```

Deactivate virtual environment.
```
(env) $ deactivate
```

Install dependencies/packages.

```
(env) $ pip install -r requirements.txt
```

Install *mysqlclient* to connect MySQL database.

Add `mysqlclient` to [requirements.txt](/requirements.txt) 

*Note(Windows): Requires Microsoft Visual C++ 14.0)*

or

Run following command to install *mysqlclient* system wide. 
```
$ pip install --only-binary :all: mysqlclient
```

**Migration**

Set environment variables (like, [Database credentials](https://github.com/omkar-hardwell/django-crud/blob/master/mywebapps/mywebapps/settings.py#L84-L97) etc.)

The migrate looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your [settings.py](/mywebapps/mywebapps/settings.py) file and the database migrations.

Run following commands.

```
(env) $ python mywebapps/manage.py migrate
(env) $ python mywebapps/manage.py makemigrations crudwebapp
(env) $ python mywebapps/manage.py migrate
```

**Running**

When all dependencies installed and configurations are set, run the application.

```
(env) $ python mywebapps/manage.py runserver
```

Access application by entering *http://127.0.0.1:8000/* or *http://localhost:8000/* url on browser.

Creating an admin user follow this [steps](https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user). 

Access admin panel *http://127.0.0.1:8000/admin/* or *http://localhost:8000/admin/* url on browser.


**Testing**

*Note: Test cases are pending.*

**For style guide enforcement (flake8)**

```
(env) $ flake8 file_path/
```

**References**

* [Python](https://www.python.org)
* [django](https://www.djangoproject.com/)
* [Flake8](http://flake8.pycqa.org)
