@when(u'I go to the homepage')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')

@then(u'I should see a question')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('question')

@then(u'I should see three options')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_class_name('answer')
