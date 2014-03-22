@when(u'I go to the checklist')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')

@then(u'I should see the checklist form')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('my_wonderful_form')

@when(u'I submit the item and amount')
def step_impl(context):
    br = context.browser
    item = br.find_element_by_name("description")
    item.send_keys("apples")
    amount = br.find_element_by_name("amount")
    amount.send_keys("20")
    br.find_element_by_id("submit").click()

@then(u'I should see the the item and amount added to a table')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_class_name('open')

@when(u'I check the completed box')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    br.find_element_by_class_name("completed_box").click()

@then(u'I should see a strikethough through the item')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    assert br.find_element_by_class_name("closed")
