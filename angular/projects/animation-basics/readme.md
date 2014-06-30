# Angular Animation Basics

## Part 1

http://embed.plnkr.co/DjjogP/

### Before the button click:

**JS**

```javascript
$scope.fade = false;
```

**HTML**

```html
<h2 ng-class="{fade:fade}" class="" style="">Hello World!</h2>
```

### After the button click:

**JS**

```javascript
$scope.fade = true;
````

**HTML**

```html
<h2 ng-class="{fade:fade}" class="fade" style="">Hello World!</h2>
```

### What's happening?

On the button click, the value of `fade` is set to true, adding it to the DOM. This triggers the animation.

## Part 2

http://embed.plnkr.co/9Eujxd/

It's a little harder to see what's happening in this example, but Angular adds the appropriate classes - `ng-enter` and `ng-leave` - to the elements, during the animation cycle, which tiggers the subsequent CSS animation.

## Part 3

http://embed.plnkr.co/3UmSZy/preview

### Before the button click:

**HTML**

```html
<div id="rectangle" ng-show="showRectangle" class="btn btn-warning animate-rectangle ng-hide" ng-class="{ extra: extraClass }" style="">i am the rectangle</div>
```

### After the button click:

**HTML**

<div id="rectangle" ng-show="showRectangle" class="btn btn-warning animate-rectangle" ng-class="{ extra: extraClass }" style="">i am the rectangle</div>


### What's happening?

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

## Part 4



