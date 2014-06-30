# Angular Animation Basics

## Part 1

http://plnkr.co/edit/QvxiW28A17VscZBrP20X?p=preview

### Before the button click:

```javascript
$scope.fade = false;
```

```html
<h2 ng-class="{fade:fade}" class="" style="">Hello World!</h2>
```

### After the button click:

```javascript
$scope.fade = true;
````

```html
<h2 ng-class="{fade:fade}" class="fade" style="">Hello World!</h2>
```

### What's happening?

On the button click, the value of `fade` is set to true, adding it to the DOM. This triggers the animation.

## Part 2
