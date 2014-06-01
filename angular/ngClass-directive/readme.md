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

Another similar example: [http://jsfiddle.net/mjhea0/q8yLn/](http://jsfiddle.net/mjhea0/q8yLn/)

### Example 4: Strings

The value of the input or dropdown element is added as a CSS class. 

```html
<div class="container" ng-app>
    <form role="form">
         <h1>ngClass example<br><span class="small">String Syntax</h1>
        <br>
        <div class="form-group">
            <p>Use the dropdown to pick the class you want assign to the below 'h2' element. Or type the name of the class in the input box.</p>
            <select class="form-control" ng-model="text">
                <option value="">- Please pick a class -</option>
                <option>selected</option>
                <option>background</option>
                <option>purple</option>
                <option>text-danger</option>
                <option>bigger</option>
            </select>
            <br>
            <input class="form-control" ng-model="text" placeholder="- Please type a class -">
            <br>
             <h2 ng-class="text">Watch me change colors</h2>
        </div>
    </form>
</div>
```

[http://jsfiddle.net/mjhea0/At5Qk/](http://jsfiddle.net/mjhea0/At5Qk/)

### Example 5: Arrays

This syntax allows you to apply more than one class to a single element. Change the value of the first dropdown to update the background color and the other dropdown to update the font color.


```html
<div class="container" ng-app>
  <form role="form">
    <h1>ngClass example<br><span class="small">Array Syntax</h1>
    <br>
    <div class="form-group">
      <p>Use the dropdowns to pick the classes you want assigned to the below 'h2' element.
      <select class="form-control" ng-model="background">
        <option value="">- Class for the background color -</option>
        <option>brown</option>
        <option>red</option>
        <option>green</option>
        <option>blue</option>
        <option>purple</option>
      </select>
      <br>
      <select class="form-control" ng-model="text">
        <option value="">- Class for the font color -</option>
        <option>gray</option>
        <option>pink</option>
        <option>orange</option>
        <option>white</option>
        <option>black</option>
      </select>
      <br>
      <h2 ng-class="[background, text]">Watch me change colors</h2>
    </div>
  </form>
</div>
```

[http://jsfiddle.net/mjhea0/76bLd/](http://jsfiddle.net/mjhea0/76bLd/)

### Example 6: Maps

This syntax allows you to apply more than one class to a single element. Change the value of the first dropdown to update the background color and the other dropdown to update the font color.


```html
<div class="container" ng-app>
  <form role="form">
    <h1>ngClass example<br><span class="small">Map Syntax</h1>
    <br>
    <div class="form-group">
      <p>Use the checkboxes to pick the class you want assigned to the below 'h2' element.
      <div class="form-group">
        <input type="checkbox" ng-model="selected"> selected class<br>
        <input type="checkbox" ng-model="background"> background class<br>
        <input type="checkbox" ng-model="purple"> purple class<br>
        <input type="checkbox" ng-model="bigger"> bigger class<br>
        <input type="checkbox" ng-model="reverse"> reverse class<br>
      </div>
      <br>
      <h2 ng-class="{
        'selected class': selected,
        'background class': background,
        'purple class': purple,
        'bigger class': bigger,
        'reverse class': reverse
      }">Watch me change colors</h2>
    </div>
  </form>
</div>
```

[http://jsfiddle.net/mjhea0/ebt3K/](http://jsfiddle.net/mjhea0/ebt3K/)

<hr>

Think about how you could use this directive for other events, like -

1. On a mouseover or button click
1. On a text value change

