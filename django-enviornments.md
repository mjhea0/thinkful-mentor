# Django Enviornments

## virtualenv

[virtualenv](https://pypi.python.org/pypi/virtualenv) (virtual environment) is required when you run multiple projects on the same computer. Put simply, virtualenv manages all of your projects' dependencies, while also isolating them form one another.

When working on a project, make sure your virtualenv is installed and activated before installing dependencies. Also, make sure to create a *requirements.txt* file to maintain a record of all installed dependendencies as well as their versions:

```sh
$ pip freeze > requirements.txt
```

Add this final to your project root.

## shell

```python
$ manage.py runserver shell
```

## runserver

```python
$ manage.py runserver [optional port]
```


