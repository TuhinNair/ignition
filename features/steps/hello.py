from behave import *
from scripts import run_cmd


@given("we have ignition installed")
def step_impl(context):
    process = run_cmd("poetry run ignition -h", quiet=True)
    assert process.returncode == 0


@when("hello is passed in as a command")
def step_impl(context):
    process = run_cmd("poetry run ignition hello", capture_output=True)
    context.response = process.stdout


@then("the default hello message is printed out to stdout")
def step_impl(context):
    assert context.response.decode("utf-8") == "Hello world!\n"


@when("the hello command is passed in with a name option")
def step_impl(context):
    process = run_cmd("poetry run ignition hello -n tuhin", capture_output=True)
    context.response = process.stdout


@then("a hello <name> message is printed out to stdout")
def step_impl(context):
    assert context.response.decode("utf-8") == "Hello tuhin!\n"
