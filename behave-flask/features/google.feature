Feature: Confirming that selenium is set up correctly

    Scenario: check that we can confirm the title of the Google home page
        When I go to the google home page
        Then I should see that the title is "Google"
