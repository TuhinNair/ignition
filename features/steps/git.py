from behave import *
from scripts import run_cmd


def ctx_resp_to_string(ctx_resp):
    return ctx_resp.decode("utf-8")


@when(
    "the user runs 'ignite --toolchain git --first-name John --last-name Doe --email john.doe@company.com'"
)
def step_impl(context):
    process = run_cmd(
        "poetry run ignition ignite --toolchain git --first-name John --last-name Doe --email john.doe@company.com --dry-run",
        capture_output=True,
    )
    assert process.returncode == 0
    context.response = process.stdout


@then("the git user profile is set with the user's name")
def step_impl(context):
    resp = ctx_resp_to_string(context.response)
    assert "git.user.name=John Doe\n" in resp


@then("the git email is set with user's email")
def step_impl(context):
    resp = ctx_resp_to_string(context.response)
    assert "git.user.email=john.doe@company.com\n" in resp


@then("the git commit template is configured")
def step_impl(context):
    resp = ctx_resp_to_string(context.response)
    assert "git.commit.template=ignition_default_git_commit.txt\n" in resp