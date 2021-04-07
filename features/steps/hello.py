from behave import *
import subprocess


def run_cmd(cmd, capture_output=False):
    return subprocess.run(cmd.split(" "), capture_output=capture_output)


@given("we have ignition installed")
def step_impl(context):
    process = run_cmd("poetry run ignition -h")
    assert process.returncode == 0


@when("hello is passed in as a command")
def step_impl(context):
    process = run_cmd("poetry run ignition hello", True)
    context.response = process.stdout


@then("the default hello message is printed out to stdout")
def step_impl(context):
    assert context.response.decode("utf-8") == "Hello world!\n"


@when("the hello command is passed in with a name option")
def step_impl(context):
    process = run_cmd("poetry run ignition hello -n tuhin", True)
    context.response = process.stdout


@then("a hello <name> message is printed out to stdout")
def step_impl(context):
    assert context.response.decode("utf-8") == "Hello tuhin!\n"
