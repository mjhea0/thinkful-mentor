# Flask RESTful API Final Project

## Description

Designing a REST API with Flask and Python, from a TDD/BDD perspective.

## High-level Overview

1. Define problem/pain points - "What problem are you solving?"
2. User workflow/stories. Create feature file for Behave - i.e.,
  ```
  Scenario: check that the form displays
    When I go to the home page
    Then I should see the login form
  ```
3. Mockup/wireframe. High Fidelty (pen, paper) -> Low Fidelity (bootstrap)
4. Convert user workflow/scenarios into pseudo code - which will eventually become comments
5. Discuss design patterns/programming paradigms. 
6. Break workflow/pseudo code into functions. Test with Behave while coding. BDD.
7. Program iteratively, starting lean. 
8. Test - Code - Refactor 
9. Add integration testing with PhantomJS. Perhaps use some mocking.

## APIs

### What is an API?

Put simply, an API is collection of functions that other programs can access or manipulate data from. Each function has an associated endpoint (also called a resource). One can make changes to a resource via the HTTP verbs:

1. GET - view a resource
2. POST - create a new resource
3. PUT - update a resourc
4. DELETE - delete a resource

### Basic REST Design Practices

URLs (enpoints) are used for identifying a specific resource, while the HTTP verbs define the actions one can take on those resources. Each resource should only have two URLs. The first is for a collection, while the second is for a specific element in that collection.

For example, let's say we are designing a basic todo API. The endpoint `/todos/` could be for the collection, while `/todos/<id>/` could be for a specific todo from the collection.

|                |         GET        | POST         | PUT                  | DELETE               |
|----------------|:------------------:|--------------|----------------------|----------------------|
| `/todos/`      | View all todos     | Add new todo | Update all todos     | Delete all todos     |
| `/todos/<id>/` | View specific todo | N/A          | Update specific todo | Delete specific todo |

We can then get more specific with our searches using query strings - i.e., `GET /todos/?limit=10`. This could potentially just return the first 10 todos from the collection.

### Workflow for creating an API via Flask

1. Source data
2. Setup persistence layer (database or JSON files or external API)
3. Add Flask
4. Setup/Install Flask-SQLAlchemy (if needed)
5. Create URLS/end points
6. Create Query Strings
7. Test, Test, Test
8. Add front end

## User Stories

User stories describe a feature told from the perspective of the end user. Use the following format:

- As a [type of user], I want [some goal or feature] so that [some reason].
- As a [type of user], I want [some goal or feature] because [some reason].
- As a [type of user], I can [some goal or feature]


