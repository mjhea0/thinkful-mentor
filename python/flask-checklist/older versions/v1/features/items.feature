Feature: confirming that adding items to a checklist works
	
	Scenario: check that the form displays
		When I go to the checklist
		Then I should see the checklist

	Scenario: check to see if table is working
		When I go to the checklist
		And I submit the item and amount
		Then I should see the the item and amount added to a table	

	Scenario: check to see if completed tasks are strikethrough
		When I go to the checklist
		And I check the completed box
		Then i should see a strikethough through the item