Feature: confirming that user can see questions and answers, submit, and receive response
    
    Scenario: check that a question displays
        When I go to the homepage
        Then I should see a question

    Scenario: check that options display
        When I go to the homepage
        Then I should see three options

    Scenario: check that a button displays next to each option
        When I go to the homepage
        Then I should see three buttons

    Scenario: check that when a button is pushed a message is displayed
        When I go to the homepage
        And I click a button
        Then I should see a message


