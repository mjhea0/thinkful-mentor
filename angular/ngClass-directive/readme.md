## ngClass

The [`ngClass`](https://docs.angularjs.org/api/ng/directive/ngClass) directive gives you the ability to conditionally change CSS classes via an expression in the view. 

```html
<ul class="checkboxList">
  <li class="unchecked" ng-repeat="todo in todos" ng-class="{'checked': todo.check}">
    <input type="checkbox" ng-model="todo.check"/>
    <span class="done-{{todo.done}}">{{todo.text}}</span>
  </li>
</ul>
```

Here, each todo in the list is appended to an `li` along with a checkbox. When the `to-do` model is updated - e.g., when a todo is checked or unchecked - then the appropriate class is applied. By setting the default class as the `unchecked` class, when an item is checked, the CSS class is changed from `unchecked` to `checked`.

Think about how you could use this directive for other events, like -

1. On a mouseover or button click
1. When the text value of an element changes

*Note*: You do not have to set a default class. Instead, you could just have a class applied when the item is checked.