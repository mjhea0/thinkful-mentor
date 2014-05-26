Feature:
Confirming that the food form displays the correct nutritional information

    Scenario: 
        Given the food arguments includes the name of the food, calories, protein, amino_acid_profile, carbohydrates, fat
            When the food is accessed
            Then the amino_acid profile will be displayed.