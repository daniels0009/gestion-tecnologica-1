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

@then('the calculator returns "{expected:g}"')
def step_impl(context, expected):
    assert isinstance(expected, float)
    assert context.result == expected