# Angular Kittens

## Part 1

```
Given I am on the index (`/#/`) page
When I click "New Kitten" in the navigation bar
Then a form is displayed (on a new route - `/#/new`)
When I enter the name of the kitten
And I enter an image url for the kitten
And I enter a bio for that kitten
When I click the "Create Kitten" button
Then the kitten is listed on the index page (`/#/`)
And the list displays a thumbnail of the kitten image
And the name of the kitten
And the kitten bio
And the number of likes a kitten has
```

## Part 2

> Make sure to add a service to store all kittens

```
When I visit the index (`/#/`) page
And I see a list of kittens
When I click the "View Comments" link for a kitten
Then I am shown all the comments for that kitten (on a new route - `/#/comments/:id`)
```

```
When I click the "Add Comment" link for a kitten on the comments (`/#/comments/:id`) page
Then I see a form (on the same page)
And I can input a comment body  
And when I click the "Create Comment" link
Then I can see my comment in the list of comments for that kitten
And I can no longer see the form
```

## Part 3

```
Given I am on the index page
And I see a list of kittens
When I click the "Like" link for a kitten
Then the number of likes for that kitten is increased by one
```

## Part 4

```
Given I am on the index page
And I click "Sort by Name"
Then the kittens are displayed in alphabetical order by name
And when I click "Sort by Likes"
Then the kittens are displayed in order of most likes to fewest likes
```
