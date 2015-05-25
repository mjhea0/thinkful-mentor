# Functional JavaScript - map, filter, reduce

## Map

Given an array, the `map()` method "transforms" each element in the array then returns a new array with the transformed values. Use this method when you find yourself looping through an array, transforming each element, and then pushing each one to a new array.

For example, take an array of numbers and return an array where each number from the original array is multiplied by 2.

**Non-functional**:

```javascript
var numbers = [1, 2, 3, 4, 5];
var newNumbers = [];

for (var i = 0; i < numbers.length; i++) {
  newNumbers.push(numbers[i] * 2);
}

console.log(newNumbers);
```

**`map()`**:

```javascript
var numbers = [1, 2, 3, 4, 5];

var newNumbersWithMap = numbers.map(function(num) {
   return num * 2;
});

console.log(newNumbersWithMap);
```

## Filter

Given an array, the `filter()` method creates a new array of elements from the original array that pass a specified test. Use this method when you find yourself looping through an array, filtering out certain elements with a conditional statement, and then pushing each value that passes the conditonal to a new array.

For example, take the `numbers` array and return an array with only the even numbers.

**Non-functional**:

```javascript
var numbers = [1, 2, 3, 4, 5];
var newNumbers = [];

for (var i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    newNumbers.push(numbers[i]);
  }
}

console.log(newNumbers);
```

**`filter()`**:

```javascript
var numbers = [1, 2, 3, 4, 5];

var newNumbersWithFilter = numbers.filter(function(num) {
   return num % 2 === 0;
});

console.log(newNumbersWithFilter);
```

## Reduce

Given an array, the `reduce()` method reduces all elements into a single total value. Use this method when you find yourself looping through an array and adding each element to a total value.

**Non-functional**:

```javascript
var numbers = [1, 2, 3, 4, 5];
var newNumbers = 0;

for (var i = 0; i < numbers.length; i++) {
  newNumbers += numbers[i];
}

console.log(newNumbers);
```

**`reduce()`**:

```javascript
var numbers = [1, 2, 3, 4, 5];

var newNumbersWithReduce = numbers.reduce(function(total, num) {
   return total + num;
}, 0);

console.log(newNumbersWithReduce);
```