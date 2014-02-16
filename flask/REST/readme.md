# Tibor's Final Project

## Description

Designing a REST API with Flask and Python, from a TDD perspective.

## Steps

1. Start with user stories. 
2. Break user stories into pseudo code - which will eventually become comments.
3. Write Tests from a behavior standpoint - BDD
4. Test - Code - Refactor
5. Program iteratively, starting lean. OOP. Maybe some discussion on design patterns if there is time.

## APIs

### What is an API?

Put simply, an API is collection of functions that other programs can access or manipulate data from. Each function has an associated endpoint (also called a resource). One can make changes to a resource via the HTTP verbs:
1. GET - view a resource
2. POST - create a new resource
3. PUT - update a resourc
4. DELETE - delete a resource

### Basic REST Design Practices

URLs (enpoints) are used for identifying a specific resource, while the HTTP verbs define the actions one can take on those resources. Each resource should only have two URLs. The first is for a collection, while the second is for a specific element in that collection.

For example, let's say we are designing a basic todo API. The endpoint /todos/ could be for the collection, while /todos/<id>/ could be for a specific todo from the collection.

|              |         GET        | POST         | PUT                  | DELETE               |
|--------------|:------------------:|--------------|----------------------|----------------------|
| /todos/      | View all todos     | Add new todo | Update all todos     | Delete all todos     |
| /todos/<id>/ | View specific todo | N/A          | Update specific todo | Delete specific todo |

We can then get more specif with our searches using query strings - i.e., `GET /todos/?limit=10`. This could potentially just return the first 10 todos from the collection.

### Workflow

1. Source data
2. Setup persistence layer
3. Add Flask
4. Setup/Install Flask-SQLAlchemy
5. Create URLS
6. Create Query Strings
7. Test, Test, Test
8. Add front end

## User Stories

User stories describe a feature told from the perspective of the end user. Use the following format:

- As a <type of user>, I want <some goal or feature> so that <some reason>.
- As a <type of user>, I want <some goal or feature> because <some reason>.
- As a <type of user>, I can <some goal or feature>


