I'm putting together a post on conventions/best practices for Angular newbies. These are some of the hurdles that my students faced.

# Tentative outline. 

Thoughts?

## Best Practices
1. MVC/MV Presenter/MVVW - whatever you want to call the third piece (controller, presenter, view-model, whatever, *) - just adhere to separating the model, view, and business logic. In other words, model updates view, user consumes view, user interacts with controller to manipulate/update model
1. DRY - this is a given, but it doesn't hurt to repeat
1. Do not got against the framework; in most cases, Angular offers a reasonable solution - find it. Stay away from jQuery, especially in the Angular controller. Be smart with hacking. 
1. Learn directives and how to compartmentalize/modularize code. The quicker you do, the better off you will be.
1. Did I mention refactor. Refactor, refactor, reactor. 
1. Building blocks - interpolation, controller

## Be aware that

1. It's easy to write bad code, so be curious - look at the API (yes, there's a lot of it - but it is readable), refactor, write tests (just do it). TDD can help a lot.
1. Angular is a SPA. Treat it that way. Learn to leverage it.
1. Error messages suck. Learn to Google. Use Stack Overflow. Read the source code. And make sure to take advantage of the vibrant community behind the framework!
1. $scope is magic. It's not a model, yet it references the model; and it's not the view, yet it's consumed by the view. $scope is implicitly called in the view. It's there, beneath the hood, binding the model and view. Besides, directives this is the most important thing to understand and often the biggest hurdle.

# Feedback 1

Few quick points I could think of...

 - I usually describe $scope as being the gateway between the model and the view.  Nothing should cross that boundary without being routed through $scope.
 - Keep your controllers skinny, don't keep business logic in your controller methods, let a service manage data manipulating and access.  The controller should just coordinate access between your services <-> $scope <-> view
 - I get asked "so where is the model" from a lot of people, thinking that the model is some magic Angular feature that will give them extension methods (like backbone models).  The model is your service (data + business logic).
 - Where possible let the view manage display logic, if you're finding that you are creating a bunch of $scope.showCustomerPanel style of properties, revisit your model design to see if you can manage view state there, if it doesn't quite add up, extend your $scope with a domain view model object property like $scope.panels.customer.show.  This will lead to cleaner controllers and more logically separated UI view state management.
 
## Feedback 2

Have you tried using Batarang for debugging?  https://chrome.google.com/webstore/detail/angularjs-batarang/ighdmehidhipcmcojjgiloacoafjmpfk?hl=en  It adds a tab to the inspector/debugger for view Scopes, models, etc.

Also, I just got back from Future Insights conference and had attended a full-day Angular bootcamp lead by John Lindquist. One of the things that stood out to me in his workshop was his use of the "controller as" syntax.  I was under the impression it was still considered experimental but after talking with him he told me  it's now considered a best practice.  Things change pretty quickly I guess!  I noticed that using controller as made the hierarchy a lot cleaner and helps to demystify the "$scope" object that is used for a bunch of things.  It also helps clarify what properties you are accessing:

```
<div ng-controller="GroupCtrl as group">
   <h2>{{ group.title }}</h2>
   <div ng-controller="GroupItemCtrl as item">
      <h3>{{ group.title}} - {{ item.title }}</h3>
   </div>
</div>
```

The JavaScript behind it changes a little bit as well.  Most importantly, you attach properties to the controller itself rather than the scope.  The created $scope, then, is used only for Angular-specific things such as watching, broadcasting, etc.

```
app.controller('GroupCtrl', function() {
   this.title = "Group Title";
   this.updateGroup = function() { }
   // other properties
});
```

As you can see, the $scope is not even injected into the controller unless it's needed for something.  This keeps the code cleaner and avoids treating $scope as some confusing black box.  The main downside of this approach is having to know what you named the controller when using the "as xxxx" format.  But accurate naming of dependencies is something you have to be mindful of with Angular anyway so doesn't seem too much of a stretch.

## More Feedback ...
