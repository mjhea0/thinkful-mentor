@given(u'the food arguments includes the name of the food, calories, protein, amino_acid_profile, carbohydrates, fat')
def step_impl(context):
    pass

@when(u'the food is accessed')
def step_impl(context):
    assert True is not False

@then(u'the amino_acid profile will be displayed.')
def step_impl(context):
    assert context.failed is False
