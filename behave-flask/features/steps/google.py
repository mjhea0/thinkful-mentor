@when (u'I go to the google home page')
def step_impl(context):
    context.browser.get('http://www.google.com')

@then(u'I should see that the title is "Google"')
def step_impl(context):
    assert context.browser.title == "Google"
