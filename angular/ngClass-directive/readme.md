## ngClass

The [`ngClass`](https://docs.angularjs.org/api/ng/directive/ngClass) directive gives you the ability to conditionally change CSS classes via an expression in the view. 

### Example 1

```html
<ul class="checkboxList">
  <li class="unchecked" ng-repeat="todo in todos" ng-class="{'checked': todo.check}">
    <input type="checkbox" ng-model="todo.check">
    <span>{{todo.text}}</span>
  </li>
</ul>
```

Here, each todo in the list is appended to an `li` along with a checkbox. When the `to-do` model is updated - e.g., when a todo is checked or unchecked - then the appropriate class is applied. By setting the default class as the `unchecked` class, when an item is checked, the CSS class is changed from `unchecked` to `checked`.

Looking closer at `ng-class`, we are checking to see if the the checkbox is check. So, if the expression evaluates to true, the `checked` class is applied.

*Note*: You do not need a default class. Instead, you could just apply a class when the input is checked.

### Example 2

```html
<table class="table" ng-controller='employeeController'> 
  <tr ng-repeat='employee in directory' 
    ng-click='Employee($index)' 
    ng-class='{selected: $index==selectedRow}'> 
    <td>{{employee.name}}</td> 
    <td>{{employee.department}}</td>
  </tr> 
</table>
```

In this example, when an employee is clicked, the row number is grabbed from the controller:

```javascript
$scope.Employee = function(row) { 
  console.log(row)
  $scope.selectedRow = row;
};
```

The `$index` property evalautes to the index value of the employee in the for loop. Thus, the `selected` class is assigned when the index value is equal to the row number.

### Example 3

```html
<tr ng-repeat='employee in directory' 
  ng-click='Employee($index)' 
  ng-class="{zero: $index == 0, one: $index == 1, two: $index == 2}">
```

This is very similar to the previous example. See if you can figure it out on your own.

Another example: [http://jsfiddle.net/mjhea0/q8yLn/](http://jsfiddle.net/mjhea0/q8yLn/)

<hr>

Think about how you could use this directive for other events, like -

1. On a mouseover or button click
1. On a text value change

