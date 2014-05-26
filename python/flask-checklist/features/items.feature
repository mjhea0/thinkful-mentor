Feature: confirming that adding items to a checklist works
    
    Scenario: check that the form displays
        When I go to the checklist
        Then I should see the checklist form

    Scenario: check to see if table is working
        When I go to the checklist
        And I submit the item and amount
        Then I should see the the item and amount added to a table  

    Scenario: check to see if completed tasks have a strikethrough
        When I go to the checklist
        And I check the completed box
        Then I should see a strikethough through the item

    Scenario: check that an error populates if the field is left blank
        When I go to the checklist
        And I submit a blank form
        Then I should see an error
