# Instant Karma: Unit Testing with AngularJS

Unit tests are simple: Break your app up, testing each piece of functionality. Since BDD (red, green, refactor) is awesome, we'll utilize a BDD framework called Jasmine powered by Karma, a test runner.

## Setup

### Start Project

```sh
$ git clone https://github.com/angular/angular-seed.git angular-test-project
$ cd angular-test-project
```

### Install Dependencies

```sh
$ npm install
```

### Run the tests

```sh
$ npm test
```

Results:

```sh
Chrome 36.0.1985 (Mac OS X 10.8.5): Executed 5 of 5 SUCCESS (0.606 secs / 0.056 secs)
```

## Testing a Filter

### Write the test

Update *filtersSpec.js*:

```javascript
'use strict';

/* jasmine specs for filters go here */

describe('filter', function() {

  beforeEach(module('myApp.filters'));

  ... snip ...

  describe('concatenateString', function() {
    it('should append a supplied string at the end', inject(function(concatenateStringFilter) {
      expect(concatenateStringFilter('first','_second')).toEqual('first_second')
    }))
  })

});
```

**What's going on?**

1. `describe('filter', function()` provides the context that we're testing - our app's custom filters - so that the testing suite has access to it
2. `beforeEach(module('myApp.filters'))` indicates that as soon as the `myApp.filters` module is instantiated the tests are ran
3. This test is specifically targeting a filter called `concatenateString` that `should append a supplied string at the end`
4. `expect(appendStuffFilter('first','_second')).toEqual('first_second')` tests the actual filter - given the string 'first', we should expect `first_second` if `_second` is the supplied input; returns either `true` or `false`

### Run the test

```sh
$ npm test
```

You should get the following failure:

```sh
Chrome 36.0.1985 (Mac OS X 10.8.5) filter concatenateString should append a supplied string at the end FAILED
```

### Add the filter

Update *filters.js*:

```javascript
.filter('concatenateString', function() {
return function(text, string) {
    return text + string
}
});
```

Yup - this just concatenates two strings.

### Test again

Boom!

```
Chrome 36.0.1985 (Mac OS X 10.8.5): Executed 6 of 6 SUCCESS (0.189 secs / 0.054 secs)
```

Super simple. Let's move on to something a bit more complex.

