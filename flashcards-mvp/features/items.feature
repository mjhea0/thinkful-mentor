Feature: confirming that user can see questions and answers
    
    Scenario: check that a question displays
        When I go to the homepage
        Then I should see a question

    Scenario: check that options display
        When I go to the homepage
        Then I should see three options

    Scenario: check that an button displays next to each option
        When I go to the homepage
        Then I should see three buttons

