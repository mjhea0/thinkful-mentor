# Angular Animation Basics with CSS Transitions

Angular 1.2 introduced us to the new animations API, [ngAnimate](https://docs.angularjs.org/api/ngAnimate), which supports four types of animations:

1. CSS Transitions
1. CSS keyframes
1. Javascript callbacks
1. Custom directives

Since CSS transitions are the easiest to work with, we'll start there. First, let's get your app animation ready.

## Getting Started

To get started, add the Angular animate JavaScript library to your HTML:

```html
<script type="text/javascript" src="https://code.angularjs.org/1.2.18/angular-animate.min.js"></script>
```

Then load the `ngAnimate` module into your Angular app:

```javascript
var app = angular.module('myApp', ['ngAnimate']);
```

Finally, add a class to the HTML element you wish to animate so that Angular can attach the animation to it.

That's it.

## CSS Transition Basics

Follow the Angular class-based naming conventions for the starting and ending animations:

| Animation | Directives                                  | Starting Class   | Ending Class           |
|-----------|---------------------------------------------|------------------|------------------------|
| enter     | ngIf, ngInclude, ngRepeat, ngSwitch, ngView | .ng-enter        | .ng-enter-active       |
| leave     | ngIf, ngInclude, ngRepeat, ngSwitch, ngView | .ng-leave        | .ng-leave-active       |
| move      | ngRepeat                                    | .ng-move         | .ng-move-active        |
| show      | ngShow, ngHide                              | .ng-hide-remove  | .ng-hide-remove-active |
| hide      | ngShow, ngHide                              | .ng-hide-add     | .ng-hide-add-active    |
| add       | ngClass                                     | .{class}-add     | .{class}-add           |
| remove    | ngClass                                     | .{class}-remove  | .{class}-remove        |

Please check the Angular [documentation](https://docs.angularjs.org/guide/animations) for more info.

## Examples

### Example 1

http://embed.plnkr.co/DjjogP/

#### Before the button click:

**JS**

```javascript
$scope.fade = false;
```

**HTML**

```html
<h2 ng-class="{fade:fade}" class="" style="">Hello World!</h2>
```

#### After the button click:

**JS**

```javascript
$scope.fade = true;
````

**HTML**

```html
<h2 ng-class="{fade:fade}" class="fade" style="">Hello World!</h2>
```

#### What's happening?

On the button click, the value of `fade` is set to true, adding it to the DOM. This triggers the animation.

### Example 2

http://embed.plnkr.co/9Eujxd/

It's a little harder to see what's happening in this example, but Angular adds the appropriate classes - `ng-enter` and `ng-leave` - to the elements, during the animation cycle, which tiggers the subsequent CSS animation.

### Example 3

http://embed.plnkr.co/3UmSZy/preview

#### Before the button click:

**HTML**

```html
<div id="rectangle" ng-show="showRectangle" class="btn btn-warning animate-rectangle ng-hide" ng-class="{ extra: extraClass }" style="">i am the rectangle</div>
```

#### After the button click:

**HTML**

<div id="rectangle" ng-show="showRectangle" class="btn btn-warning animate-rectangle" ng-class="{ extra: extraClass }" style="">i am the rectangle</div>


#### What's happening?

This example combines the functionality from the first two examples. You can see that before the button click, to show the rectangle, the rectangle has a class of `ng-hide` assigned to it. The actual CSS for `ng-hide` looks like this:

```css
.ng-hide {
  display:none!important;
}
```

Thus, when removed, you can see the element. However, you also have to add the following CSS so that the element is visible *during* the animation:

```css
#rectangle.ng-hide-add,
#rectangle.ng-hide-remove {
  display: block !important;
}
```

Like the last example, Angular adds the appropriate classes during the animation lifecycle to trigger the appropriate animation.

## Conclusion

Cheers!