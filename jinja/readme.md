# Primer on Jinja Templating

Flask includes the powerful [Jinja](http://jinja.pocoo.org/docs/) templating language, right out of the box. It's modelled after Django templates (but it renders much faster), and, although, Flask does not force you to use any templating language, it assumes that you'll be using Jinga since it does come pre-installed.

For those who have not been exposted to a templating language before, such languagues essentially contain variables as well as some programming logic, which when evaluated (or rendered into HTML) are replaced with **actual** values. The variables and/or logic are placed between tags or delimeters. For example, Jinga templates use `{% ... %}` for expressions or logic (like for loops), while `{{ ... }}` are used for outputting the results to the template. The latter tag, when rendered, is replaced with a value or values, which are seen by the end user.

## Quick Examples

Make sure you have Jinja installed before running these examples - `pip install jinja2`

First:

```sh
>>> from jinja2 import Template
>>> t = Template("Hello {{ something }}!")
>>> t.render(something="World")
u'Hello World!'
>>>
>>> from jinja2 import Template
>>> t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
>>> t.render()
u'My favorite numbers: 1 2 3 4 5 6 7 8 9 '
```

Notice how the actual output rendered to the user falls within the `{{ ... }}` tags.

## Flask Examples

1. Create the following product structure:
  ```sh
  ├── app
  │   ├── __init__.py
  │   ├── models.py
  │   ├── static
  │   ├── templates
  │   └── views.py
  ├── requirements.txt
  └── run.py
  ```

2. Activate a virtualenv then install flask:
  ```
  $ pip install flask
  ```

3. 
