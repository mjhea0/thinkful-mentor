Feature: Confirming that the tip calculator form works

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page

    Scenario: check that the total is correct 
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the correct total

    Scenario: check to see if edge cases are handled properly
        When I go to the tip calculator
        And I enter a string
        Then I should see an error message on the home page

    Scenario: check to see if edge cases are handled properly
        When I go to the tip calculator
        And I enter a negative number
        Then I should see an error message on the home page
