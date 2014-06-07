# Angular + D3 + Flask

This is an introductory tutorial on developing an application using Angular with a Python-Flask backend. Starting with the backend, we'll be designing a RESTful API utilizing Python and the Flask web framework. Once complete, we'll shift to the frontend where we'll consume the data from the API endpoints with AngularJS and create some nice interactive charts and graphs with the D3 library. The final code designed in a way where you can easily swap out Flask for a different Python framework, like Django or Bottle.py, if you'd prefer.

Although you don't need to have had any experience with Angular, I asumme you do have working knowledge of HTML/CSS, Javascript, Python web development with Flask, and Git. To get up to speed on these technologies, please review the second Real Python course, *Web Development with Python*.

## What is Angular?

Angular is a powerful frontend framework used for building rich web applications.

As we move through this tutorial, you'll soon find out just how easy it is to add data to your page, since Angular works directly with HTML by simply extending its functionality, as well as keep it updated, because Angular is always *watching* for changes to occur on the DOM.

For more info on Angular, check out the offical [documentation](https://angularjs.org/).

With that, let's start with a basic Hello World app utilizing Angular templating and two-way binding along with Flask. If you're already feeling comfortable with Angular, feel free to skip this tutorial and move on to the main application, *Angular + D3 + Flask*.

## Hello, Angular!

### Boilerplate

Start by downloading the Flask boilerplate. Extract the contents. Move the directory wherever is convient to you in your file system. Create and activate a virtualenv. Install the requirements. Run the app.

Open your browser to [http://localhost:5000](http://localhost:5000) and you should see the familiar "Hello, World!" text staring back at you. Right now this is clearly a basic, static application. Now, let's add some Angular magic to quicky make it dynamic and much more fun!

### Angular

To add the Angular functionality that we need to make this app dynamic, we simply need to update the template.



### Basic Steps

1. Create basic project structure
1. Add Endpoints
1. Add Angular/D3
1. Add more endpoints using fake Data via Faker
1. Update Front end
1. Add AJAX
1. Add new Endpoints
1. Update Angular/D3
1. Add likes endpoints
1. Update Angular

### Create basic project structure

1. Create directory
1. Activate virtualenv
1. Install Flask
1. Project structure

    ```
    .
    ├── app
    │   ├── __init__.py
    │   ├── static
    │   │   ├── css
    │   │   │   └── main.css
    │   │   └── js
    │   │       └── main.js
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── base.html
    │   │   └── index.html
    │   └── views.py
    ├── app.py
    └── tests.py
    ```

1. Test to make sure it works
1. Delete .git
1. Create new git
1. Commit
1. PUSH

### Add Endpoints 

1. Note: front or back (your preference; MVPs start with front, longer projects generally start with back)
1. Set up test endpoint
1. Hit end point - http://localhost:5000/reps/1
1. Display JSON results
1. Add tests

### Add Angular/D3

1. Add dependencies
1. Follow directions here - https://github.com/cmaurer/angularjs-nvd3-directives
1. Display basic chart

### Add more endpoints

1. Total Posts
1. Comments, Users, Active Users

### Update Front end

1. Add navbar
2. Add header

### Add AJAX

1. Total Users
1. Active users, Posts, Comments

### Add new Endpoint

1. Total Foo
1. Total Bar

### Update Angular/D3

1. Foo - Add function to main.js for get
1. update dom
1. Bar

### Add likes endpoint

### Update Angular

1. main.js AJAX
1. update html
1. filter date (moment.js)



