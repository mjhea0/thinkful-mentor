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


