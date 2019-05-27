from behave import given, when, then, step

import sys
sys.path.append("../..")

from sum import sum_list


@given('I have a calculator')
def step_impl(context):
    pass

@when('I add "{x:g}" and "{y:g}"')
def step_impl(context, x, y):
    assert isinstance(x, float)
    assert isinstance(y, float)
    context.result = sum_list([x, y])

@then('the calculator returns "{sum:g}"')
def step_impl(context, sum):
    assert isinstance(sum, float)
    assert context.result == sum